#coding=utf-8
import basic
import urllib
def send_ppt():
    b=basic.Basic()
    access_token=b.get_access_token()
    data='''
    {
        "touser": "o1bMd085OVPCVhib2XBQpEv_aYVM",
        "template_id": "CO8ABJrb3UJ3Foqx_uN1dJQXRXAP9IhiUdGeo5sxpZA",
        "url": "http://www.wechatshop.mobi:8080/counter/static/PPT.html",
        "data": {
            "first": {
                "value": "新的课件发布",
                "color": "#173177"
            },
            "keyword1": {
                "value": "翻转课堂",
                "color": "#173177"
            },
            "keyword2": {
                "value": "王老师",
                "color": "#173177"
            },
            "keyword3": {
                "value": "东9-201",
                "color": "#173177"
            },
            "keyword4": {
                "value": "2018-8-22",
                "color": "#173177"
            },
            "Remark": {
                "value": "点击详情下载",
                "color": "#173177"
            }
        }
    }
    '''
    postUrl = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=%s" % access_token
    if isinstance(data, unicode):
        data = data.encode('utf-8')
    urlResp = urllib.urlopen(url=postUrl, data=data)
    print(urlResp.read())
def send_video():
    b = basic.Basic()
    access_token = b.get_access_token()
    data = '''
        {
            "touser": "o1bMd085OVPCVhib2XBQpEv_aYVM",
            "template_id": "tHhpwDmV_rMwVZX-gs2rbHgj7YwnBxd0UEIawSI-w2s",
            "url": "http://www.bilibili.com/video/av30721042/?share_source=weixin&ts=1540128921&share_medium=iphone&bbid=90deae9844a6b7c2fe415db03dc1fa15",
            "data": {
                "first": {
                    "value": "你好同学，新的教学视频发布了，请及时观看预习！",
                    "color": "#173177"
                },
                "keyword1": {
                    "value": "翻转课堂导论",
                    "color": "#173177"
                },
                "keyword2": {
                    "value": "2018-10-08",
                    "color": "#173177"
                },

           
                "Remark": {
                    "value": "点击详情观看",
                    "color": "#173177"
                }
            }
        }
        '''
    postUrl = "https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=%s" % access_token
    if isinstance(data, unicode):
        data = data.encode('utf-8')
    urlResp = urllib.urlopen(url=postUrl, data=data)
    print(urlResp.read())
if __name__ == '__main__':
    send_video()