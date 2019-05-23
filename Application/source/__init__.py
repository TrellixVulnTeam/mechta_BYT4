import sys
from flask import Blueprint

sys.path.insert(0, sys.path[0])

# Основные страницы сайта. 
# Расположение index страницы и её ошибок.
# Следовательно смотреть source/blueprints/main

main = Blueprint('main', __name__)
from source.blueprints.main import views, errors