#placeholder for flask game functions


from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

endpoint = Blueprint('endpoint', __name__,
                        template_folder='templates')

@endpoint.route('/endpoint')
def index():
	return "this is a test endpoing"
 


