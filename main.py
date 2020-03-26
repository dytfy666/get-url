#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import os
import sys
import re

os.system('chcp 65001')  # 防止控制台乱码


# 获取当前exe的路径


def app_path():
    """return exe dir"""
    if hasattr(sys, 'frozen'):  # 判断sys是否含有frozen.exe属性
        return sys._MEIPASS + r'\fc'
    else:
        return os.path.dirname(__file__) + r'\fc'


def file_name(file_paths):
    file_paths = app_path()
    for root, dirs, files in os.walk(app_path()):
        print(root)  # 当前目录路径
        print(dirs)  # 当前路径下所有子目录
        print(files)  # 当前路径下所有非目录子文件


# 定义循环获取路径函数并传入（path,L）参数，还需调用
Lall = []


def findpths(pathss):
    for file in os.listdir(pathss):
        file_path = os.path.join(pathss, file)
        if os.path.isdir(file_path):
            findpths(file_path)
        elif os.path.isfile(file_path) and file.endswith('.py'):  # endswith(.py)  判断以.py 结尾
            Lall.append(file_path)
    return Lall


# 获取一个新的显示列表外加序号,
def new_list(listname):
    list3 = [str(i) for i in listname]
    str2 = ''.join(list3)
    list2 = re.findall(r'\\(\w+?).py', str2)
    for i in range(len(list2)):
        t = str(i + 1) + '.'
        print(t + list2[i], end='\000\000')


'''
# 定义获取路径函数并传入（path,L）参数，还需调用
def listdir(paths):  # 传入储存的list
    path = paths
    dirname = findpths(path)
    return dirname
'''


def choose_live(ridd):
    path = app_path()
    if ridd == 123456788:
        return '这个真没有'
    else:
        t = L[ridd]
        command = 'python %s' % (t)
        result = os.system(command)
        return result



L = findpths(app_path())
#print(L)
list1 = new_list(Lall)
ridd = eval(input('\n\n请输入直播平台ID\n')) - 1
ru = choose_live(ridd)
print(ru)
# print(rid)
# print(L[rid])
# print(t)
# 'python %s' %(t)


"""
def file_name(file_dir):   
    L=[]   
    for root, dirs, files in os.walk(file_dir):  
        for file in files:  
            if os.path.splitext(file)[1] == '.jpeg':    #通过splitetext函数，以.分割文件名对比后缀
               L.append(os.path.join(root, file))  
    return L 
"""
