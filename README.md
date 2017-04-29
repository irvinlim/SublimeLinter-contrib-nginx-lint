SublimeLinter-contrib-nginx-lint
================================

[![Build Status](https://travis-ci.org/irvinlim/SublimeLinter-contrib-nginx-lint.svg?branch=master)](https://travis-ci.org/irvinlim/SublimeLinter-contrib-nginx-lint)

This linter plugin for [SublimeLinter][docs] provides an interface to [nginx-lint][nginx-lint-homepage]. It will be used with files that have the `nginx` syntax, which requires [sublime-nginx][sublime-nginx-homepage] to be installed as well.

## Installation
SublimeLinter 3 must be installed in order to use this plugin. If SublimeLinter 3 is not installed, please follow the instructions [here][installation].

### Syntax and linter installation
Before using this plugin, you must ensure that both [sublime-nginx][sublime-nginx-homepage] and [nginx-lint][nginx-lint-homepage] is installed on your system. 

#### `sublime-nginx`
Please see [sublime-nginx][sublime-nginx-homepage] for installation instructions, or simply install it via Package Control:

1. Within Sublime Text, bring up the [Command Palette][cmd] and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

2. When the plugin list appears, type `nginx`. Among the entries you should see `nginx`. If that entry is not highlighted, use the keyboard or mouse to select it.

#### `nginx-lint`

Please see [nginx-lint][nginx-lint-homepage] for installation instructions.

### Linter configuration
In order for `nginx-lint` to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. Before going any further, please read and follow the steps in [“Finding a linter executable”](http://sublimelinter.readthedocs.org/en/latest/troubleshooting.html#finding-a-linter-executable) through “Validating your PATH” in the documentation.

Once you have installed and configured `nginx-lint`, you can proceed to install the `SublimeLinter-contrib-nginx-lint` plugin if it is not yet installed.

### Plugin installation
Please use [Package Control][pc] to install the linter plugin. This will ensure that the plugin will be updated when new versions are available. If you want to install from source so you can modify the source code, you probably know what you are doing so we won’t cover that here.

To install via Package Control, do the following:

1. Within Sublime Text, bring up the [Command Palette][cmd] and type `install`. Among the commands you should see `Package Control: Install Package`. If that command is not highlighted, use the keyboard or mouse to select it. There will be a pause of a few seconds while Package Control fetches the list of available plugins.

1. When the plugin list appears, type `nginx-lint`. Among the entries you should see `SublimeLinter-contrib-nginx-lint`. If that entry is not highlighted, use the keyboard or mouse to select it.

## Settings
For general information on how SublimeLinter works with settings, please see [Settings][settings]. For information on generic linter settings, please see [Linter Settings][linter-settings].

## Contributing
If you would like to contribute enhancements or fixes, please do the following:

1. Fork the plugin repository.
1. Hack on a separate topic branch created from the latest `master`.
1. Commit and push the topic branch.
1. Make a pull request.
1. Be patient.  ;-)

Please note that modifications should follow these coding guidelines:

- Indent is 4 spaces.
- Code should pass flake8 and pep257 linters.
- Vertical whitespace helps readability, don’t be afraid to use it.
- Please use descriptive variable names, no abbreviations unless they are very well known.

Thank you for helping out!

[docs]: http://sublimelinter.readthedocs.org
[installation]: http://sublimelinter.readthedocs.org/en/latest/installation.html
[locating-executables]: http://sublimelinter.readthedocs.org/en/latest/usage.html#how-linter-executables-are-located
[pc]: https://sublime.wbond.net/installation
[cmd]: http://docs.sublimetext.info/en/sublime-text-3/extensibility/command_palette.html
[settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html
[linter-settings]: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html
[inline-settings]: http://sublimelinter.readthedocs.org/en/latest/settings.html#inline-settings

[nginx-lint-homepage]: https://github.com/temoto/nginx-lint
[sublime-nginx-homepage]: https://github.com/brandonwamboldt/sublime-nginx