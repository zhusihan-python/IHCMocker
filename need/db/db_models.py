import os
import sqlite3
from need.settings import proj_root


class DBModels(object):
    def __init__(self):
        self.conn = sqlite3.connect(os.path.join(proj_root, "mocker.db"))
        self.cur = self.conn.cursor()


db_model = DBModels()
