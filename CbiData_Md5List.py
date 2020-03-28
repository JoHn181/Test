#!/usr/bin/python 
#coding=utf-8 
import hashlib
import os
import csv

path=[]

def get_filemd5(file_path):
    md5=None
    if os.path.isfile(file_path):
        f=open(file_path,'rb')
        md5_obj=hashlib.md5()
        md5_obj.update(f.read())
        hash_code=md5_obj.hexdigest()
        f.close()
        md5=str(hash_code).lower()
    return md5

def get_path(file_path):
    tem_path=[0]*100
    if os.path.isfile(file_path):
        if os.path.splitext(file_path)[1]==".zip":
#          print(file_path)    用于调试
            path.append(file_path)
    if os.path.isdir(file_path):
        tem_list=os.listdir(file_path)
        a=0
        while a<len(tem_list):
            tem_path[a]=file_path+"\\"+tem_list[a]
            get_path(tem_path[a])  
            a+=1

            

if __name__=="__main__":
    print('当前路径:'+os.getcwd())
    print('程序运行中',end='',flush = True)
    get_path(os.getcwd())
    with open("md5.csv","w") as csvfile: 
        writer = csv.writer(csvfile)
        #先写入columns_name
        writer.writerow(['文件类型','站名','版本','文件名','MD5','路径'])
        tem_rel=[0,0,0,0,0,0]
        rel=[]
        a=0
        i=0
        while a<len(path):
            if path[a].find('联锁数据')!=-1:
                tem_rel[0]='联锁数据'    #type
                tem_rel[1]=os.path.basename(os.path.abspath(os.path.dirname(path[a])+os.path.sep+".."))    #站名
                tem_rel[2]=os.path.basename(os.path.dirname(path[a]))    #版本
                tem_rel[3]=os.path.basename(path[a])    #文件名
                tem_rel[4]=get_filemd5(path[a])    #md5
                tem_rel[5]=path[a]
                rel.append(tem_rel)
                writer.writerow(rel[i])
                print('>',end='',flush = True)
#                print(rel[i])
                i+=1
            if path[a].find('发布数据')!=-1:
                tem_rel[0]='发布数据'    #type
                if len(os.path.basename(os.path.abspath(os.path.dirname(path[a])+os.path.sep+"..")).split('_'))>2:
                    tem_rel[2]=os.path.basename(os.path.abspath(os.path.dirname(path[a])+os.path.sep+".."))    #站名
                    tem_rel[1]=os.path.basename(os.path.dirname(path[a]))    #版本
                else:
                    tem_rel[1]=os.path.basename(os.path.abspath(os.path.dirname(path[a])+os.path.sep+".."))    #站名
                    tem_rel[2]=os.path.basename(os.path.dirname(path[a]))    #版本
                tem_rel[3]=os.path.basename(path[a])    #文件名
                tem_rel[4]=get_filemd5(path[a])    #md5
                tem_rel[5]=path[a]
                rel.append(tem_rel)
                writer.writerow(rel[i])
                print('>',end='',flush = True)
#                print(rel[i])
                i+=1  
            if path[a].find('配置文件')!=-1:
                tem_rel[0]='配置文件'    #type
                if os.path.basename(os.path.abspath(os.path.dirname(path[a])+os.path.sep+"..")).find('.')!=-1:
                     tem_rel[2]=os.path.basename(os.path.abspath(os.path.dirname(path[a])+os.path.sep+".."))    #版本
                     tem_rel[1]=os.path.basename(os.path.dirname(path[a]))    #站名
                if os.path.basename(os.path.abspath(os.path.dirname(path[a])+os.path.sep+"..")).find('配置文件')!=-1:
                     tem_rel[2]=os.path.basename(os.path.splitext(path[a])[0])    #版本
                     tem_rel[1]=os.path.basename(os.path.dirname(path[a]))    #站名
                tem_rel[3]=os.path.basename(path[a])    #文件名
                tem_rel[4]=get_filemd5(path[a])    #md5
                tem_rel[5]=path[a]
                rel.append(tem_rel)
                writer.writerow(rel[i])
                print('>',end='',flush = True)
 #               print(rel[i]) 
                i+=1
            a+=1
    print('\n''md5.csv文件已生成! ')
    print('试用版本有情况联系62184!')
    input()

    
    
    
