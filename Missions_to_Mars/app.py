from flask import Flask, render_template, redirect
import pymongo
import time
import scrape_mars


app = Flask(__name__)

# setup mongo connection
conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

db = client.mars_db
collection = db.mars_collection




@app.route('/')
def index():
    mars = db.collection.find()
    return render_template('index.html', mars=mars)


@app.route('/scrape')
def scrape():
    # Run the scrape function
    mars_data = scrape_mars.scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.mars_collection.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
