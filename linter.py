#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Irvin Lim
# Copyright (c) 2017 Irvin Lim
#
# License: MIT
#

"""This module exports the NginxLint plugin class."""

from SublimeLinter.lint import Linter, util


class NginxLint(Linter):
    """Provides an interface to nginx-lint."""

    syntax = 'nginx'
    cmd = 'nginx-lint'
    executable = None
    regex = (
        r'^\"?.+(?::|\" \(line )'                       # Matches `filename:` OR `"filename" (line `
        r'(?P<line>\d+)'                                # Captures line number
        r'(?::|, column )'                              # Matches `:` OR `, column `
        r'(?P<col>\d+)'                                 # Captures column number
        r'(?:\):\n| )'                                  # Matches `):\n` OR a space
        r'(?:(?P<warning>[^\s]+): |(?P<error>.+)\n)'    # Captures warning before `: `, or error before `\n`
        r'(?P<message>.+)'                              # Captures message
    )
    multiline = True                                    # Errors span 3 lines, while warnings span 1
    tempfile_suffix = '.conf'                           # nginx-lint takes in a file name, rather than input from stdin
    error_stream = util.STREAM_BOTH
