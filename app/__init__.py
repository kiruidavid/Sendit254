from flask import Flask, Blueprint

from app.api.v1 import version1



def create_app():
	app=Flask(__name__) 
	app.url_map.strict_slashes=False
	app.config["ERROR_404_HELP"]=False
	app.register_blueprint(version1)
	return app
