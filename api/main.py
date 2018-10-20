
from flask import Flask
from lib.PingEndpoint import PingEndpoint
from lib.SocialEndpoint import SocialEndpoint
from lib.SearchLatLon import SearchLatLon
from lib.SearchQuery import SearchQuery
from db.BasicConnection import BasicConnection
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

	# ==========================================================================
	def runServer(self, host="127.0.0.1", debug=True):

		runs = self._app.run(debug=debug, host=host)

	# ==========================================================================
	def loadRoutes(self):

		# TODO: load routers from configuration
		return -1	

################################################################################
try:
	CONN = BasicConnection("root", "m4p8v3p7g6", "127.0.0.1", "pp")
except:
	print("[ERROR] Could not establish DB connection.")
	exit(1)

def main(argv):

	if argv[0] == "test":
		api = BasicAPI()
		api.addEndpoint(PingEndpoint())
		api.addEndpoint(SocialEndpoint(CONN), methods=["POST"])
		api.addEndpoint(SearchLatLon(CONN))
		api.addEndpoint(SearchQuery(CONN))
		api.runServer(debug=True)
	elif argv[0] == "run":
		api = BasicAPI()
		api.loadRoutes()
		api.runServer(debug=False)

main(sys.argv[1:])
