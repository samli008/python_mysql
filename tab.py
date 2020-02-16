# pip3 install readline -i https://mirrors.aliyun.com/pypi/simple
# copy tab.py to /usr/local/lib/python3.5/site-packages
import sys
import readline
import rlcompleter
import atexit
import os

# tab completion
readline.parse_and_bind('tab: complete')
# history file
histfile = os.path.join(os.environ['HOME'], '.pythonhistory')
try:
    readline.read_history_file(histfile)
except IOError:
    pass
atexit.register(readline.write_history_file, histfile)

del os, histfile, readline, rlcompleter
