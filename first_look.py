'''Simple data previewer.'''

import matplotlib.pyplot as plt
import pandas

def look(datafile,x_col=0,plot_type="scatter",delimiter="\t",
ylabel="",xlabel="",title=""):
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
						ylabel - Y-axis label (string)
						xlabel - X-axis label (string)

		Recommended usage:
			import first_look as fl
			fl.look("your_data_file")
	'''
	if plot_type == "scatter":
		sty = "o"
	else:
		sty = "-"
	if title=="":
		title=datafile

	df = pandas.read_csv(datafile,sep=delimiter) # create a dataframe
	ax = df.plot(x=x_col,title=title,style=sty) # create a matplotlib axis
	if ylabel != "":
		ax.set_ylabel(ylabel)
	if xlabel != "":
		ax.set_xlabel(xlabel)
	plt.show() # show the plot

