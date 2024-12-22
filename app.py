import os
from flask import Flask , render_template ,request ,redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import update
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db= SQLAlchemy(app)

class messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False)
    email = db.Column(db.String(255), unique=False)
    message = db.Column(db.String(255), unique=False)


@app.route('/submit' , methods=['GET', 'POST'])
def Submit():
    if(request.method=='POST'):
        name=request.form['name']
        email=request.form['email']
        message=request.form['message']
        new_con = messages(name=name,email=email,message=message)
        db.session.add(new_con)
        db.session.commit()
        return redirect(url_for('Hello_World'))
    return render_template('index.html')  


@app.route('/')
def Hello_World():
    return render_template('index.html')


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/portfolio-details')
def portfolio_details():
    return render_template('portfolio-details.html')

@app.route('/portfolio-details1')            
def portfolio_details1():
    return render_template('portfolio-details1.html')

@app.route('/about')
def about():
    return render_template('index.html')    

@app.route('/resume')
def resume():
    return render_template('index.html')

@app.route('/portfolio')
def portfolio():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('index.html')        

if __name__ == "__main__":
    app.run(debug=True)      
