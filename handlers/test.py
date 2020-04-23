# coding=utf-8

import os
import sys

import tornado.web
import tornado.gen

import sqlite3 

# 建立数据库连接
def get_conn():
    return sqlite3.connect("tornado.db3") # 建立与“tornado.db3”数据库的连接，若数据库不存在，则立即新建
# print("opened databases successfully")

# Helloworld  请求处理
class HelloworldHandlers(tornado.web.RequestHandler):
    def get(self):
        self.render("helloworld.html")

# 主页
class IndexHandlers(tornado.web.RequestHandler):
    def get(self):
        self.render("index/index.html")

# 登录
class LoginHandlers(tornado.web.RequestHandler):
    def get(self):
        uname = self.get_argument('uname')
        pwd = self.get_argument('pwd')
        # print(uname, pwd)
        self.write(uname + ',' + pwd)

# 通过user-agent判断是否是正常访问
uas = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'] # user-agent
class AccessHandlers(tornado.web.RequestHandler):
    def get(self):
        ua =self.request.headers['User-Agent']
        # 如果访问该地址的不是uas中的浏览器，直接给出403:禁止访问
        if ua not in uas:
            self.send_error(403) 
        else:
            self.render("helloworld.html")

# 通过记录IP次数来判断是否是正常访问
ipcount = {}
class IPAccess(tornado.web.RequestHandler):
    def get(self):
        ip = self.request.remote_ip
        print(ip)

        num = ipcount.get(ip,0) + 1
        ipcount[ip] = num

        if ipcount[ip] > 5:
            self.send_error(403)
        else:
           self.write('正常访问')

# 注册
class RegisterHadnlers(tornado.web.RequestHandler):
    def initialize(self,conn):
        self.conn = conn

    def get(self):
        self.render("login.html")
    
    def post(self):
        # 获取请求参数
        uname = self.get_argument('uname')
        pwd = self.get_argument('pwd')
        print(uname,pwd)
        try:
            cursor = self.conn.cursor()
            print(cursor)
            cursor.execute("INSERT INTO user (uname, pwd,datetime) VALUES ('%s','%s',datetime())" % (uname, pwd)) # 将获取到的用户名、密码和注册日期写入数据库
            self.conn.commit()
            print ("插入成功")
            self.conn.close()
        except:
            self.conn.rollback()
            print ("插入失败")

# 文件上传与保存
class UploadHandlers(tornado.web.RequestHandler):
    def get(self):
        self.render('upload.html')

    def post(self):
        img1 = self.request.files['img1']
        # print (img1) 输出上传的图片

        for img in img1:
            body = img.get('body', '')
            # content_type = img.get('content_type', '')
            filename = img.get('filename', '')
            # print(content_type)
            # print(filename)
        
        # 设置图片储存路径
        files_dir = os.path.join(os.getcwd(), 'files', filename)

        # 将文件储存至本地
        with open(files_dir, 'wb') as fw:
            fw.write(body)

