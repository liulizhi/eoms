#!/usr/bin/python
#encoding:utf-8




class SSHAgent(object):

    def ssh(self, ip):
        '''ssh ip '''
        # 连接相关的机器，根据ip
        print "连接到ip机器啦%s" % ip
        return self

    def execute(self, cmd):
        # 在这个连接对象里面执行cmd, 相当在连接上的机器上执行命令
        # execute
        return "doing execute cmd %s" % cmd
