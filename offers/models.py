from common.models import Column, ForeignKey, Integer, String, db
from users.models import User


class Offer(db.Model):
    __tablename__ = "offers"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    text = Column(String)
    user_id = Column(Integer, ForeignKey(User.id))
