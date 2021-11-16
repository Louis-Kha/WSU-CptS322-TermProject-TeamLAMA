from datetime import timedelta
from flask import session
from app import create_app, db, LoginManager
from app.Model.models import Post, Tag

app = create_app()

# done here
@app.before_first_request
def initDB(*args, **kwargs):
    # loginMgr = LoginManager()
    # loginMgr.init_app(app)
    # session.permanent = False
    # app.permanent_session_lifetime = timedelta(minutes=20)
    # session.modified = True
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)