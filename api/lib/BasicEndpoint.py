
from flask import request
import json

class BasicEndpoint:

	_endpoint_name = ""
	_endpoint_path = ""

	# ==========================================================================
	def __init__(self, endpoint_name, endpoint_path):

		self._endpoint_name = endpoint_name
		self._endpoint_path = endpoint_path
		print("[LOG]", self._endpoint_name, "(" + self._endpoint_path + ")", "initialized.")

	# ==========================================================================
	def catch(self, **args):

		r = request
		if r.method == "GET": return self.get(r, args)
		elif r.method == "POST": return self.post(r, args)
		elif r.method == "DELETE": return self.delete(r, args)
		elif r.method == "PUT": return self.put(r, args)
		else: return self.createError("error", "Not a valid request type.")

	# ==========================================================================
	def createError(self, etype, message):

		return json.dumps({"type":etype, "message":message})

	# ==========================================================================
	def get(self, params, args):

		return self.createError("error", "GET '" + self._endpoint_path + "' not defined.")

	# ==========================================================================
	def post(self, params, args):

		return self.createError("error", "POST '" + self._endpoint_path + "' not defined.")

	# ==========================================================================
	def delete(self, params, args):

		return self.createError("error", "DELETE '" + self._endpoint_path + "' not defined.")
		
	# ==========================================================================
	def put(self,params, args):

		return self.createError("error", "PUT '" + self._endpoint_path + "' not defined.")
