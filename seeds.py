from app.models import User
from app.db import Session, Base, engine
from app.models import User, Post, Comment, Vote

#drop and rebuild tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

db = Session()

#insert users
db.add_all([
    User(username="alesmonde0", email="nwestnedge@cbc.ca", password="password123"),
    User(username="jwilloughway1", email="rmebes1@sogou.com", password="password123"),
    User(username="iboddam2", email="cstoneman2@last.fm", password="password123"),
    User(username="dstanmer3", email="ihellier3@goo.net.jp", password="password123"),
    User(username="djiri4", email="gmidgley4@weather.com", password="password123")
])

db.commit()

db.add_all([
    Post(title="TitleOne", post_url="one.com", user_id=1),
    Post(title="TitleTwo", post_url="two.com", user_id=2),
    Post(title="TitleThree", post_url="three.com", user_id=3),
    Post(title="TitleFour", post_url="four.com", user_id=4)
])

db.commit()

#insert comments
db.add_all([
    Comment(comment_text="Check me out", user_id=1, post_id=2),
    Comment(comment_text="Another comment here", user_id=2, post_id=3),
    Comment(comment_text="Third comment", user_id=3, post_id=4),
    Comment(comment_text="Fourth comment", user_id=4, post_id=1)
])

db.commit()

db.add_all([
    Vote(user_id=1, post_id=2),
    Vote(user_id=1, post_id=4),
    Vote(user_id=2, post_id=4),
    Vote(user_id=3, post_id=4),
    Vote(user_id=3, post_id=2),
    Vote(user_id=4, post_id=2)
])

db.commit()

db.close()