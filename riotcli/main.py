
from cement import App, TestApp, init_defaults
from cement.core.exc import CaughtSignal
from .core.exc import RiotCliError
from .controllers.base import Base

# configuration defaults
CONFIG = init_defaults('todo')
CONFIG['todo']['foo'] = 'bar'


class RiotCli(App):
    """RIOT CLI primary application."""

    class Meta:
        label = 'riotcli'

        # configuration defaults
        config_defaults = CONFIG

        # call sys.exit() on close
        close_on_exit = True

        # load additional framework extensions
        extensions = [
            'yaml',
            'colorlog',
            'jinja2',
        ]

        # configuration handler
        config_handler = 'yaml'

        # configuration file suffix
        config_file_suffix = '.yml'

        # set the log handler
        log_handler = 'colorlog'

        # set the output handler
        output_handler = 'jinja2'

        # register handlers
        handlers = [
            Base
        ]


class RiotCliTest(TestApp,RiotCli):
    """A sub-class of RiotCli that is better suited for testing."""

    class Meta:
        label = 'riotcli'


def main():
    with RiotCli() as app:
        try:
            app.run()

        except AssertionError as e:
            print('AssertionError > %s' % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except RiotCliError:
            print('RiotCliError > %s' % e.args[0])
            app.exit_code = 1

            if app.debug is True:
                import traceback
                traceback.print_exc()

        except CaughtSignal as e:
            # Default Cement signals are SIGINT and SIGTERM, exit 0 (non-error)
            print('\n%s' % e)
            app.exit_code = 0


if __name__ == '__main__':
    main()
