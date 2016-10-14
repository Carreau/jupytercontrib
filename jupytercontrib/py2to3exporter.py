# Copyright 2016 - The Jupyter development team
# adapted from Thomas Kluyver nb2to3 script:
# https://gist.github.com/takluyver/c8839593c615bb2f6e80
""" Simple exporter that convert a notebook from Legacy Python 2 to Python 3
"""


from nbconvert.exporters.notebook import NotebookExporter


#!/usr/bin/env python3
"""
To run: python3 nb2to3.py notebook-or-directory
"""
# Authors: Thomas Kluyver, Fernando Perez
# See: https://gist.github.com/takluyver/c8839593c615bb2f6e80

import lib2to3
from lib2to3.refactor import RefactoringTool, get_fixers_from_package


from nbconvert.preprocessors import Preprocessor

class Python2to3Preprocessor(Preprocessor):
    """A Pelican specific preprocessor to remove some of the cells of a notebook"""

    # I could also read the cells from nb.metadata.pelican if someone wrote a JS extension,
    # but for now I'll stay with configurable value.

    def __init__(self, *args, **kwargs):
        super(Python2to3Preprocessor, self).__init__(*args, **kwargs)
        availables_fixes = set(get_fixers_from_package('lib2to3.fixes'))
        self.refactoring_tool = RefactoringTool(availables_fixes)


    def preprocess(self, nb, resources):
        self.log.info("runnign 2to3 on each cell of the notebook.")
        refactor_notebook_inplace(nb, self.refactoring_tool, '<dummy path>')
        return nb, resources


def refactor_notebook_inplace(nb, refactoring_tool, path):
    
    def refactor_cell(src):
        try:
            tree = refactoring_tool.refactor_string(src+'\n', str(path) + '/cell-%d' % i)
        except (lib2to3.pgen2.parse.ParseError,
                lib2to3.pgen2.tokenize.TokenError):
            return src
        else:
            return str(tree)[:-1]

    
    # Run 2to3 on code
    for i, cell in enumerate(nb.cells, start=1):
        if cell.cell_type == 'code':
            if cell.execution_count in ('&nbsp;', '*'):
                cell.execution_count = None

            if cell.source.startswith('%%'):
                # For cell magics, try to refactor the body, in case it's
                # valid python
                head, source = cell.source.split('\n', 1)
                cell.source = head + '\n' + refactor_cell(source)
            else:
                cell.source = refactor_cell(cell.source)
                   

    # Update notebook metadata
    nb.metadata.kernelspec = {
        'display_name': 'Python 3',
        'name': 'python3',
        'language': 'python',
    }
    if 'language_info' in nb.metadata:
        nb.metadata.language_info.codemirror_mode = {
            'name': 'ipython',
            'version': 3,
        }
        nb.metadata.language_info.pygments_lexer = 'ipython3'
        nb.metadata.language_info.pop('version', None)




class Python2to3Exporter(NotebookExporter):
    """
    This is a custom exporter that will pate all cells to use Python 3.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.register_preprocessor( Python2to3Preprocessor(), enabled=True)
 





