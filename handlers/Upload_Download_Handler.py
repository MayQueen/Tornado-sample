# coding=utf-8

import os
import sys

import tornado.web
import tornado.gen

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
