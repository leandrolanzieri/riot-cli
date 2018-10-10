from cement import Controller, ex, shell
import re
import json

class Utils(Controller):
    class Meta:
        label = 'utils'
        stacked_type = 'nested'
        help = 'convenience commands'

    @ex(help='list the supported boards by an application',
        arguments=[
            ( ['-j', '--json'],
              {'help':'outputs in JSON format',
               'action':'store_true'} )
        ])
    def supported_boards(self):
        info = self.get_app_build_info()
        
        if info == None:
            return

        output_json = self.app.pargs.json
        
        if output_json:
            print(json.dumps(info['supported_boards']))
        else:
            self.app.render(info, 'utils/supported_boards.jinja2')

    def get_app_build_info(self):
        out, err, code = shell.cmd('make info-build')

        if code != 0:
            self.app.log.error('No application found')
            return None

        raw = out.decode('utf-8')
        info = {}
        info['raw'] = raw
        info['app_name'] = re.search('APPLICATION:\s*([^\n\r]*)', raw). \
                           group(0).split(' ')[1]
        info['supported_boards'] = re.search('supported boards:\s*([^\n\r]*)', raw) \
                                   .group(0).split(':\n')[1].split(' ')
        return info