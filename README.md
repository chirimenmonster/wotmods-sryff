# mod SryFF

This mod provids the function of sending "sry" to team chat when you 'erroneously' an ally.

*Read this in other languages: [English](README.md), [日本語](README.ja.md)*

## Installation

Copy the wotmod file `chirimen.sryff_<version>.wotmod` to your WoT's mods folder `<WoT_game_folder>/mods/<WoT_version>`.

The mods folder is like, for example, `C:\Games\World_of_Tanks\mods\1.4.0.1`,
and the wotmod file is like `chirimen.sryff_0.2.wotmod`.
Please read the version number as appropriate.


## Configuration

If you want to change the default behavior, put the configuration file.

The configuration file is `<WoT_game_folder>/mods/configs/chirimen.sryff/config.xml`.
There is no version number.

The configuration file is in XML format (encoding is UTF-8).
The default setting is the same as the following.

``` xml
<config.xml>
    <delay>3.0</delay>
    <cooldown>12.0</cooldown>
    <message>sry</message>
</config.xml>
```

The meaning of each element is as follows.

+ **delay**:
This is the delay (in seconds) until team chat is sent after shooting.
By default, I will send a chat after 3.0 seconds.
+ **cooldown**:
The time (in seconds) after sending cooldown team chat until next SryFF becomes valid.
Set so that chat is not sent too much with machine cannon etc.
By default, we do not send chat for 12.0 seconds.
+ **message**:
The content of the team chat to send. By default it simply sends "sry".


## Advanced configuration

The contents of chat can include erroneous player name and vehicle name.
A character string enclosed with a variable name in {} is expanded to the contents of the variable.

The following variables can be used.

+ **playerName** of the opponent player
+ **vehicleName** of the other car

For example, if you include the name of the opponent player in the chat message, it will be as follows.

```xml
<config.xml>
    <delay>3.0</delay>
    <cooldown>12.0</cooldown>
    <message>sry {playerName}</message>
</config.xml>
```
