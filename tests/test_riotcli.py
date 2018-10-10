
from pytest import raises
from riotcli.main import RiotCliTest

def test_riotcli():
    # test riotcli without any subcommands or arguments
    with RiotCliTest() as app:
        app.run()
        assert app.exit_code == 0


def test_riotcli_debug():
    # test that debug mode is functional
    argv = ['--debug']
    with RiotCliTest(argv=argv) as app:
        app.run()
        assert app.debug is True


def test_config():
    # test config without arguments
    argv = ['config']
    with RiotCliTest(argv=argv) as app:
        app.run()


    # test command1 with arguments
    argv = ['config', 'list']
    with RiotCliTest(argv=argv) as app:
        app.run()
        data,output = app.last_rendered
