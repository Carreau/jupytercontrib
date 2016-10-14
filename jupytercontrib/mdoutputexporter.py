"""
Custom exporter that encloses notebook outputs in ```output ``` code blocks.
"""

import os.path

from nbconvert.exporters.markdown import MarkdownExporter

#-----------------------------------------------------------------------------
# Classes
#-----------------------------------------------------------------------------

class MarkdownOutputExporter(MarkdownExporter):

    @property
    def template_path(self):
        x = super(MarkdownOutputExporter, self).template_path+[os.path.join(os.path.dirname(__file__), "templates")]
        print(x)
        return x

    def _template_file_default(self):
        return 'md_output' # markdown
