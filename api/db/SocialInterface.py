
import mysql.connector
import urllib.request
import json

class SocialInterface:

	_conn = None

	# ==========================================================================
	def __init__(self, connection):
		self._conn = connection

	# ==========================================================================
	def getUser(self, email):
		return None, None, None

	# ==========================================================================
	def createUser(self, email, password):
		return None, None, None

	# ==========================================================================
	def loginUser(self, email, password):
		return None, None, None
