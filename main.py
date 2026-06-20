from flask import Flask, render_template
app = Flask(__name__)
 
@app.route('/')
def home_page():
    return render_template('homepage.html')

@app.route('/sezione1')
def sezione1():
    return render_template('first.html')

@app.route('/sezione2')
def sezione2():
    return render_template('second.html')
   





app.run(debug=True)