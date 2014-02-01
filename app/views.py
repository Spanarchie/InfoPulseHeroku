from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from app import app
from pyZone import webData


access = {"admin":"L1", "colin":"L5"}

@app.route('/')
def entrypoint():
    return render_template('landing.html')

@app.route('/router')
def router():
    pageSpec = webData.getPageDetail(session['username'], session['role'])
    return render_template('routerFill.html')

@app.route('/routed')
def routed():
    pageSpec = webData.getPageDetail(session['username'], session['role'])
    return render_template('routerFiller.html', layout = pageSpec)



users = {'admin':'default','joel':'bacon','luis':'bacon','colin':'bacon'}
uAtts = {'admin':{'role':'Admin', 'emp':'Nike'},'joel':{'role':'Admin', 'emp':'UX3'},'luis':{'role':'Manager', 'emp':'MagicLuis'},'colin':{'role':'Worker', 'emp':'spanarchian'}}

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
            return redirect(url_for('routed'))
        else:
            flash("Username doesn't exist or incorrect password")
            return render_template('landing.html', error=error)


@app.route('/logout')
def logout():
    session.pop('signedIn', None)
    flash('You were logged out')
    return redirect(url_for('entrypoint'))
