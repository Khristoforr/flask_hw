from app import db




class Ad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(1000))
    creation_date = db.Column(db.String(64))
    owner = db.Column(db.String(40))

    def __str__(self):
        return f'AD {self.title}'

    def __repr__(self):
        return str(self)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            "owner": self.owner
        }