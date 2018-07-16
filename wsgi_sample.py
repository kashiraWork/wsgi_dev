from jinja2 import Environment, FileSystemLoader                                                                                                                          

class MyWSGIApplication(object):
    def __call__(self, environ, start_response):
        jinja2_env = Environment(loader=FileSystemLoader('./templates', encoding='utf8'))
        template = jinja2_env.get_template('index.html')
        html = template.render()

        start_response('200 OK', [('Content-Type', 'text/html')])
        return [html.encode('utf-8')]


app = MyWSGIApplication()


from wsgiref import simple_server

application = MyWSGIApplication()


if __name__ == '__main__':

    srv = simple_server.make_server('', 8888, application)

    srv.serve_forever()

