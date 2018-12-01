
from api.lib.BasicEndpoint import BasicEndpoint
import json
from api.db.SearchInterface import SearchInterface
from urllib.parse import unquote

class SearchQuery(BasicEndpoint):

	_search_connection = None

	# ==========================================================================
	def __init__(self, connection):
		BasicEndpoint.__init__(self, "SearchQuery", "/location/search/<query>")
		self._search_connection = SearchInterface(connection)

	# ==========================================================================
	def get(self, params, args):

		# set parameter if given;
		radius = 10
		if "radius" in params.args:
			if int(params.args["radius"]) < 1 or int(params.args["radius"]) > 50:
				return self.createError("error", "Radius not in valid range.")
			radius = params.args["radius"]

		# get the actual query;
		args["query"] = unquote(args["query"])
		# and get DB result;
		names, res, osm = self._search_connection.getSearchResultsByQuery(args["query"], radius)

		resp = {
			"status":200,
			"query": args["query"],
			"radius": radius,
			"alias": names,
			"result": res,
			"osm": {
				"Name": osm["display_name"],
				"Latitude": osm["lat"],
				"Latitude": osm["lon"],
				"osm_id": osm["osm_id"]
			}
		}

		# TODO: call DB to get results

		return json.dumps(resp)
