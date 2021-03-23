from flask import Flask, render_template,redirect
from flask_pymongo import PyMongo
import Mars_Scrape


#create an instance for Flask App
app = Flask(__name__) 

#connect 
app.config["MONGO_URI"]='mongodb://localhost:27017/marsdb'
mongo= PyMongo(app)


@app.route("/")
def index():
    data=mongo.db.collection.find_one()
    return render_template ('index.html', mars=mars)

@app.route('/scrape')
def scrape():
    return render_template ('index.html', mars=mars)
    

if __name__=="__main__":
    app.run(debug=True)
    