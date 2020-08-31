from app import db
from sqlalchemy_imageattach.entity import Image, image_attachment

# Models
class AllRecipes(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    description = db.Column(db.String(512))
    description = db.Column(db.String(2048))
    photo = image_attachment('UserPicture')

    def __repr__(self):
        return '<AllRecipes %r - %r - %r - %r>' % self.name, self.description, self.photo, self.recipe