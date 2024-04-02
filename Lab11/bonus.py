# ######################################################
# Author :  Aidan Dannhausen-Brun
# email :   adannhau@purdue.edu
# ID :      ee364a10
# Date :    3/31/24
# ######################################################


from sqlalchemy import String, Integer
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import Column

# ######################################################
# No Module - Level Variables or Statements !
# ONLY FUNCTIONS BEYOND THIS POINT !
# ######################################################


class Base(DeclarativeBase):
    pass


class Post(Base):

    __tablename__ = "posts"

    postID = Column("postid", String)
    postTitle = Column("posttitle", String)
    uID = Column("userid", Integer)
    cont = Column("content", String)

    def __init__(self, **kw):
        super().__init__(**kw)

    def __repr__(self) -> str:
        return f"""Post(postID={self.postID!r}, postTitle={self.postTitle!r},
                    userID={self.uID!r}, content={self.cont!r})"""


def create_table(engine):
    Base.metadata.create_all(engine)


def create_session_factory():
    engine = create_engine("sqlite:///database.db", echo=True)
    return sessionmaker(bind=engine)


def add_post(post_id, posttitle, userid, content):
    session = create_session_factory()
    new_post = Post(post_id, posttitle, userid, content)
    session.add(new_post)
    if (posttitle.endswith("announcment")):
        session.add(Post(post_id, posttitle.replace('announcement', 'class1'), userid, content))
        session.add(Post(post_id, posttitle.replace('announcement', 'class2'), userid, content))
        session.add(Post(post_id, posttitle.replace('announcement', 'class3'), userid, content))
    session.commit()

# This block is optional and can be used for testing .
# We will NOT look into its content .
# ######################################################


if __name__ == "__main__":

    from sqlalchemy import create_engine

    engine = create_engine("sqlite:///database.db", echo=True)
    create_table(engine)
