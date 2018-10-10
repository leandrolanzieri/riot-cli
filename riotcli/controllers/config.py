from cement import Controller, ex
from ..core.riot_config.riot_config import RiotConfig

class Config(Controller):
    default_config_file = 'riot.yaml'

    class Meta:
        label = 'config'
        stacked_type = 'nested'
        help = 'handle riot configuration'

    @ex(help='list configurable parameters',
        arguments=[
            ( ['-v', '--verbose'],
              {'help': 'prints detailed list',
               'action': 'store_true'} )
        ]
    )
    def list(self):
        data = {}
        configuration = RiotConfig.parse_config(self.default_config_file)
        data['parameters'] = configuration['configuration']
        data['verbose'] = self.app.pargs.verbose
        self.app.render(data, 'config/list.jinja2')
