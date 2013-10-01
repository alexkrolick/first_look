'''Simple data previewer.'''

import matplotlib.pyplot as plt
import pandas

def look(datafile,x_col=0,plot_type="scatter",delimiter="\t"):
	'''A simple graphical data previewer that plots columns against
	   each other. Expects data to be stored in columns with one row
	   of headers inside a delimited text file, i.e., .tsv or .csv.
	   You need pandas and matplotlib installed to use this module.

	   Required inputs: datafile - path to file to preview (string)

	   Optional inputs: x_col - which column to use for x-axis
								(int, index starts at 0)
						plot_type - "scatter" or "line" plot (string)
						delimiter - data file delimiter (string),
									usually tab ("\t") or comma (",")

		Recommended usage:
			import first_look as fl
			fl.look("your_data_file")
	'''
	if plot_type == "scatter":
		sty = "o"
	else:
		sty = "-"

	df = pandas.read_csv(datafile,sep=delimiter) # create a dataframe
	df.plot(x=x_col,title=datafile,style=sty) # create a matplotlib object
	plt.show() # show the plot

