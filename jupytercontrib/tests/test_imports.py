

def test_py2to3_import():
    from jupytercontrib.py2to3exporter import Python2to3Exporter
    Python2to3Exporter()


def test_mdconvert_import():
    from jupytercontrib.mdoutputexporter import MarkdownOutputExporter
    MarkdownOutputExporter()
