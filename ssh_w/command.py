#!/usr/bin/python
#encoding:utf-8



class Command(object):

    cmds = ["hostname", "ip -a", "ls /home", "ps aux | wc -l"]
    results = {}
    
    def __init__(self, agent):
        self.agent = agent # ssh-agent 对象

    def load(self):
        '''执行一序列的命令'''
        print "开始执行命令" 
        for cmd in self.cmds:
            print "\t", cmd
            res = self.agent.execute(cmd)
            self.results[cmd] = res
        print "结束执行命令" 
        return self.results
