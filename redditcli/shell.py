"""
Command Line Interface for redditcli
"""

from __future__ import print_function

import argparse
import logging
import sys

from cliff import app
from cliff import commandmanager
import redditcli.commands.account
from redditcli.api import client

LOG = logging.getLogger(__name__)


class HelpAction(argparse.Action):
    """Custom help action.

    Provide a custom action so the -h and --help options
    to the main app will print a list of the commands.

    The commands are determined by checking the CommandManager
    instance, passed in as the "default" value for the action.

    """
    def __call__(self, parser, namespace, values, option_string=None):
        outputs = []
        max_len = 0
        app = self.default
        parser.print_help(app.stdout)
        app.stdout.write('\nCommands for API v2 :\n')

        for name, ep in sorted(app.command_manager):
            factory = ep.load()
            cmd = factory(self, None)
            one_liner = cmd.get_description().split('\n')[0]
            outputs.append((name, one_liner))
            max_len = max(len(name), max_len)

        for (name, one_liner) in outputs:
            app.stdout.write('  %s  %s\n' % (name.ljust(max_len), one_liner))

        sys.exit(0)


class RedditShell(app.App):

    log = logging.getLogger(__name__)

    def __init__(self):
        super(RedditShell, self).__init__(
            description='Testing', #__doc__.strip(),
            version='0.1',
            command_manager=commandmanager.CommandManager('reddit.cli'),
        )
        self.log.debug('Inside Init')
        self._set_shell_commands(self._get_commands())

    def configure_logging(self):
        log_lvl = logging.DEBUG if self.options.debug else logging.WARNING
        logging.basicConfig(
            format="%(levelname)s (%(module)s) %(message)s",
            level=log_lvl)
        logging.getLogger('iso8601').setLevel(logging.WARNING)
        if self.options.verbose_level <= 1:
            logging.getLogger('requests').setLevel(logging.WARNING)

    def initialize_app(self, argv):
        self.log.debug('Initializing App')
        self._clear_shell_commands()
        ver = '1.0'
        self._set_shell_commands(self._get_commands())
        self.client = client.Client(base_url='test',#elf.redditapi_url,
                                    auth_url='https://www.reddit.com/api/v1/access_token',
                                    username=self.username,
                                    password=self.password,
                                    client_id=self.client_id,
                                    client_secret=self.client_secret,
                                    user_agent=self.user_agent)

    def _set_shell_commands(self, cmds_dict):
        for k, v in cmds_dict.items():
            self.command_manager.add_command(k, v)
        self.log.debug('Inside set shell commands')

    def build_option_parser(self, description, version,
                            argparse_kwargs=None):
        argparse_kwargs = argparse_kwargs or {}
        parser = argparse.ArgumentParser(
            description=description,
            add_help=False,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            **argparse_kwargs
        )

        parser.add_argument(
            '--version',
            action='version',
            version='%(prog)s {0}'.format(version),
            help='Show program\'s version number and exit.',
        )

        parser.add_argument(
            '--debug',
            default=False,
            action='store_true',
            help='Show tracebacks on errors.',
        )

        parser.add_argument(
            '-v', '--verbose',
            action='count',
            dest='verbose_level',
            default=self.DEFAULT_VERBOSE_LEVEL,
            help='Increase verbosity of output. Can be repeated.',
        )

        parser.add_argument(
            '-h', '--help',
            action=HelpAction,
            nargs=0,
            default=self,
            help='Show this help message and exit.',
        )

        parser.add_argument(
            '--redditapi-url',
            action='store',
            dest='redditapi_url',
            default='http://reddit.com',
            help='Reddit API url',
        )

        parser.add_argument(
            '--client-id',
            action='store',
            dest='client_id',
            help='Client ID for your registered application.',
        )

        parser.add_argument(
            '--client-secret',
            action='store',
            dest='client_secret',
            help='Secret token for your registered Client application',
        )

        parser.add_argument(
            '--username',
            action='store',
            dest='username',
            default=None,
            help='Username for your registered Client application',
        )

        parser.add_argument(
            '--password',
            action='store',
            dest='password',
            default=None,
            help='Password for your registered Client application',
        )

        parser.add_argument(
            '--user_agent',
            action='store',
            dest='user_agent',
            default='python-app/0.1 by RedditCli',
            help='User agent name for your registered Client application',
        )

        return parser

    def _clear_shell_commands(self):
        exclude_cmds = ['help']

        cmds = self.command_manager.commands.copy()
        for k, v in cmds.items():
            if k not in exclude_cmds:
                self.command_manager.commands.pop(k)

    def _get_commands(self):
        return {
            'my-karma': redditcli.commands.account.GetKarma,
        }


def main(argv=sys.argv[1:]):
    return RedditShell().run(argv)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))



























