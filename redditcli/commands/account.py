__author__ = 'Gobin'

import argparse
import logging
import json
from cliff import show
from cliff import command
from cliff import lister

from redditcli.api import account


class Me(lister.Lister):
    log = logging.getLogger(__name__)

    def get_parser(self, program_name):
        parser = super(Me, self).get_parser(program_name)
        return parser

    def take_action(self, parsed_args):
        mydetails = account.AccountManager(self.app.client).me()
        if mydetails:
            data = ((n, v) for n, v in mydetails._data.iteritems())
            columns = (
                'Field',
                'Value'
            )
            return columns, data
        else:
            return None


class Karma(lister.Lister):
    log = logging.getLogger(__name__)

    def get_parser(self, program_name):
        parser = super(Karma, self).get_parser(program_name)
        return parser

    def take_action(self, parsed_args):
        mykarma = account.AccountManager(self.app.client).getkarma()
        if mykarma:
            data = ((n['sr'], n['comment_karma'], n['link_karma']) for n in mykarma.data)
            columns = (
                'Subreddit',
                'Comment Karma',
                'Link Karma'
            )
            return columns, data
        else:
            return None


class Friends(lister.Lister):
    log = logging.getLogger(__name__)

    def get_parser(self, program_name):
        parser = super(Friends, self).get_parser(program_name)
        return parser

    def take_action(self, parsed_args):
        myfriends = account.AccountManager(self.app.client).getfriends()
        self.log.debug('Test: %s', myfriends)
        if myfriends:
            data = ((n['date'], n['name'], n['id']) for n in myfriends.children)
            columns = (
                'Date',
                'Name',
                'Id'
            )
            return columns, data
        else:
            return None


class Prefs(lister.Lister):
    log = logging.getLogger(__name__)

    def get_parser(self, program_name):
        parser = super(Prefs, self).get_parser(program_name)
        return parser

    def take_action(self, parsed_args):
        myprefs = account.AccountManager(self.app.client).me()
        if myprefs:
            data = ((n, v) for n, v in myprefs._data.iteritems())
            columns = (
                'Field',
                'Value'
            )
            return columns, data
        else:
            return None