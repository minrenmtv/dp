import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.template
import tornado.gen
import random
import time

class MainHandler(tornado.web.RequestHandler):
    def get(self):
	loader = tornado.template.Loader(".")
        self.write(loader.load("index.html").generate())

class WSHandler(tornado.websocket.WebSocketHandler):
    def open(self):
    	print 'Connection opened.'
    	self.write_message("Welcome to my websocket server.")
      
    @tornado.web.asynchronous
    @tornado.gen.engine
    def on_message(self, message):
        print message
        if message == "start":
            while True:
                msg = ""
                for y in range(0, 10):
                    status = random.randint(0,1)
                    msg += str(status)

                self.write_message(msg)
                print msg
                yield tornado.gen.Task(tornado.ioloop.IOLoop.instance().add_timeout, time.time() + 1)
                # time.sleep(2)


    def on_close(self):
      print 'Connection closed.'

application = tornado.web.Application([
    (r'/ws', WSHandler),
    (r"/", MainHandler),
    (r"/(.*)", tornado.web.StaticFileHandler, {"path": "./resources"}),
])

if __name__ == "__main__":
    application.listen(9090)
    tornado.ioloop.IOLoop.instance().start()
