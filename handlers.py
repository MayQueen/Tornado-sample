# coding=utf-8

import os
import sys

import tornado.web
import tornado.gen

class HelloworldHandlers(tornado.web.RequestHandler):
    def get(self):
        self.render("helloworld.html")