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

# global terrorism database analysis, visualizations
@app.route('/terrorism')
def terrorism():
    return render_template('terrorism.html', data=data)

# human freedom index analysis, visualizations
@app.route('/freedom')
def freedom():
    return render_template('freedom.html', data=data)

'''
@app.route('/happiness-rol')
def happinessROL():
    return render_template('happiness-rol.html', data=data)

@app.route('/happiness-gdp')
def happinessGdp():
    return render_template('happiness-gdp.html', data=data)
'''

@app.route('/happiness-terrorism')
def happinessTerrorism():
    return render_template('happiness-terrorism.html', data=data)

@app.route('/happiness-unemployment')
def happinessUnemployment():
    return render_template('happiness-unemployment.html', data=data)

@app.route('/happiness-uni')
def happinessUni():
    return render_template('happiness-uni.html', data=data)

@app.route('/terrorism-heatmap')
def terrorismHeatmap():
    return render_template('terrorism-heatmap.html', data=data)

@app.route('/university-heatmap')
def universityHeatmap():
    return render_template('colleges-heatmap.html', data=data)

if __name__ == "__main__":
    app.debug = True
    app.run()
