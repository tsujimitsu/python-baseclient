import logging
import os

from cliff.show import ShowOne
from cliff.lister import Lister
from cliff.command import Command


class TestCmd(Command):
    "A simple command that prints a message."

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(TestCmd, self).get_parser(prog_name)
        return parser

    def take_action(self, parsed_args):
        self.log.info('sending greeting')
        self.log.debug('debugging')
        self.app.stdout.write('hi!\n')


class TestList(Lister):
    "Show a list of test"

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(TestList, self).get_parser(prog_name)
        return parser

    def take_action(self):    
        return (('Name', 'Size'),
               (1,2)
        )
        #tests = ['','','']
        #return (('ID', 'Name'),
        #       (('1234', 'Test1')
        #       )


class TestShow(ShowOne):
    "Show detail information of test"

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(TestShow, self).get_parser(prog_name)
        return parser

    def take_action(self):
        columns = ('ID',
                   'Name',
                   'Value'
        )
        data = ('1234',
                'Test1',
                'testestes'
        )

        return (columns, data)
