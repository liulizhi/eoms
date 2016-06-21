#-*- coding:utf-8 -*-
'''
Created on 2016/6/14
@author: QiRui.Su schangech@gmail.com
'''

import os
import time
import shutil 

def read_file(path):
    #读取文件，如果文件不存在，则提示 文件不存在，请检查
    # 判断是否存在【目录或者文件】
    # res = os.path.exists(path)
    # 判断文件是否存在 
    # res = os.path.isfile(path)
    name = "D://testfilepy"
    try:
        res = os.makedirs(name, 0777)
    except Exception as e:
        print e
        res = False
    return res


def backup_file(source_file, backup_dir):
    #文件存在，先备份文件，在进行其它操作
    check_dir = os.path.exists(backup_dir)
    if not check_dir:
        try:
            res = os.makedirs(backup_dir, 0777)
        except Exception as e:
            res = False
            return e
    if res:
        bk_file = backup_dir + os.sep + time.strftime('%Y%m%d%H%M')
        targ_dir = bk_file + os.sep + source_file
        shutil.copy(source_file, targ_dir)
        check_backup = os.path.isfile(targ_dir)
        return check_backup      
    
    

def update_file(source_file, targ):
    #更新、修改文件
    #  判断修改文件数是否在可接受范围内，超过范围，则提示超过范围，不允许操作
    if targ:
        f = file(source_file, 'r')
        for line in f.readlines():
            pass
    

def rollback_file():
    #异常，则回滚，回滚之后，检查
    pass



if __name__ == '__main__':
    path = "D://config.ini"
    print read_file(path)