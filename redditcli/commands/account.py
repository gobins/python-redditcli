__author__ = 'Gobin'

import argparse
import logging

from cliff import command
from cliff import show

from redditcli.api import base
from redditcli.api import account



class GetKarma(show.ShowOne):

    def get_parser(self, program_name):
        parser = super(GetKarma, self).get_parser(prog_name)

        parser.add_argument(


        )

    def take_action(self, parsed_args):
        account = account.AccountManager(self.app.client).getkarma(parsed_args.name)
        return account


