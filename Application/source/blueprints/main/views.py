# -*- coding: utf-8 -*-

from flask import render_template
from source import main # Основной блюпринт

# Метод index. Главная страница сайта.
@main.route('/', methods=['GET', 'POST'])
@main.route('/index', methods=['GET', 'POST'])
def index():
	return render_template('main/index.html')
#