import os
import sys

import tornado
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options

from tornado.options import define, options

from url import handlers

# 添加默认配置信息
define("port", default=8000, help= "run on the given port", type = int) # 默认启动配置


class Application(tornado.web.Application):
    def __init__(self):
        # 配置文件路径
        settings = dict(
            debug =True,
            static_path = os.path.join(os.path.dirname(__file__), "static"),
            template_path = os.path.join(os.path.dirname(__file__), "templates"),
        )
        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ =="__main__":
   
    port =8000 # 默认启动端口
    tornado.options.parse_command_line()

    app = Application()
    http_server = tornado.httpserver.HTTPServer(app, xheaders=True)
    http_server.listen(options.port)

    try:
        print("*"*5 + "APP启动" + "*"*5)
        print("Listen on http://localhost:{0}".format(port))
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        print("\n" + "*"*5 + "APP停止" + "*"*5)
        tornado.ioloop.IOLoop.instance().stop()

