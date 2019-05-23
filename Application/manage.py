# -*- coding: utf-8 -*-

# Application developed by @DevilPaper
# telegram: https://t.me/paper_devil
# mail: ketov-x@yandex.ru / ketov-x@inbox.ru

from source.application import create_app

# create_app( confname )
# confname: a)development
#			b)testing
#			c)production
app = create_app('default')
# При развёртывание не указывать явно
# имя конфига, а указать переменную
# окружения.

if __name__ == '__main__':
	app.run()