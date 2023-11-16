
# -- setup: -------------------------------------------------------------------
import os
import pathlib

project = 'autodevice'

cwd = pathlib.Path(os.getcwd())
project_dir = cwd.parent.parent.joinpath(project)
version_path = project_dir.joinpath("__version__.py")

with open(version_path) as v:
    exec(v.read()) # yields __version__


# -- Project information ------------------------------------------------------

copyright = '2023, Michael E. Vinyard'
author = 'Michael E. Vinyard'
release = __version__


# -- General configuration: ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'nbsphinx',
    'sphinx_copybutton',
    'sphinx_design',
]

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output: ------------------------------------------------
html_theme = 'pydata_sphinx_theme'

html_static_path = ['_static']
html_css_files = ['css/custom.css']

html_theme_options = {
    "github_url": "https://github.com/mvinyard/autodevice",
    "twitter_url": "https://twitter.com/vinyard_m",
}
