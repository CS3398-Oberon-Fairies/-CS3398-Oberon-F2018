
import unittest
import json

from lib.PingEndpoint import PingEndpoint
from lib.SearchLatLon import SearchLatLon
from lib.SearchQuery import SearchQuery

class TestEndpoints(unittest.TestCase):

	# ==========================================================================
	def test_basic(self):

		pe = PingEndpoint()
		self.assertEqual(pe.get({}, {}), json.dumps({
			"status":200,
			"info":"https://github.com/CS3398-Oberon-Fairies/CS3398-Oberon-F2018/api/",
			"version":"0.1"
		}))


if __name__ == '__main__':
    unittest.main()