project = "collectiontools"
html_theme = "sphinx_book_theme"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
]
exclude_patterns = [
    "venv",
    ".venv",
]
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}
