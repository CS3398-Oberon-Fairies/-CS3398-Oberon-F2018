import mysql.connector
import urllib.request
import json
import hashlib
import uuid
from db.SocialInterface import SocialInterface

class ReportInterface:

    _conn = None
    _conn2 = None

    # ==========================================================================
    def __init__(self, connection):
        self._conn = connection
        self._conn2 = SocialInterface(connection)

    # ==========================================================================
    def getparkingLotID(self, lotName):
        db_query = "SELECT * FROM parkinglot WHERE LotName='"+lotName+"'";
        names, values = self._conn.getResult(db_query)
        return values[0][0]

    def getparkingLot(self, lot_name):
        db_query = "SELECT * FROM parkinglot WHERE LotName='"+lot_name+"'";
        return self._conn.getResult(db_query)

    def getparkingLotName(self, lotID):
        db_query = "SELECT * FROM parkinglot WHERE Lot_id='"+lotID+"'";
        names, values = self._conn.getResult(db_query)
        return values[0][1]

    # ==========================================================================
    def createReport(self, lotName, lot_status, token):
        names, sess = self._conn2.getSession(token)
        cols, lot_info = self.getparkingLot(lotName)
        if len(lot_info) == 0:
            return False, "Parking lot does not exist"
        userID = sess[0][1]
        lotID = lot_info[0][1]
        if len(sess) > 0:
            db_query = "INSERT INTO report (user_id ,report, lot_id) VALUES ('"+userID+"' , '"+lot_status+"','"+lotID+"')";
            self._conn.execute(db_query)
            return True, "New report added."
        else:
            return False, "User must be logged into a session to report."

    # ==========================================================================
    def checkLotStatus(self, lotName):
        labels, lot_info = self.getparkingLot(lotName)
        if len(lot_info) == 0:
            return False, "Parking lot does not exist"
        col, values = self.getparkingLotID(lotName)
        lotID = values[0][0]
        db_query = "SELECT * FROM report WHERE report='full' AND lot_id='"+lotID+"' AND TIMEDIFF(CURRENT_TIMESTAMP,timestamp) < TIMEDIFF(CURRENT_TIMESTAMP,CURRENT_TIMESTAMP-INTERVAL 1 HOUR) ORDER BY timestamp DESC";
        names, lots = self._conn.execute(db_query)
        if len(lots) > 3:
            return True, lotName + " is full"
        else:
            return False, lotName + " is not full"













