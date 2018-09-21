
from flask import Flask
from lib.PingEndpoint import PingEndpoint
from lib.SearchLatLon import SearchLatLon
from lib.SearchQuery import SearchQuery
import sys

################################################################################
class BasicAPI:

	_endpoints = {}

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

	# ==========================================================================
	def runServer(self, host="127.0.0.1", debug=True):

		runs = self._app.run(debug=debug, host=host)

	# ==========================================================================
	def loadRoutes(self):

		# TODO: load routers from configuration
		return -1

	# ==========================================================================
	def __init__(self):

		self._app = Flask(__name__)
		self.loadRoutes()		

################################################################################
def main(argv):

	if argv[0] == "test":
		api = BasicAPI()
		api.addEndpoint(PingEndpoint())
		api.addEndpoint(SearchLatLon())
		api.addEndpoint(SearchQuery())
		api.runServer(debug=True)
	elif argv[0] == "run":
		api = BasicAPI()
		api.loadRoutes()
		api.runServer(debug=False)

main(sys.argv[1:])
