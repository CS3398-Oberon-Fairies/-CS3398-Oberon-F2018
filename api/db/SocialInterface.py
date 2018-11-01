
import mysql.connector
import urllib.request
import json
import hashlib
import uuid

class SocialInterface:

	_conn = None

	# ==========================================================================
	def __init__(self, connection):
		self._conn = connection

	# ==========================================================================
	def encryptPassword(self, password):
		return hashlib.sha512(password.encode('utf-8')).hexdigest()

	# ==========================================================================
	def getUser(self, email):
		db_query = "SELECT * FROM users WHERE Username='"+email+"'";
		return self._conn.getResult(db_query)

	# ==========================================================================
	def getSession(self, token):
		db_query = "SELECT * FROM sessions s RIGHT JOIN users u ON (s.user_id=u.user_id) WHERE s.Token='"+token+"'";
		return self._conn.getResult(db_query)

	# ==========================================================================
	def createUser(self, email, password):
		names, values = self.getUser(email)
		if len(values) > 0: return False, "User exists already."
		db_query = "INSERT INTO users (Username, Password) VALUES ('"+email+"', '"+self.encryptPassword(password)+"')";
		self._conn.execute(db_query)
		return True, "New user added."

	# ==========================================================================
	def loginUser(self, email, password):
		names, values = self.getUser(email)
		print(values)
		if len(values) == 0: return False, "Wrong username or password."
		enc_password = self.encryptPassword(password)
		if values[0][2] != enc_password: return False, "Wrong username or password."
		token = str(uuid.uuid4())
		db_query = "INSERT INTO sessions (user_id, Token) VALUES ("+str(values[0][0])+", '"+token+"')";
		self._conn.execute(db_query)
		return True, token
