#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by 
# Copyright (c) 2015 
#
# License: MIT
#

"""This module exports the Galaxylint plugin class."""

from SublimeLinter.lint import Linter, PythonLinter, util


class Galaxylint(PythonLinter):
# class Galaxylint(Linter):
    """Provides an interface to galaxylint."""

    syntax = 'galaxy'
    cmd = 'galaxylint@python --file'
    regex = (
        r'^.+?:(?P<line>\d+):(?P<col>\d+): '
        r'parse (?P<error>error), '
        r'(?P<message>.+)'
    )
    tempfile_suffix = "galaxy"
    # error_stream = util.STREAM_STDOUT
    error_stream = util.STREAM_BOTH
