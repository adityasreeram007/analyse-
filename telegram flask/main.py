from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('login.html')
@app.route('/groups')
def group():
    return render_template('groups.html')
@app.route('/home')
def home():
    return render_template('telegram.html')
if __name__=='__main__':
    app.run(debug=True)