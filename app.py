from flask import Flask , render_template ,request ,redirect

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
