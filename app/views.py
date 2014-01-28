from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from app import app
from pyZone import webData


access = {"admin":"L1", "colin":"L5"}

@app.route('/')
def entrypoint():
    return render_template('index.html')

@app.route('/router')
def router():
    return render_template('routerFill.html')

@app.route('/brief')
def brief():
    formBrief, BriefReports = webData.getBriefData()
    return render_template('brief.html',
        title = 'Brief',
        user = formBrief,
        posts = BriefReports)

users = {'admin':'default','joel':'bacon','luis':'bacon','colin':'bacon'}
uAtts = {'admin':{'role':'Admin', 'emp':'Nike'},'joel':{'role':'Client', 'emp':'UX3'},'luis':{'role':'Analyst', 'emp':'MagicLuis'},'colin':{'role':'DemiGod', 'emp':'Spanarchian.co.uk'}}

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        required = ['username', 'password']
        for r in required:
            if r not in request.form:
                flash("Error: {0} is required.".format(r))
                return render_template('landing.html', error=error)
        
        usr = request.form['username']
        pwdIn = request.form['password']

        if usr in users and users[usr] == pwdIn:
            data = uAtts[usr]
            session['signedIn'] = True
            session['username'] = usr
            session['role'] = data['role']
            session['emp'] = data['emp']
            flash('You were logged in')
            return redirect(url_for('brief'))
        else:
            flash("Username doesn't exist or incorrect password")
            return render_template('landing.html', error=error)


@app.route('/logout')
def logout():
    session.pop('signedIn', None)
    flash('You were logged out')
    return redirect(url_for('entrypoint'))
