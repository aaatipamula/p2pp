# Main Flask file
from flask import Flask, render_template, request, url_for, redirect

app = Flask("spare")

@app.get("/")
def index():
    return redirect(url_for('static', filename='index.txt'))

@app.get("/feed")
def feed():
    content = ('item1', 'item2', 'item3')
    return render_template('feed.html', content=content)

@app.get("/login")
def validateLogin():
    email = request.args.get('email', '')
    phone = request.args.get('phone_num', '')
    user = 'thing' #get user class

    if not user is None:
        return render_template('not_found.html'), 404
    else:
        #redirect
        return redirect(url_for('feed', community=user.community))

