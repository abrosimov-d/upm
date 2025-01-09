from db import DB
from helper import Helper
from datetime import datetime
scheme = {
    'id': 'integer primary key autoincrement not null',
    'page_id': 'text',
    'page_url': 'text',
    'title': 'text',
    'time': 'text',
    'data': 'text',
}

class Snapshot:
    def __init__(self, page_id, url, title, time, data):
        self.data = {}
        self.data['id'] = Helper.random_id()
        self.data['page_id'] = page_id
        self.data['page_url'] = url
        self.data['title'] = title
        self.data['time'] = datetime.now()
        self.data['data'] = data
        self.db = DB('snapshots.db')
        #def create(self, table, scheme):
        self.db.create('snapshots', scheme)

    def store_to_db(self):
        self.db.insert_data('snapshots', self.data)
