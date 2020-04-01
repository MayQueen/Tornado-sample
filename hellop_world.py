import tornado
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options


from tornado.options import define, options

define("port", default=8000, help= "run on the given port", type = int)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello world")

application = tornado.web.Application([
    (r"/", MainHandler),
])

if __name__ =="__main__":
    port = 8000

    tornado.options.parse_command_line()

    http_server = tornado.httpserver.HTTPServer(application, xheaders = True)
    http_server.listen(options.port)

    try:
        print("*"*10 + "APP 启动" + "*"*10)
        print("Listen on http://localhost:{0}".format(port))
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        print("\n" + "*"*10 + "APP 停止" + "*"*10)
        tornado.ioloop.IOLoop.instance().stop()
