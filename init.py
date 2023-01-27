from main import *
from pprint import pprint

service1 = [("GET", "/api/v1/cluster/metrics"),
                ("POST", "/api/v1/cluster/{cluster}/plugins"),
                ("POST", "/api/v1/cluster/{cluster}/plugins/{plugin}")]

service2 = [("GET", "/api/v1/cluster/freenodes/list"),
                ("GET", "/api/v1/cluster/nodes"),
                ("POST", "/api/v1/cluster/{cluster}/plugins/{plugin}"),
                ("POST", "/api/v1/cluster/{cluster}/plugins")]

app=app_parce()

out=app.parce(service1)
pprint(json.loads(out))

out=app.parce(service2)
pprint(json.loads(out))
