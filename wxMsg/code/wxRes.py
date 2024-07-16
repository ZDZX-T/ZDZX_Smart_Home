from flask import Flask, request
from WXBizMsgCrypt3 import WXBizMsgCrypt
import xml.etree.cElementTree as ET
import sys

app = Flask(__name__)

sToken = ''  # 填写接收消息服务器配置页面生成的Token
sEncodingAESKey = ''  # 填写接收消息服务器配置页面生成的EncodingAESKey
sCorpID = ''  # 填写企业ID


@app.route('/', methods=['GET'])
def handle_get_request():
    # 获取 GET 请求中的参数
    sVerifyMsgSig = request.args.get('msg_signature')
    sVerifyTimeStamp = request.args.get("timestamp")
    sVerifyNonce = request.args.get("nonce")
    sVerifyEchoStr = request.args.get("echostr")
    wxcpt = WXBizMsgCrypt(sToken, sEncodingAESKey, sCorpID)
    ret, sEchoStr = wxcpt.VerifyURL(sVerifyMsgSig, sVerifyTimeStamp, sVerifyNonce, sVerifyEchoStr)
    # 返回带有参数值的响应
    if ret != 0:
        print('解析错误')
        sys.exit(0)
    return sEchoStr


if __name__ == '__main__':
    app.run(debug=False)
