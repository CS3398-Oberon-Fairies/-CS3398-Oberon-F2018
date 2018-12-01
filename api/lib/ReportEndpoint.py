from flask import request
import json
from api.lib.BasicEndpoint import BasicEndpoint
from api.db.SocialInterface import SocialInterface
from api.db.ReportInterface import ReportInterface


class ReportEndpoint(BasicEndpoint):
    _report_connection = None

    # ==========================================================================
    def __init__(self, connection):
        BasicEndpoint.__init__(self, "ReportEndpoint", "/report/<action>")
        self._report_connection = ReportInterface(connection)

    # ==========================================================================
    def report(self, form):
        names, res = self._report_connection.createReport(form["lotName"], form["lot_status"], form["token"])
        if not names: return json.dumps({
            "status": "error",
            "action": "report",
            "message": res
        })
        return json.dumps({
            "status": "success",
            "action": "report",
            "message": res
        })

    # ==========================================================================
    def checkStatus(self, form):
        names, res = self._report_connection.checkLotStatus(form["lotName"])
        if not names: return json.dumps({
            "status": "error",
            "action": "checkStatus",
            "message": res
        })
        return json.dumps({
            "status": "success",
            "action": "checkStatus",
            "message": res
        })
    
    # ==========================================================================
    def getRecentReportTime(self, form):
        names, res = self._report_connection.getLatestReportTime(form["lotName"])
        if not names: return json.dumps({
            "status": "error",
            "action": "getRecentReportTime",
            "message": res
        })
        return json.dumps({
            "status": "success",
            "action": "getRecentReportTime",
            "message": res
        })
    
    # ==========================================================================
    def post(self, params, args):
        if args["action"] == "report":
            return self.report(params.form)
        elif args["action"] == "checkStatus":
            return self.checkStatus(params.form)
        elif args["action"] == "getRecentReportTime":
            return self.getRecentReportTime(params.form)
        
