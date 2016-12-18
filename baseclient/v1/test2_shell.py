import logging
import os

from cliff.command import Command

class Test2Cmd(Command):
    "A simple command that prints a message."

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(Test2Cmd, self).get_parser(prog_name)
        return parser

    def take_action(self, parsed_args):
        self.log.info('sending greeting')
        self.log.debug('debugging')
        self.app.stdout.write('hi!test2\n')
