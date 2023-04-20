# dhummat Command Set Math Tool v1.1
by Mito-EK

dhummat (doom-ought) is a terminal-style tool that can provide mathematical functions through "Command Sets." Command Sets are specialized packages that grant access to certain mathematical tools within dhummat. Though, there is design potential for non-mathematical Command Sets.

Developed in Python 3 (specifically tested in 3.10.6). Python is required to run dhummat. 

To run, use `python3 dhummat.py` in a command line in the directory containing `dhummat.py`. An executable version may be considered in the future, but for now file operations will not work in Windows by only double clicking the dhummat script file.

The tool and source code are free and available on this repository, however please verify that you have read the [License Agreement](LICENSE) and the [Acceptable Use Policy](AUP.md) before use.

Quick Start:  
- The `info` command queries a list of commands. `info <command>` provides more detailed information.
- Check out the [wiki](https://github.com/SovereignMito/dhummat/wiki).

# Version v1.1
### Operations
- fileops: Fixed a bug where leaving whitespace at the end of a line in a script file could cause a command to fail when using `scr`.
- dhummat: Separated error messages from unrecognized commands and unexpected errors (due to coding mistakes).
### Command Sets
- Added Arithmetic Set: add, sub, mult, div, mod, pow, round, floor, ceil

Report bugs and send feedback in the discussions tab.