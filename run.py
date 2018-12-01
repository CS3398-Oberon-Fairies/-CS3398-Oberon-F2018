
from api.main import BasicAPI
from api.lib.PingEndpoint import PingEndpoint
from api.lib.SearchLatLon import SearchLatLon
from api.lib.SearchQuery import SearchQuery
from api.db.BasicConnection import BasicConnection
from api.lib.SocialEndpoint import SocialEndpoint
from api.lib.ReportEndpoint import ReportEndpoint

################################################################################
CONN = BasicConnection("id7697898_app", "connect", "databases.000webhost.com", "pp")

################################################################################
def main(argv):
        api = BasicAPI()
        api.addEndpoint(PingEndpoint())
        api.addEndpoint(SearchLatLon(CONN))
        api.addEndpoint(SearchQuery(CONN))
        api.addEndpoint(SocialEndpoint(CONN), methods=["POST"])
        api.addEndpoint(ReportEndpoint(CONN), methods=["POST"])
        api.runServer(debug=True)

main(sys.argv[1:])
