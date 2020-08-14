#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os,sys,io,importlib
sys.setrecursionlimit(10000000)
importlib.reload(sys)
final = []
#work为绝对路径，windos下"d:/ProgramH5Server/H5_server_lj/log"
#linux运行1：chmod a+x log.py  2：sed -i 's/\r$//' log.py 3：./log.py
work = "d:/ProgramH5Server/H5_server_lj/log"
for root,dirs,files in os.walk(work): 
    for file in files: 
        final.append(os.path.join(root,file))    

def writeline(file):
    filename = file
    log_dir = os.path.join(work, filename)
    with io.open(log_dir, 'r', encoding='utf-8') as f: 
        print(file)
        lines = f.readlines()
        error_line = []
        operate_line = []
        for line in lines:
            if 'Error' in line or 'ERROR' in line or 'Exception' in line or 'EXCEPTION' in line or './' in line :
                error_line.append(line)
            elif '---add' in line :
                operate_line.append(line)

    errorlogname = 'error.log'
    operatelogname = 'operate.log'
    resultwork = os.path.dirname(__file__)
    log_a = os.path.join(resultwork, errorlogname)
    log_b = os.path.join(resultwork, operatelogname)
    with io.open(log_a, 'a',encoding='utf-8') as result:
        result.write('日志文件错误:'+ file)
        for i in list(set(error_line)):
            result.write(i)
    with open(log_b, 'a', encoding='utf-8') as result:
        result.write('日志文件操作:'+ file)
        for i in list(set(operate_line)):
            result.write(i)

for file in final:
    writeline(file)

#定时
