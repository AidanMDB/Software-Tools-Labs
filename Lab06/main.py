import flask
import sqlite3

app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return flask.redirect('/home')

@app.route('/home', methods=['GET'])
def home():
    return flask.render_template("music.html")


@app.route('/song/<scode>', methods=['GET', 'POST'])
def song_id(scode):
    conn = sqlite3.connect('data/music.db')
    c = conn.cursor()
    song = c.execute(f"SELECT * FROM songs where id={scode}").fetchone()
    c.close()
    conn.close()
    return flask.render_template('song_display.html', music=song)
    



if __name__ == '__main__':
    app.run(port=8050, host='127.0.0.1', debug=True)