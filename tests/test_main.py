
from riotcli.main import RiotCliTest

def test_riotcli(tmp):
    with RiotCliTest() as app:
        res = app.run()
        print(res)
        raise Exception

def test_command1(tmp):
    argv = ['command1']
    with RiotCliTest(argv=argv) as app:
        app.run()
