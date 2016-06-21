#-*- coding:utf-8 -*-
'''
Created on 2016/6/21

@author: QiRui.Su schangech@gmail.com
'''
import requests

class GetToken():
    
    def __init__(self):
        self.url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=wx053fd424ed53c149&corpsecret=B48uhBXv508i1Jpq65XEjswdKMycLbYoI2oW1SkkylehXhQGoY7sSiwyg-4rps3S"

    def get_token(self):
        r = requests.get(self.url)
        return r.json()
        

if __name__ == '__main__':
    Token = GetToken()
    print Token.get_token()