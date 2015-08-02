__author__ = 'Gobin'

import argparse
import logging
from cliff import show
from cliff import command

from redditcli.api import account


class GetKarma(show.ShowOne):
    log = logging.getLogger(__name__)

    #def __init__(self):
    #    self.log.debug('Initializing GetKarma.')

    def get_parser(self, program_name):
        parser = super(GetKarma, self).get_parser(program_name)
        return parser

    def take_action(self, parsed_args):
        mykarma = self.app.client.account.getkarma()
        if mykarma is not None:
            self.log.debug('There is something inside.')
        return mykarma


