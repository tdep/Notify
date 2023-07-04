from core import db

# class Playlist(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(140))
#     date = db.Column(db.Date())
#     time = db.Column(db.Time())
#     category = db.Column(db.String, db.ForeignKey('category.id'))

#     def __repr__(self):
#         return '<Playlist {}'.format(self.title)

class Todo(db.model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    date = db.Column(db.Date())
    time = db.Column(db.Time())
    category = db.Column(db.String, db.ForeignKey('category.id'))

    def __repr__(self):
        return '<ToDo {}>'.format(self.title)