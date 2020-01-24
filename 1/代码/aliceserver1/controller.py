#coding:utf8
from jinja2 import Template
import os

def index():
    file = os.path.join('views','index.html')
    with open(file,'r') as f:
        html = f.read()
        #html = html.replace('{{title}}','文章标题').replace('{{content}}','文章内容')
    return html

def article():
    file = os.path.join('views','article.html')
    with open(file, 'r') as f:
        # print 'hello'
        html = f.read()
        html = html.decode('utf-8') #utf-8 -> unicode
        # print type(html)
        tpl = Template(html)
        articles = [
            {'title':u'文章1标题','content':u'文章内容1'},
            {'title':u'文章2标题','content':u'文章内容2'}
        ]
        html = tpl.render(title=u'文章标题',content=u'文章内容',articles=articles)
    print type(html)
    return html.encode('utf-8')