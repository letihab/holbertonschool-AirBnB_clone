#!/usr/bin/python3
"""file storage autoinit"""

from models.engine.file_storage import FileStorage

"""variable storage, and instance of filestorage"""
storage = FileStorage()
storage.reload()
