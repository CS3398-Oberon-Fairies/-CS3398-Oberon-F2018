
from flask import request
import json
from lib.BasicEndpoint import BasicEndpoint
from db.SocialInterface import SocialInterface

class SocialEndpoint(BasicEndpoint):

	_search_connection = None

	# ==========================================================================
	def __init__(self, connection):
		BasicEndpoint.__init__(self, "SocialEndpoint", "/social/<action>")
		self._search_connection = SocialInterface(connection)

	# ==========================================================================
	def register(self, form):
		return json.dumps({})

	# ==========================================================================
	def login(self, form):
		return json.dumps({})

	# ==========================================================================
	def post(self, params, args):
		if args["action"] == "register": return self.register(params.form)
		elif args["action"] == "login": return self.login(params.form)		
