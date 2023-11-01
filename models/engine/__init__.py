#!/usr/bin/python3
"""create unique file storage"""


from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
