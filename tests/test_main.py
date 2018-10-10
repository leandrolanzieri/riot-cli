
from riotcli.main import RiotCliTest

def test_riotcli(tmp):
    with RiotCliTest() as app:
        res = app.run()
        print(res)

def test_config(tmp):
    argv = ['config']
    with RiotCliTest(argv=argv) as app:
        app.run()
