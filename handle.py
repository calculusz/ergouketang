

# -*- coding: utf-8 -*-
# filename: handle.py
from basic import Basic
import hashlib
import web
import reply
import receive
import media
import DB as db
import hist
import json

class Handle(object):
    def POST(self):
	try:
            webData = web.data()
            con = db.connectdb()
            print "Handle Post webdata is ", webData
            recMsg = receive.parse_xml(webData)
            is_b=db.check_binding(con,recMsg.FromUserName)
            print(is_b)
            if  is_b!=1 and isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text' :
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
                        db.insert_user(con,toUser)

                        return replyMsg.send()
                    elif recMsg.Eventkey == 'mpState':
                        toUser = recMsg.FromUserName
                        fromUser = recMsg.ToUserName
                        re, len, fn=db.query_ppt(con,toUser)
                        hist.create_hist(len,re,fn)
                        accessToken = Basic().get_access_token()
                        myMedia = media.Media()
                        mediaType = "image"
                        res=myMedia.uplaod(accessToken,'./img/{0}.jpg'.format(fn),mediaType)
                        data = json.loads(res)
                        media_id = data['media_id']
                        print(media_id)
                        replyMsg = reply.ImageMsg(toUser, fromUser, media_id)
                        return replyMsg.send

            # else:
            print "do nothing"
            closedb(db)
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
