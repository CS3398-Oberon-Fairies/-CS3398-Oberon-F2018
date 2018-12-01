
import sys

from api.main import BasicAPI
from api.lib.PingEndpoint import PingEndpoint
from api.lib.SearchLatLon import SearchLatLon
from api.lib.SearchQuery import SearchQuery
from api.db.BasicConnection import BasicConnection
from api.lib.SocialEndpoint import SocialEndpoint
from api.lib.ReportEndpoint import ReportEndpoint

################################################################################
CONN = BasicConnection("p_g149", "1Ae(8DaEe#5E0F9(", "db4free.net", "prioritypark")

################################################################################
def main(argv):
        api = BasicAPI()
        api.addEndpoint(PingEndpoint())
        api.addEndpoint(SearchLatLon(CONN))
        api.addEndpoint(SearchQuery(CONN))
        api.addEndpoint(SocialEndpoint(CONN), methods=["POST"])
        api.addEndpoint(ReportEndpoint(CONN), methods=["POST"])
        return api.runServer(debug=True)

main(sys.argv[1:]).run()
