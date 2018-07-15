import cgi
from jinja2 import Environment, FileSystemLoader

class MyWSGIApplication(object):
    def __call__(self, environ, start_response):
        if environ['REQUEST_METHOD'].upper() == "GET":
            jinja2_env = Environment(loader=FileSystemLoader('./templates', encoding='utf8'))
            template = jinja2_env.get_template('get.html')

            fs = cgi.FieldStorage(
                environ=environ,
                keep_blank_values=True,
            )
            html = template.render(title=fs['title'].value, comment=fs['comment'].value)

            start_response('200 OK', [('Content-Type', 'text/html')])
            return [html.encode('utf-8')]


app = MyWSGIApplication()
