"""
应用程序是存在于包中的。 
在Python中，包含__init__.py文件的子目录被视为一个可导入的包。 
当你导入一个包时，__init__.py会执行并定义这个包暴露给外界的属性。
"""
from flask import Flask

app = Flask(__name__)

from app import routes  # 导入放在底部可以避免由于这两个文件之间的相互引用而导致的错误



