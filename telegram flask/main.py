from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)
@app.route('/telegram',methods = ['POST'])
def telegram():
    return render_template('telegram.html')
@app.route('/login', methods = ['POST'])
def login():
    error = None
    
    if request.method == 'POST':
        if (request.form["username"] == 'admin' or request.form["password"] == 'admin'):
            #print(request.form['username'])
            error = 'Invalid username or password. Please try again!'
            return render_template('login.html', error = error)
        else:
            flash('You were successfully logged in')
            return redirect(url_for('telegram'))    
    return render_template('login.html', error = error)
@app.route('/groups',methods = ['POST'])
def group():
    return render_template('groups.html')
# @app.route('/home')
# def home():
#     return render_template('telegram.html')
if __name__=='__main__':
    app.run(debug=True)





