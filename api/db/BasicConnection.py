
import mysql.connector

class BasicConnection:

	_conn = None

	# ==========================================================================
	def __init__(self, username, password, host, db):
		self._conn = mysql.connector.connect(
			user=username,
			password=password,
			host=host,
			database=db
		)

	# ==========================================================================
	def getResult(self, query):
		cur = self._conn.cursor()
		cur.execute(query)
		return [it[0] for it in cur.description], list(cur)

	# ==========================================================================
	def execute(self, query):
		cur = self._conn.cursor()
		cur.execute(query)
		self._conn.commit()
