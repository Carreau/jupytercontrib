# jupyter contrib

Some small utilities that are related to Jupyter. 

This is not endorsed by the Jupyter team, and not part of the official Jupyter project. 

Feel free to submit any patches, or utility modules for which a full packages
might be inappropriate or too much of an hassle. 

# installation

```
pip install jupytercontrib
```

# Extensions

Any extension present here should not modify Jupyter/IPython behavior at install time. 
You can provide a tool to simplify activation, but installation should likely be without side-effects. 


# What can I find here:


## 2to3 for notebooks

An extra nbconvert exporter that convert Legacy Python 2 notebook to New Awesome and useful Python 3
It requires `nbconvert` master. 


It uses [entry points]  to directly expose a `--to=2to3` when using `jupyter nbconvert`, thus you can do thing like 

```
jupyter nbconvert --to 2to3 <mynotebook.ipynb>
```

This will create a file name `mynotebook.nbconvert.ipynb` which each cell converted to Python 3. 


## Markdown exporter w/ output

Extension of the standard notebook-to-markdown exporter that tags output cells as `output`.
Can be used, for example, when building Sphinx docs to style output differently from input code blocks. 

```
jupyter nbconvert --to mdoutput --output=<output.md> <mynotebook.ipynb>
```
