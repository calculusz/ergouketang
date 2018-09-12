#coding=utf-8
import basic
import urllib
b=basic.Basic()
access_token=b.get_access_token()
data='''
{
	"touser": "o1bMd0775CIi3NuFPkDg1gnyvwDo",
	"template_id": "CO8ABJrb3UJ3Foqx_uN1dJQXRXAP9IhiUdGeo5sxpZA",
	"url": "http://www.163.com",
	"data": {
		"first": {
			"value": "新的课件发布",
			"color": "#173177"
		},
		"keyword1": {
			"value": "神经网络",
			"color": "#173177"
		},
		"keyword2": {
			"value": "王二狗",
			"color": "#173177"
		},
		"keyword3": {
			"value": "东9大石头",
			"color": "#173177"
		},
		"keyword4": {
			"value": "猴年马月",
			"color": "#173177"
		},
		"Remark": {
			"value": "点击详情下载",
			"color": "#173177"
		}
	}
}
'''
postUrl = "https://api.weixin.qq.com/cgi-bin/message/custom/send?access_token=%s" % access_token
if isinstance(data, unicode):
    data = data.encode('utf-8')
urlResp = urllib.urlopen(url=postUrl, data=data)
print(urlResp.read())