
from api.lib.BasicEndpoint import BasicEndpoint
import json
from api.db.SearchInterface import SearchInterface

class SearchLatLon(BasicEndpoint):

	# ==========================================================================
	def __init__(self, connection):
		BasicEndpoint.__init__(self, "SearchLatLon", "/location/search/<latitude>,<longitude>")
		self._search_connection = SearchInterface(connection)

	# ==========================================================================
	def get(self, params, args):

		# set parameter if given;
		radius = 10
		if "radius" in params.args:
			if int(params.args["radius"]) < 1 or int(params.args["radius"]) > 50:
				return self.createError("error", "Radius not in valid range.")
			radius = params.args["radius"]

		names, res = self._search_connection.getSearchResultsByLatLng(
			args["latitude"],
			args["longitude"],
			radius
		)

		resp = {
			"status":200,
			"lat": args["latitude"],
			"lon": args["longitude"],
			"radius": radius,
			"alias": names,
			"result": res
		}

		# TODO: call DB to get results

		return json.dumps(resp)
