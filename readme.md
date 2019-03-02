# mod SryFF

## この mod は

味方を「誤射」したときにチームチャットに "sry" を送る機能を提供します。

## インストール

WoT の mods フォルダ `<WoT_game_folder>/mods/<WoT_version>` に
wotmod ファイル `chirimen.sryff_<version>.wotmod` をコピーします。

mods フォルダは例えば `C:\Games\World_of_Tanks\mods\1.4.0.1` のようになっていて、
wotmod ファイルは `chirimen.sryff_0.2.wotmod` のようになっています。
バージョン番号のところは適当に読み替えてください。

## 設定

デフォルトの動作を変更したいときは設定ファイルを置きます。

設定ファイルは `<WoT_game_folder>/mods/configs/chirimen.sryff/config.xml` です。
バージョン番号はありません。

設定ファイルは XML 形式です（エンコーディングは UTF-8）。
デフォルトの設定は次と同じです。

```
<config.xml>
    <delay>3.0</delay>
    <cooldown>12.0</cooldown>
    <message>sry</message>
</config.xml>
```

各要素の意味は下記のようになります。

+ `delay`
射撃後にチームチャットを送るまでの遅延（秒）です。
デフォルトでは 3.0 秒後にチャットを送ります。
+ `cooldown`
チームチャットを送ってから、次に SryFF が有効になるまでの時間（秒）です。
機関砲などでチャットを送りすぎないように設定します。
デフォルトでは 12.0 秒間はチャットを送りません。
+ `message`
送るべきチームチャットの内容です。
デフォルトでは単に "sry" と送ります。

## 高度なメッセージ

チャットの内容に誤射相手のプレイヤー名や車輌名を含めることができます。
{} で変数名をくくった文字列が、変数の内容に展開されます。

下記の変数が使用可能です。

+ `playerName` 相手のプレイヤー名
+ `vehicleName` 相手の車輌名

例えばチャットメッセージに相手プレイヤー名を含める場合は次のようになります。

```
<config.xml>
    <delay>3.0</delay>
    <cooldown>12.0</cooldown>
    <message>sry {playerName}</message>
</config.xml>
```

