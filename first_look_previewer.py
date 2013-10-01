# usage (type in terminal):
# python first_look_previewer.py file_to_preview
# expected to be in same directory as first_look.py

# alternately, just open python and import the first_look
# module (this is better and has more options)

# run help(first_look) for further instructions

import sys
import first_look as fl
datafile = sys.argv[1]

fl.look(datafile)
