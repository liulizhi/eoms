#!/usr/bin/python
#encoding:utf-8




class Store(object):
    
    def __init__(self, parser):
        self.parser = parser

    def store(self):
        print "开始存储结果到相关介质"
        for key, value in self.parser.parser_results.items():
            print "storeing......", key," =====values:====", value
            #pass
        print "结束存储结果到相关介质"



