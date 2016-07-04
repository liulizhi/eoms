#!/usr/bin/python 
#encoding:utf-8

import sys
import os.path

mp = os.path.join(os.path.dirname(os.path.abspath(__file__)), "module")
sys.path.append(mp)

import ssh_agent
import command
import mparser 
import store

def main():
    
    # 主机名  ip 序列号
    ipall_dict = {}
    
    for x in xrange(1, 2):
        ip_msg = []
        
        ip = "10.10.10.%d" % x
    
        # 获取连接对象
        agent = ssh_agent.SSHAgent().ssh(ip)

        # 执行相关的命令, 定义好的命令
        cmd = command.Command(agent)
        results = cmd.load()
        print "#######################"
        print results
        print "#######################"
    
        # 执行解析, 注意每个命令的结果不一样，需要不同的解析方式
        ps = mparser.Parser(cmd)
        res_parse = ps.parse()
        print "#######################"
        print res_parse
        print "#######################"
        
        # 存储结果，可以是文本，数据库，其他
        st = store.Store(ps)

        st.store()
    

if __name__ == "__main__":
    main()




