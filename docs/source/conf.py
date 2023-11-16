
# -- Project information ------------------------------------------------------
project = 'autodevice'
copyright = '2023, Michael E. Vinyard'
author = 'Michael E. Vinyard'
release = '0.1.0rc0'


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
    "github_url": "https://github.com/mvinyard/neural-diffeqs",
    "twitter_url": "https://twitter.com/vinyard_m",
}
