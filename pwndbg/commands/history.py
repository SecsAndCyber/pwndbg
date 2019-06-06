#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Display the history.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import argparse

try:
    import readline
except ImportError:
    """
        This can error on some GDB instances
        Encountered on docker `debian:jessie`
    # (gdb) pi import pwndbg
    # Python Exception <type 'exceptions.ImportError'> readline module disabled under GDB:
    """
    readline = None

import gdb

import pwndbg.commands

parser = argparse.ArgumentParser()
parser.description = __doc__
parser.add_argument('count', type=int, nargs='?',
                    help='The amount of history entries to display')
@pwndbg.commands.ArgparsedCommand(parser)
def history(count=10):
    if readline is None:
        print("Command history not supported due to import error")
        return
    history_length = readline.get_current_history_length()
    history = reversed([readline.get_history_item(i) for i in range(history_length)])
    history = list(history)[:min(count, history_length)]
    for entry in history:
        print(entry)
