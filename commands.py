import logging

from cliff.command import Command

class GetIdentity(Command):
    """Command to get the identity of the user."""

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        self.log.info('Test Command')
