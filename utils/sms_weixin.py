#-*- coding:utf-8 -*-
'''
Created on 2016/6/21

@author: QiRui.Su schangech@gmail.com
'''

import requests
import json
import urllib2
from datetime import *
import time
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
class GetToken():
    '''
    Get the token
    '''
    
    def __init__(self):
        '''
        corpid  -- 企业Id
        corpsecret  --  管理组的凭证密钥
        '''
        #self.url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wx053fd424ed53c149&corpsecret=wqlTerwiN4-9axDI1ThI5uhZ3KDcPmS1Yt9xKC2YAT_cRTTBdhMP0XtWO5zEkyGI"
        self.url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wx053fd424ed53c149&corpsecret=bMa1QAVUXt7RXjkZ4q88-jD2AJ4n_S1DkCSuA-He2Uuw41RZLNnhUb8_zu-ZY_FE"
        # wx053fd424ed53c149
        # yhw8U54y2pnmkJC-J6sn5dc4R8x6s9vt7rIkRBxOvd9i18t7fU5GMobb7PhiYn4l

    def get_token(self, create_time_stamp = 0):
        cur_time_stamp = int(time.time())
        if cur_time_stamp - create_time_stamp >= 7200 :
            create_time_stamp = int(time.time())
            r = requests.get(self.url)
        return r.json()
    
def send_text_mess(*args, **kwargs):
    try:
        body = {
                   #"touser": kwargs['touser'],
                   "toparty": kwargs['toparty'],
                   "msgtype": "text",
                   "agentid": kwargs['agentid'],
                   "text": {
                       "content": kwargs['content'].encode('utf-8')
                   },
                   "safe":"0"
                }
        data = json.dumps(body, ensure_ascii=False)
        url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s' % kwargs['token']['access_token']
        #request = urllib2.Request()
        #response = urllib2.urlopen(request, data)
        #msg = response.read()
        
        ret = requests.post(url, data = data)
        msg = ret.json()
        return_code = 1
    except Exception, ex:
        msg = u'异常:' + str(ex)
        return_code = 0
    finally:
        writelog(url, msg)
        return return_code
    
class Chat():
    
    def __init__(self):
        self.url = "https://qyapi.weixin.qq.com/cgi-bin/chat/get?access_token=%s&chatid=%s"
        
    def create_chat(self, token_id):
        body = {
                   "chatid": "4325241991",
                   "name": "企业应用报警中心",
                   "owner": "admin",
                   "userlist": ["13716119736","admin","schangech"]
                }
        url = "https://qyapi.weixin.qq.com/cgi-bin/chat/create?access_token=%s" % (token_id)
        data = json.dumps(body, ensure_ascii=False)
        response = requests.post(url, data = data)
        msg = response.json()
        print msg
        
    def get_chat_msg(self, token_id, chatid=1):
        #url = self.url % (token_id, chatid)
        response = requests.post("https://qyapi.weixin.qq.com/cgi-bin/chat/get?access_token=%s&chatid=%s" % (token_id, chatid))
        msg = response.json()
        print msg
    

def writelog(url, msg):
    timenow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    f = open("D://wechat.log", "a")
    f.write(timenow + "    " + str(msg) + "  " + url  + "\n")
    f.close()
    
if __name__ == '__main__':
#     Token = GetToken()
#     token_id = Token.get_token()
#     print token_id
#     # 扩展，把token加入到cookie中，避免每次进行获取
#     send_mess_status = send_text_mess(token=token_id, toparty=2, agentid=4, content=u'临时消息发送接口')
#     if send_mess_status:
#         print("消息发送成功")
#     else:
#         print("消息发送失败")
    chat = Chat()
    token_id = {}
    token_id['access_token'] = "ozZlU5C0t_MgTjadlAZjPxlL-hdfV0qqpFH2WH5nbJfCcJXVvx1p2hdoEJh-mGRW"
    chat.create_chat(token_id['access_token'])
        
    
    
    