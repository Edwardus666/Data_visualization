import os

from sanic import Sanic
from sanic.response import json
from sanic_jinja2 import SanicJinja2

_dir = os.path.dirname(os.path.dirname(__file__))
# 一定要 才能读取绝对路径, 如果是相对路径呢
app = Sanic('my_project')
app.static('/static', f'./static')
jinja = SanicJinja2(app, pkg_name='main', pkg_path='./templates')


@app.route('/')
async def index(request):
    # calc
    # 30s
    return jinja.render('index.html', request, my_title='Hello, sanic!')


# api
@app.route('/get_user_name')
async def get_user_name(request):
    return json({'name': 'Tom'})


# api
@app.route('/get_data')
async def get_data(request):
    # calc
    a = {
        'a': [],
        'd': [],
    }
    return json(a)


# api
@app.route('/get_data1')
async def get_data1(request):
    # calc
    a = {
        'a': [],
        'd': [],
    }
    return json(a)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000, debug=True, workers=1)
