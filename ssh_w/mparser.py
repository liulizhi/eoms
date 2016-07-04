#!/usr/bin/python
#encoding:utf-8


class Parser(object):

    parser_results = {}
    
    def __init__(self, cmd):
        self.cmd = cmd

    def parse(self):
        print "开始解析结果"
        for key, value in self.cmd.results.items():
            print "\t", key, value
            self.parser_results["parser %s" % key] = value
        print "结束解析结果"
        return self.parser_results

