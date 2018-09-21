
from lib.BasicEndpoint import BasicEndpoint
import json

class SearchLatLon(BasicEndpoint):

	# ==========================================================================
	def __init__(self):
		BasicEndpoint.__init__(self, "SearchLatLon", "/location/search/<latitude>,<longitude>")

	# ==========================================================================
	def get(self, params, args):

		# set parameter if given;
		radius = 10
		if "radius" in params.args:
			if int(params.args["radius"]) < 1 or int(params.args["radius"]) > 50:
				return self.createError("error", "Radius not in valid range.")
			radius = params.args["radius"]

		resp = {
			"status":200,
			"lat": args["latitude"],
			"lon": args["longitude"],
			"radius": radius
		}

		# TODO: call DB to get results

		return json.dumps(resp)
