from jinja2 import Environment, FileSystemLoader

def application(environ, start_response):
    jinja2_env = Environment(loader=FileSystemLoader('./templates', encoding='utf8'))
    template = jinja2_env.get_template('hello.html')
    html = template.render()

    start_response('200 OK', [('Content-Type', 'text/html')])
    return [html.encode('utf-8')]
