__author__ = 'Gobin'

import argparse
import logging

from cliff import command
from cliff import show


class GetKarma(show.ShowOne):

    # def get_parser(self, program_name):
    #     parser = super(GetKarma, self).get_parser(prog_name)
    #
    #     parser.add_argument(
    #
    #     )

    def take_action(self, parsed_args):
        uri = '/api/v1/me/karma'