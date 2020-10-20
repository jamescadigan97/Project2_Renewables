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
#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///project.sqlite")


# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Dataset = Base.classes.dataset


#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################


@app.route("/") 
def welcome():
    return render_template("index.html")

@app.route("/scrape")
def scrape():
    renewable_scrape.renewable_scrape()
    return redirect("/sunburst")

@app.route("/hydro")
def hydro():
    """Return dashboard.html."""
    return render_template("hydro.html")

@app.route("/wind")
def wind():
    """Return dashboard.html."""
    return render_template("wind.html")


@app.route("/heatmap")
def heatmap():
    
    return render_template("heatmap.html")

@app.route("/solar")
def solar():
    """Return dashboard.html."""
    return render_template("solar.html")

@app.route("/location")
def location():
    """Return dashboard.html."""
    return render_template("location.html")

@app.route("/sunburst")
def sunburst():
    data =  json.load(open("my_renewables.json","r")) 
    return render_template("webscrape_sunburst.html",r_last_refresh=data["last_scrape"],renewable_title_0=data["articles "][0],renewable_link_0=data["links"][0],renewable_title_1=data["articles "][1],renewable_link_1=data["links"][2], renewable_title_2 = data["articles "][2],renewable_link_2=data["links"][4],renewable_title_3=data["articles "][3],renewable_link_3=data["links"][6])



if __name__ == '__main__':
    app.run(debug=True)
