"""
SocialNet Parser - A social network XML data parser and visualizer.

This package provides functionality to parse, validate, format, and visualize
social network data stored in XML format.
"""

__version__ = "1.0.0"
__author__ = "SocialNet Parser Team"

from .controllers import XMLController, DataController
from .controllers.utilities.binary_utils import ByteUtils
from .ui import CodeViewerWindow, LandingWindow, ManualWindow, BrowseWindow, BaseXMLWindow
from utils.file_io import read_file, write_file, read_binary, write_binary, pretty_format
from utils.token_utils import is_opening_tag, is_closing_tag, extract_tag_name, tokenize

__all__ = [
    'XMLController',
    'DataController',
    'ByteUtils',
    'CodeViewerWindow',
    'BaseXMLWindow',
    'BrowseWindow',
    'ManualWindow',
    'LandingWindow',
    'read_file',
    'write_file',
    'read_binary',
    'write_binary',
    'pretty_format',
    'is_opening_tag',
    'is_closing_tag',
    'extract_tag_name',
    'tokenize'
]
