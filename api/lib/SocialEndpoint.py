
from flask import request
import json
from lib.BasicEndpoint import BasicEndpoint
from db.SocialInterface import SocialInterface

class SocialEndpoint(BasicEndpoint):

	_social_connection = None

	# ==========================================================================
	def __init__(self, connection):
		BasicEndpoint.__init__(self, "SocialEndpoint", "/social/<action>")
		self._social_connection = SocialInterface(connection)

	# ==========================================================================
	def register(self, form):
		names, res = self._social_connection.createUser(form["email"], form["password"])
		if not names: return json.dumps({
				"status":"error",
				"action": "register",
				"message": res
			})
		return json.dumps({
			"status":"success",
			"action": "register",
			"message": res
		})

	# ==========================================================================
	def login(self, form):
		names, res = self._social_connection.loginUser(form["email"], form["password"])
		if not names: return json.dumps({
				"status":"error",
				"action": "login",
				"message": res
			})
		return json.dumps({
			"status":"success",
			"action": "login",
			"token": res
		})

	# ==========================================================================
	def post(self, params, args):
		if args["action"] == "register": return self.register(params.form)
		elif args["action"] == "login": return self.login(params.form)		
