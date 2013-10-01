first_look
==========

A simple data previewer for delimited text data files. Uses pandas and matplotlib to plot the data, without a lot of nonsense.

Example:

Open a python terminal and switch to the directory containing first_look.py and the examples folder.

```python
import first_look as fl
fl.look("examples/carbon_fiber_test_data.tsv",plot_type="scatter")
```

![Example Plot](/examples/carbon_fiber_test_plot.png)
