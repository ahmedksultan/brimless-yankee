from flask import Flask, render_template
import urllib
import os
import data as dataModule
data = {
    "globalTerrorism": dataModule.globalTerrorism,
    "happiness": dataModule.happiness,
    "humanFreedomIndex": dataModule.humanFreedomIndex,
    "unemlployment": dataModule.unemployment,
    "universityRankings": dataModule.universityRankings
}


app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/happiness-gdp') 
def happinessGdp():
    return render_template('happiness-gdp.html', data=data)


if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0')
