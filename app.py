#Import dependencies
import os
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask import Flask, jsonify, render_template
import sqlalchemy
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import renewable_scrape
import json


os.chdir(os.path.dirname(os.path.abspath(__file__)))
engine = create_engine("sqlite:///project.sqlite")


# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Dataset = Base.classes.dataset

#Create Flask App
app = Flask(__name__)

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "templates", "USA.geojson")
heatmapdata = json.load(open(json_url))

#Connect to Mongo DB
app.config["MONGO_URI"] = "mongodb://localhost:27017/renewables"
mongo = PyMongo(app)

@app.route("/") 
def welcome():

    return render_template("index.html")

#Create route for scrape
@app.route("/scrape")
def scrape():
    # Run the scrape function
    renewable_data = renewable_scrape.renewable_scrape()

    # Update the Mongo database using update and upsert=True
    mongo.db.renewables.replace_one({}, renewable_data, upsert=True)
    return redirect("/webscrape_sunburst")

#Create route for hydro-electric energy production
@app.route("/hydro")
def hydro():

    return render_template("hydro.html")

#Create route for wind energy production
@app.route("/wind")
def wind():

    return render_template("wind.html")

#Create route for heatmap
@app.route("/heatmap")
def heatmap():

    return render_template("heatmap.html")

#Create route for solar energy production
@app.route("/solar")
def solar():

    return render_template("solar.html")

#Create route for location
@app.route("/location")
def location():

    return render_template("location.html")

#Create route for webscrape and sunburst
@app.route("/webscrape_sunburst")
def webscrape_sunburst():

    #Take one instance from the Mongo DB
    data = mongo.db.renewables.find_one()

    return render_template("Webscrape_sunburst.html",r_last_refresh=data["renewable_refresh"],renewable_title_0=data["renewable_titles"][0],renewable_link_0=data["renewable_links"][0],renewable_title_1=data["renewable_titles"][1],renewable_link_1=data["renewable_links"][2], renewable_title_2 = data["renewable_titles"][2],renewable_link_2=data["renewable_links"][4],renewable_title_3=data["renewable_titles"][3],renewable_link_3=data["renewable_links"][6])

#Create route for heatmap
@app.route("/api/heatmap")
def heatmapgeojson():
    return jsonify(data = heatmapdata)


@app.route("/data")
def data():
    """Return dashboard.html."""
    return render_template("data.html")


if __name__ == '__main__':
    app.run(debug=True)
