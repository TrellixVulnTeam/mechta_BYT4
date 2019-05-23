from flask import Flask, render_template
from source.config import config

def create_app(confname):
	''' Flask Instance Creation Factory
		Фабрика создания экземпляра приложения  '''

	app = Flask(__name__) # creation an exemplar
	app.config.from_object(config[confname]) # Config setting from
	config[confname].init_app(app)			 # passed argument confname

	# initialization of additional extensions
	# db.init_app(app)
	# mail.init_app(app)

	# blueprints initialization
	from source import main as main
	app.register_blueprint(main)
	
	return app