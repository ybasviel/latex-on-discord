import discord
import re
import subprocess

# 自分のBotのアクセストークン
with open("bot.token") as tokenfile:
    TOKEN = tokenfile.read()

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('LaTeX botがログインしました')
    

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):

    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    #latex文法
    if message.content.startswith("```latex"):
        text = message.content
        text = text[8:len(text)-3]
        #```latex〜```を取り外す

        imgpath = "./latexondiscord/image.png"
        #生成される画像のパス

        formerupdatetime = os.path.getctime(imgpath) #画像の更新時刻を確認
        latexmessage(text) #画像作成
        nowupdatetime = os.path.getctime(imgpath) #画像の更新時刻を確認
        if formerupdatetime == nowupdatetime: #画像の更新がされていないとき
            await message.channel.send("Syntax error!!")
        else: #画像がきちんと更新されているとき
            await message.channel.send(file=discord.File(imgpath))


def latexmessage(message):
    text = repr(message) #バックスラッシュを2倍にしてくれるらしい
    text = text[1:len(text)-1] #reprでつけられた''の囲いを外す

    #テンプレを開く
    with open("./latexondiscord/latex-on-discord-template.tex") as file:
        nakami = file.read()
        #文章を挿入
        onew = re.sub("ここに文章を挿入",text, nakami,flags=re.DOTALL)

    #コンパイルする方のファイルを開く
    with open("./latexondiscord/latex-on-discord.tex", mode="w") as file:
        file.write(onew) #書き込む

    #シェルスクリプトにコンパイルしてもらう
    subprocess.run('./latexondiscord/textopng.sh')

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)