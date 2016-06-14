#-*- coding:utf-8 -*-
'''
Created on 2016-6-8

@author: QiRui.Su schangech@gmail.com
'''

import json
import urllib2
from urllib2 import URLError

class Zabbix_Auth:
    
    def __init__(self):
        self.url = 'http://zabbix.light.fang.com/api_jsonrpc.php'
        self.header = {"Content-Type":"application/json"}


    def user_login(self):
        data = json.dumps({
                           "jsonrpc": "2.0",
                           "method": "user.authenticate",
                           "params": {
                                      "user": "admin",
                                      "password": "SouFun.ComZabbix"
                                      },
                           "id": 0
                           })

        request = urllib2.Request(self.url, data)
        for key in self.header:
            request.add_header(key, self.header[key])

        try:
            result = urllib2.urlopen(request)
        except URLError as e:
            print "\033[041m authenticate is failed, please check it !\033[0m", e.code
        else:
            response = json.loads(result.read())
            result.close()
            self.authID = response['result']
            return self.authID
        
