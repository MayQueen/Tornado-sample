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

# 主页
class IndexHandlers(tornado.web.RequestHandler):
    def get(self):
        self.render("index/index.html")

# 管理员登录
class AdminHandlers(tornado.web.RequestHandler):
    def get(self):
        self.render("admin/admin_login.html")

# 用户登录
class LoginHandlers(tornado.web.RequestHandler):
    def get(self):
        self.render("user/user_login.html")

# 用户注册
class RegisterHadnlers(tornado.web.RequestHandler):
    def initialize(self,conn):
        self.conn = conn

    def get(self):
        self.render("user/user_create.html")
    
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

# 用户密码找回
class PasswordResetHandlers(tornado.web.RequestHandler):
    def get(self):
        self.render("user/password_reset.html")