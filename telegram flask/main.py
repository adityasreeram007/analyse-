from flask import Flask,render_template,request,redirect,url_for,session
import os
app=Flask(__name__)
@app.route('/')
def telegram():
    if not session.get('logged_in'):
        return render_template('login.html')       
    else:
        return render_template('telegram.html')
@app.route('/login', methods = ['POST'])
def login():
    error = None
    
    if request.method == 'POST':
        if (request.form["username"] == 'admin' or request.form["password"] == 'admin'):
            #print(request.form['username'])
            session['logged_in']=True
        else:
            flash('Wrong password')
    return telegram()   
    #return render_template('login.html', error = error)
@app.route('/groups')
def group():
    return render_template('groups.html')
# @app.route('/home')
# def home():
#     return render_template('telegram.html')
if __name__=='__main__':
    app.secret_key=os.urandom(12)
    app.run(debug=True)





