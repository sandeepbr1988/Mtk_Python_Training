from flask import Flask,request
from flask import render_template

app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    
    return render_template("index.html")
    #return '<h1>Hello, World</h1>'
@app.route('/about',methods=['GET'])    
def about():
    
    return render_template("about.html")
    #return '<h1>Hello, World</h1>'  
      
@app.route('/services',methods=['GET'])
def services():
    return render_template("services.html")

@app.route('/technology',methods=['GET'])
def technology():
    return render_template("technology.html")

@app.route('/contact',methods=['GET'])
def contact():
    return render_template("contact.html")
if __name__ == '__main__':
    app.run(debug=True)


