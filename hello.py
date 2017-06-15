import web

urls = ( '/(.*)', 'hello' )

class hello:
    def GET(self, name):
        if not name:
            name = 'world'
        return 'hello ' + name + '!'

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()





