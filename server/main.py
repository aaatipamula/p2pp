# Main Flask file
from flask import Flask, render_template, request, url_for, redirect
from database import Database
import os.path as path
from sqlite3 import IntegrityError

app = Flask("spare")
dbFile = path.join(__file__.replace('main.py', ''), 'database', 'database.db')
dbFile = r"./database/database.db"
db = Database(dbFile)

@app.get("/")
def index():
    return redirect(url_for('static', filename='index.txt'))

@app.get("/feed")
def feed():
    community = request.args.get('community', '')

    content = db.select_all_posts()
    return render_template('feed.html', content=content, community=community)

@app.get("/login")
def validateLogin():
    email = request.args.get('email', '')
    phone = request.args.get('phone_num', '')

    db_phone = db.select_one_user(email)

    if not db_phone == phone:
        return render_template('retry.html'), 404
    else:
        return redirect(url_for('feed', community=user.community))

@app.get("/signup")
def validateSignup():
    pass
