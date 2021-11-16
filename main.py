import discord
import platform
import key

client = discord.Client()


@client.event
async def on_ready():
    print("on_ready")
    print(discord.__version__)


@client.event
async def on_message(message): 
    
    # 送信者がbotである場合は弾く
    if message.author.bot:
        return 
    # メッセージの本文が 鳴いて だった場合
    if message.content == "こっこ":
        # メッセージが送られてきたチャンネルに送る
        await message.channel.send("こっこ なんの？ 何曜日？ 何時？")
        # content = random.choice(random_contents)
        # await message.channel.send(content)
    elif message.content == "おはよう！":
        await message.channel.send("こけこっこー！")
        
    ## --- DEV MODE ---
    elif message.content == "こっこえんぶ":
        await message.channel.send(str(platform.platform()) + "\n Google Cloud Engine -e2-micro -us-west0")

# ------ 実装メモ -----
# 1. メッセージを分解して辞書に登録
#   dict = {内容:[曜日,時間]}
# 2. ループを作成してdateモジュールを設定
#   dateモジュールの中で曜日に変換して，辞書を読む
#   if 辞書の中と曜日が一致して，時間が一致すれば，await発火
# 3. 2を30秒ごとに更新すれば毎時間読める
# 4. 削除機能を作る
    
tokens = key.Token()
client.run(tokens)