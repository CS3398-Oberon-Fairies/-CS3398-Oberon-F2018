
import mysql.connector
import urllib.request
import json

class SearchInterface:

	_conn = None

	# ==========================================================================
	def __init__(self, connection):
		self._conn = connection

	# ==========================================================================
	def get(self, url, retry=5):
		c = 0
		while True:
			if c >= retry: return False
			try: return json.loads(urllib.request.urlopen(url).read().decode("utf-8"))
			except:
				time.sleep(3)
				c += 1

	# ==========================================================================
	# TODO: implement nominatim caching
	def getSearchResultsByQuery(self, query, radius):
		elements = query.split(" ")
		if len(elements) > 10: elements = elements[0:10]
		db_query = "+".join(elements)
		req = "https://nominatim.openstreetmap.org/search?q="+db_query+"&format=json"
		req = self.get(req)
		names, res = self.getSearchResultsByLatLng(req[0]["lat"], req[0]["lon"], radius)
		return names, res, req[0]

	# ==========================================================================
	def getSearchResultsByLatLng(self, lat, lng, radius):
		db_query = "SELECT *, (6371 * acos(cos(radians("+lat+")) * cos(radians(Latitude) ) * cos(radians(Longitude) - radians("+lng+")) + sin(radians("+lat+")) * sin(radians(Latitude))) ) AS distance FROM parkinglot HAVING distance < "+str(radius)+" ORDER BY distance"
		return self._conn.getResult(db_query)
