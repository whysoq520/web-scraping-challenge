from flask import Flask, render_template, redirect, time
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# setup mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/Mars_app")



@app.route('/')
def index():
    mars = mongo.db.mars_collection.find()
    return render_template('index.html', mars=mars)


@app.route('/scrape')
def scrape():
    # Run the scrape function
    mars_info= scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.mars_collection.update({}, mars_info, upsert=True)

    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
