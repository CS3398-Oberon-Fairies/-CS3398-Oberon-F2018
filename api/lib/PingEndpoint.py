
from flask import request
import json
from lib.BasicEndpoint import BasicEndpoint

class PingEndpoint(BasicEndpoint):

	# ==========================================================================
	def __init__(self):

		BasicEndpoint.__init__(self, "Root", "/ping/<name>")

	# ==========================================================================
	def get(self, params, args):

		resp = {
			"status":200,
			"info":"https://github.com/CS3398-Oberon-Fairies/CS3398-Oberon-F2018/api/",
			"version":"0.1"
		}

		if "name" in args: resp["hello"] = args["name"]

		return json.dumps(resp)
