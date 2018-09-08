

# -*- coding: utf-8 -*-
# filename: handle.py

import hashlib
import web
import reply
import receive

class Handle(object):
    def POST(self):
	try:
            webData = web.data()
            print "Handle Post webdata is ", webData   
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                content = "pull test! git"
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            elif isinstance(recMsg,receive.Msg) and recMsg.MsgType == 'image':
                toUser=recMsg.FromUserName
                fromUser=recMsg.ToUserName
                mediaId=recMsg.MediaId
                replyMsg = reply.ImageMsg(toUser,fromUser,mediaId)
                return replyMsg.send()
            # elif isinstance(recMsg,)
            if isinstance(recMsg, receive.EventMsg):
                if recMsg.Event == 'CLICK':
                    if recMsg.Eventkey == 'mpBind':
                        content = "enter course code"
                        # content = "输入课程代码".encode('utf-8')
                        replyMsg = reply.TextMsg(toUser, fromUser, content)
                        return replyMsg.send()

            # else:
            print "do nothing"
            return "success"
        except Exception, Argment:
            return Argment
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return "hello, this is handle view"
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = "wangergou"

            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print "handle/GET func: hashcode, signature: ", hashcode, signature
            if hashcode == signature:
                return echostr
            else:
                return ""
        except Exception, Argument:
            return Argument
