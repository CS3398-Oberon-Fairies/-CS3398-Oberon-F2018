
from flask import Flask
import sys

################################################################################
class BasicAPI:

	_endpoints = {}

	# ==========================================================================
	def __init__(self):

		# TODO: initialize DB connection
		self._app = Flask(__name__)
		self.loadRoutes()	

	# ==========================================================================
	def addEndpoint(self, endpoint_handler, methods=["GET"]):

		# add endpoint to API;
		self._endpoints[endpoint_handler._endpoint_path] = endpoint_handler
		# add endpoint route to flask;
		self._app.add_url_rule(
			endpoint_handler._endpoint_path,
			endpoint_handler._endpoint_name,
			endpoint_handler.catch,
			methods=methods
		)
		self._app.after_request(self.fixRequest)

	# ==========================================================================
	def fixRequest(self, response):
		
	    response.headers["Access-Control-Allow-Origin"] = "*"
	    response.mimetype="application/json"
	    return response

	# ==========================================================================
	def runServer(self, host="127.0.0.1", debug=True):

		runs = self._app.run(debug=debug, host=host)

	# ==========================================================================
	def loadRoutes(self):

		# TODO: load routers from configuration
		return -1	
