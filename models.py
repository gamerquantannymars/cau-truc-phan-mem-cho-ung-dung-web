from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    """
    Model đại diện cho người dùng trong hệ thống.
    """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        """
        Trả về chuỗi đại diện cho đối tượng User.
        """
        return f'<User {self.username}>'