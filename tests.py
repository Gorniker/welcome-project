import unittest
from main import *

#Данные для первых запусков
service1 = [("GET", "/api/v1/cluster/metrics"),
                ("POST", "/api/v1/cluster/{cluster}/plugins"),
                ("POST", "/api/v1/cluster/{cluster}/plugins/{plugin}")]

#Данные для второго запуска
service2 = [("GET", "/api/v1/cluster/freenodes/list"),
                ("GET", "/api/v1/cluster/nodes"),
                ("POST", "/api/v1/cluster/{cluster}/plugins/{plugin}"),
                ("POST", "/api/v1/cluster/{cluster}/plugins")]

#Данные для второго запуска с повторением
service3 = [("GET", "/api/v1/cluster/freenodes/list"),
                ("GET", "/api/v1/cluster/nodes"),
                ("POST", "/api/v1/cluster/{cluster}/plugins/{plugin}"),
                ("POST", "/api/v1/cluster/{cluster}/plugins"),
                ("GET", "/api/v1/cluster/metrics")]

#Данные для второго запуска с пересечением
service4 = [("GET", "/api/v1/cluster/freenodes/list"),
                ("GET", "/api/v1/cluster/nodes"),
                ("POST", "/api/v1/cluster/{cluster}/plugins/{plugin}"),
                ("POST", "/api/v1/cluster/{cluster}/plugins"),
                ("POST", "/api/v1/cluster/metrics")]

#Данные для второго запуска с неправильным path
service5 = [("GET", "/app/v1/cluster/freenodes/list"),
                ("GET", "/api/v1/cluster/nodes"),
                ("POST", "/api/v1/cluster/{cluster}/plugins/{plugin}"),
                ("POST", "/api/v1/cluster/{cluster}/plugins")]

class TestsCase(unittest.TestCase):

    def test_simple_case(self):
        app=app_parce()
        out=app.parce(service1)
        out=app.parce(service2)
        out=json.loads(out)

    def test_repeat_case(self):
        app=app_parce()
        out=app.parce(service1)
        out=app.parce(service3)

    def test_intersection(self):
        app=app_parce()
        out=app.parce(service1)
        out=app.parce(service4)

    def test_wrong_pattern(self):
        app=app_parce()
        out=app.parce(service1)
        out=app.parce(service5)


unittest.main()
