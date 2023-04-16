# Main Flask file
from datetime import datetime, timedelta
from flask import Flask, render_template, request, url_for, redirect, make_response
from database import Database
import os.path as path
from sqlite3 import IntegrityError

app = Flask("spare")
dbFile = path.join(__file__.replace('main.py', ''), 'database', 'database.db')
dbFile = r"./database.db"
db = Database(dbFile)

@app.get("/")
def index():
    return redirect(url_for('static', filename='landing_page.html'))

@app.get("/feed")
def feed():
    community = request.args.get('community', '')
    community = 'Daisy Hill'

    posts = db.select_all_posts()
    content = []

    for _, time, duration, item, post_type, tags in posts:
        name = db.select_one_user()[2]

        hour, minute, month, day, year = [int(x) for x in duration.split('_')]
        _time = datetime(year, month, day, hour, minute) + timedelta(minutes=duration)
        time = _time.strftime("%h:%m %p %-m/%d/%Y")

        content.append((name, time, item, post_type, tags))

    return render_template('feed.html', content=content, community=community)

@app.get("/login")
def validateLogin():
    email = request.args.get('email', '')
    phone = request.args.get('phone_num', '')

    user = db.select_one_user(email)

    if user is None or not user[0] == phone:
        return render_template('retry_login.html'), 404
    else:
        resp = make_response(redirect(url_for('feed', community=user[1])))
        resp.set_cookie('email', email)
        return resp

@app.get("/signup")
def validateSignup():
    email  = request.args.get('email',"")
    phone = request.args.get('phone_num',"")
    name = request.args.get('name',"")

    try:
        db.create_user((email,phone,0,'daisy_hill',name))
        return redirect(url_for('feed', community='daisy_hill'))
    except IntegrityError: 
        return render_template('retry_signup.html'), 404

@app.get("/upload")
def uploadPost():
    items = request.args.get('items', '')
    duration = int(request.args.get('duration', ''))
    type_post = request.args.get('type', '')
    tags = request.args.get('tags', '')

    email = request.cookies.get('email')

    if email is None:
        return 404
    else:
        db.create_post((email, ))
        return redirect(url_for())
