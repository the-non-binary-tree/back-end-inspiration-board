from app import db


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    board_id = db.Column(db.Integer, db.ForeignKey('board.board_id'))
    message = db.Column(db.String, nullable=False)
    like_count = db.Column(db.Integer, default=0)
    board = db.relationship("Board",lazy=True)


    def to_dict(self):
        return {
            "id": self.id, 
            "board_id": self.board_id,
            "message": self.message,
            "like_count": self.like_count
        }
