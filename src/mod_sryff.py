
import BigWorld
import ResMgr
from PlayerEvents import g_playerEvents
from gui.battle_control.battle_constants import BATTLE_CTRL_ID
from messenger import MessengerEntry
from messenger.m_constants import BATTLE_CHANNEL, PROTO_TYPE
from messenger.proto.interfaces import IEntityFindCriteria

class MOD:
    AUTHOR = '${author}'
    NAME = '${name}'
    VERSION = '${version}'
    DESCRIPTION = '${description}'
    CONFIG = '../mods/configs/chirimen.sryff/config.xml'

class DEFAULT:
    DELAY = 3.0
    COOLDOWN = 12.0
    MESSAGE = 'sry'


def init():
    BigWorld.logInfo(MOD.NAME, '{0} {1}'.format(MOD.NAME, MOD.VERSION), None)
    control =  Control()
    g_playerEvents.onAvatarReady += control.onAvatarReady


class _Criteria(IEntityFindCriteria):
    def __init__(self, channelSetting):
        super(_Criteria, self).__init__()
        self.__channelSetting = channelSetting

    def filter(self, channel):
        return channel.getProtoType() is PROTO_TYPE.BW_CHAT2 and channel.getProtoData().settings is self.__channelSetting


class Control(object):
    def __init__(self):
        section = ResMgr.openSection(MOD.CONFIG)
        try:
            if section:
                BigWorld.logInfo(MOD.NAME, 'found config file', None)
                self.delay = section.readFloat('delay', DEFAULT.DELAY)
                self.cooldown = section.readFloat('cooldown', DEFAULT.COOLDOWN)
                self.message = section.readString('message', DEFAULT.MESSAGE)
            else:
                raise
        except:
            BigWorld.logInfo(MOD.NAME, 'use default settings', None)
            self.delay = DEFAULT.DELAY
            self.cooldown = DEFAULT.COOLDOWN
            self.message = DEFAULT.MESSAGE
        self._ready = 0

    def onAvatarReady(self):
        BigWorld.logInfo(MOD.NAME, 'onAvatarReady', None)
        msgsCtl = BigWorld.player().guiSessionProvider.shared.messages
        msgsCtl.onShowPlayerMessageByCode += self.onShowPlayerMessageByCode
        msgsCtl.onShowPlayerMessageByKey += self.onShowPlayerMessageByKey
        self.teamChatCtrl = None

    def onShowPlayerMessageByCode(self, code, postfix, targetID, attackerID, equipmentID):
        BigWorld.logInfo(MOD.NAME, 'onShowPlayerMessageByCode: ({}, {}, {}, {}, {})'.format(code, postfix, targetID, attackerID, equipmentID), None)

    def onShowPlayerMessageByKey(self, key, args, _):
        BigWorld.logInfo(MOD.NAME, 'onShowPlayerMessageByKey: ({}, {})'.format(key, args), None)
        if key == 'ALLY_HIT':
            self.delayedExecution(self.delay, self.cooldown, lambda: self.sendTeamChat(self.message))

    def sendTeamChat(self, text):
        BigWorld.logInfo(MOD.NAME, 'sendTeamChat: "{}"'.format(text), None)
        if self.teamChatCtrl is None:
            self.teamChatCtrl = MessengerEntry.g_instance.gui.channelsCtrl.getControllerByCriteria(_Criteria(BATTLE_CHANNEL.TEAM))
        self.teamChatCtrl.sendMessage(text)

    def delayedExecution(self, delay, cooldown, function):
        now = BigWorld.time()
        if now < self._ready:
            return
        BigWorld.logInfo(MOD.NAME, 'delayedExecution: delay={}, func={}'.format(delay, function), None)
        BigWorld.callback(delay, function)
        self._ready = now + delay + cooldown

