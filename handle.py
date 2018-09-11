

# -*- coding: utf-8 -*-
# filename: handle.py

import hashlib
import web
import reply
import receive
import DB as db

class Handle(object):
    def POST(self):
	try:
            webData = web.data()
            con = db.connectdb()
            print "Handle Post webdata is ", webData
            recMsg = receive.parse_xml(webData)
            is_b=db.check_binding(con,recMsg.FromUserName)
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text' and is_b!=1:
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                content = "pull test! git"
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            elif isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text' and is_b==1:
                print("courseid:"+recMsg.Content)
                db.bind_courese(con,recMsg.FromUserName,recMsg.Content)
                return 'success'


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

                        toUser = recMsg.FromUserName
                        fromUser = recMsg.ToUserName
                        print(toUser)
                        content = "enter course code"
                        replyMsg = reply.TextMsg(toUser, fromUser, content)
                        # con=db.connectdb()
                        db.insert_user(con,toUser,'')

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
