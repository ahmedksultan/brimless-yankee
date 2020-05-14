from flask import Flask, render_template
import urllib
import os
import data as dataModule
data = {
    "globalTerrorism": dataModule.globalTerrorism,
    "happiness": dataModule.happiness,
    "humanFreedomIndex": dataModule.humanFreedomIndex,
    "unemployment": dataModule.unemployment,
    "universityRankings": dataModule.universityRankings,
    "happinessROL": dataModule.happinessROL,
    "happinessTerrorism": dataModule.happinessTerrorism,
    "happinessUnemployment": dataModule.happinessUnemployment,
    "happinessUni": dataModule.happinessUni
}

app = Flask(__name__)
app.secret_key = os.urandom(24)

# landing page for project, introduction
@app.route('/')
def index():
    return render_template('index.html')

# world happiness report analysis, visualizations
@app.route('/happiness')
def happiness():
    return render_template('happiness.html', data=data)

# global terrorism database analysis, heatmap
@app.route('/terrorism')
def terrorism():
    return render_template('terrorism.html', data=data)

# global terrorism database analysis, visualizations
@app.route('/terrorism2')
def terrorism2():
    return render_template('terrorism2.html', data=data)

# human freedom index analysis, visualizations
@app.route('/freedom')
def freedom():
    return render_template('freedom.html', data=data)

# national unemployment rates (ILO) statistics analysis, visualizations
@app.route('/unemployment')
def unemployment():
    return render_template('unemployment.html', data=data)

# qs world university rankings, heatmap
@app.route('/university')
def university():
    return render_template('university.html', data=data)

# qs world university rankings, visualizations
@app.route('/university2')
def university2():
    return render_template('university2.html', data=data)

# conclusion of project/sharing of data, etc.
@app.route('/conclusion')
def conclusion():
    return render_template('conclusion.html', data=data)

if __name__ == "__main__":
    app.debug = True
    app.run()
