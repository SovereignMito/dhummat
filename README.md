# dhummat Command Set Math Tool v1.2
by SovereignMito

dhummat (doom-ought) is a terminal-style tool that can provide mathematical functions through "Command Sets." Command Sets are specialized packages that grant access to certain mathematical tools within dhummat. Though, there is design potential for non-mathematical Command Sets.

Developed in Python 3 (specifically tested in 3.10.6). Python is required to run dhummat. 

To run, use `python3 dhummat.py` in a command line in the directory containing `dhummat.py`. An executable version may be considered in the future, but for now file operations will not work in Windows by only double clicking the dhummat script file.

The tool and source code are free and available on this repository, however please verify that you have read the [License Agreement](LICENSE) and the [Acceptable Use Policy](AUP.md) before use.

Quick Start:  
- The `info` command queries a list of commands. `info <command>` provides more detailed information.
- Check out the [wiki](https://github.com/SovereignMito/dhummat/wiki).

# Version 1.2
### Functionality
- Added special sign `$`. Automatically stores the value of the last successful signable command.
- Added command chaining. By separating commands with `>>`, execute multiple commands in one line.
    - See the new [wiki](https://github.com/SovereignMito/dhummat/wiki/Command-Chaining) page for full details.
- Added support for inputting a command (encapsulated in quotes for commands more than 1 word/command chains) as a command line argument, allowing for instant evaluation without entering the dhummat terminal.
- Fixed dhummat lacking functionality for input in the OS terminal (pipes, '< filename'). Commands such as `echo add 1 2 | python3 dhummat.py` and `python3 dhummat.py < a.txt` (where `a.txt` contains a command(s) like `add 1 2`) should work now. This should behave similarly to using a command line argument, i.e. dhummat returns the output without starting an interactive terminal.
    - See the new [wiki](https://github.com/SovereignMito/dhummat/wiki/Input-Instructions) page for more information on how dhummat handles input overall.
### Command Sets
- Sign: The functionality of sign copy - `sign a b` - has been reversed such that the value of `b` is copied to `a`. This is to be consistent with `sign a n`, where the 2nd value is signed to the 1st.

Report bugs and send feedback in the discussions tab.