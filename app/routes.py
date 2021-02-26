from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    # python字典模拟一个用户
    user = {'username':'Miguel'}
    return render_template('index.html', title='Home', user=user)
