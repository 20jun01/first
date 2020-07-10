from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import os

app = Flask(__name__)

#環境変数取得
YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

""" もし、ランダム出力にしたければこっちに切り替える"""
# def article():
#     import random
#     import datetime
#     links = []
#     now = datetime.date.today().strftime("%Y/%m/%d").split("/")
#     index = int(now[0]+now[1]+now[2])
#     random.seed(index)
#     with open("article_link.txt") as fp:
#         num = int(fp.readline())
#         for i in range(num):
#             links.append(fp.readline())
#     r = random.randint(0,num-1)
#     return links[r]

"""順に出力したければこっち"""
def article():
    import datetime
    links = []
    now = datetime.date.today().strftime("%Y/%m/%d").split("/")
    index = int(now[0]+now[1]+now[2])
    with open("article_link.txt") as fp:
        num = int(fp.readline())
        for i in range(num):
            links.append(fp.readline())
    r = index % num
    return links[r]

"""上記と同様"""
# def quiz():
#     import random
#     import datetime
#     links = []
#     now = datetime.date.today().strftime("%Y/%m/%d").split("/")
#     index = int(now[0] + now[1] + now[2])
#     random.seed(index)
#     with open("quiz.txt") as fp:
#         num = int(fp.readline())
#         for i in range(num):
#             links.append(fp.readline())
#     r = random.randint(0, num - 1)
#     return links[r]

def quiz():
    import datetime
    links = []
    now = datetime.date.today().strftime("%Y/%m/%d").split("/")
    index = int(now[0] + now[1] + now[2])
    with open("quiz.txt") as fp:
        num = int(fp.readline())
        for i in range(num):
            links.append(fp.readline())
    r = index%num
    return links[r]

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    special = ["論文", "クイズ"]
    if event.message.text in special:
        text = event.message.text
        if text == special[0]:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="今日の論文はこれ！！\n"+article())
            )
        if text == special[1]:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="問題!!\n\n"+quiz()+"\n\n答えはbotの作成者に聞いてね!!!")
            )
    else:
        line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
#    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)