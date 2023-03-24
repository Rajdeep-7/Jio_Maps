from flask import Flask, render_template,request,jsonify
import folium
import matplotlib.cm
import matplotlib as mpl
import pandas as pd
import numpy as np
from scipy.interpolate import griddata
from flask_sqlalchemy import SQLAlchemy
import sqlite3


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
app.app_context().push()


class Jio(db.Model):
    __tablename__ = 'JIO_MAPS'
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(50))
    state = db.Column(db.String(50))
    jiocentre = db.Column(db.String(100))
    longitude = db.Column(db.Float)
    lattiude = db.Column(db.Float)
    fourGtech = db.Column(db.Float)
    fiveGtech = db.Column(db.Float)
    

JIO_MAPS = Jio.query.all()


@app.route("/",methods=["GET","POST"])
def base():
    jio_maps_query = Jio.query.filter_by(country="India", state="Maharashtra", jiocentre="Pune")
    print(jio_maps_query)
    result = jio_maps_query.all()
    if request.method == "POST":
        Country = request.form.get('Country')
        State = request.form.get("State")
        Jio_Centre = request.form.get("Jio_Centre")
        Network_Technology = request.form.get("Network_Technology")
        print(Country)
        print(State)
        print(Jio_Centre)
        print(Network_Technology)
        action = request.form.get("action")

        #For 4G network
        if action == "apply_filters" and Network_Technology == '4G':
            Country = request.form.get('Country')
            State = request.form.get("State")
            Jio_Centre = request.form.get("Jio_Centre")
            Network_Technology = request.form.get("Network_Technology")
            
            jio_maps_query = Jio.query.filter_by(country="India", state="Maharashtra", jiocentre="Pune")
            print(jio_maps_query)
            result = jio_maps_query.all()
            for row in result:
                longitude = row.longitude
                lattiude = row.lattiude
                fourGtech = row.fourGtech
                print(row)

            n = 150  # number of points
            lon0 = longitude
            lat0 = lattiude
            eps = 0.03
            v0 = fourGtech

            # generating values
            lat = np.random.normal(lat0, eps, n)
            lon = np.random.normal(lon0, eps, n)
            value = np.random.uniform(v0, abs(v0), n)

            # set up the grid
            step = 0.01
            xi, yi = np.meshgrid(
                np.arange(lat.min() - step / 2, lat.max() + step / 2, step),
                np.arange(lon.min() - step / 2, lon.max() + step / 2, step),
            )

            # interpolate and normalize values
            zi = griddata((lat, lon), value, (xi, yi), method='linear')
            zi /= np.nanmax(zi)
            g = np.stack([
                xi.flatten(),
                yi.flatten(),
                zi.flatten(),
            ], axis=1)

            # geo_json returns a single square
            def geo_json(lat, lon, value, step):
                cmap = mpl.cm.RdBu
                return {
                    "type": "FeatureCollection",
                    "features": [
                        {
                            "type": "Feature",
                            "properties": {
                                'color': 'white',
                                'weight': 1,
                                'fillColor': mpl.colors.to_hex(cmap(value)),
                                'fillOpacity': 0.5,
                            },
                            "geometry": {
                                "type": "Polygon",
                                "coordinates": [[
                                    [lon - step / 2, lat - step / 2],
                                    [lon - step / 2, lat + step / 2],
                                    [lon + step / 2, lat + step / 2],
                                    [lon + step / 2, lat - step / 2],
                                    [lon - step / 2, lat - step / 2],
                                ]]}}]}

            # generating a map...
            m = folium.Map(location=[lat0, lon0], zoom_start=9)

            # ...with squares...
            for gi in g:
                if ~np.isnan(gi[2]):
                    folium.GeoJson(geo_json(gi[0], gi[1], gi[2], step),
                                lambda x: x['properties']).add_to(m)
            map_html = m.get_root().render()
            return render_template('indexu.html',map_html=map_html)
        
        #For 5G network
        if action == "apply_filters" and Network_Technology == '5G':
            
            #filter_values = df.loc[(df["State"]==State) & (df["Jio_Centre"]==Jio_Centre)]

            n = 150  # number of points
            lat0 = filter_values['Latitude'].values[0]
            lon0 = filter_values['Longitude'].values[0]
            eps = 0.03
            v0 = filter_values['5G'].values[0]

            # generating values
            lat = np.random.normal(lat0, eps, n)
            lon = np.random.normal(lon0, eps, n)
            value = np.random.uniform(v0, abs(v0), n)

            # set up the grid
            step = 0.01
            xi, yi = np.meshgrid(
                np.arange(lat.min() - step / 2, lat.max() + step / 2, step),
                np.arange(lon.min() - step / 2, lon.max() + step / 2, step),
            )

            # interpolate and normalize values
            zi = griddata((lat, lon), value, (xi, yi), method='linear')
            zi /= np.nanmax(zi)
            g = np.stack([
                xi.flatten(),
                yi.flatten(),
                zi.flatten(),
            ], axis=1)

            # geo_json returns a single square
            def geo_json(lat, lon, value, step):
                cmap = mpl.cm.RdBu
                return {
                    "type": "FeatureCollection",
                    "features": [
                        {
                            "type": "Feature",
                            "properties": {
                                'color': 'white',
                                'weight': 1,
                                'fillColor': mpl.colors.to_hex(cmap(value)),
                                'fillOpacity': 0.5,
                            },
                            "geometry": {
                                "type": "Polygon",
                                "coordinates": [[
                                    [lon - step / 2, lat - step / 2],
                                    [lon - step / 2, lat + step / 2],
                                    [lon + step / 2, lat + step / 2],
                                    [lon + step / 2, lat - step / 2],
                                    [lon - step / 2, lat - step / 2],
                                ]]}}]}

            # generating a map...
            m = folium.Map(location=[lat0, lon0], zoom_start=9)

            # ...with squares...
            for gi in g:
                if ~np.isnan(gi[2]):
                    folium.GeoJson(geo_json(gi[0], gi[1], gi[2], step),
                                lambda x: x['properties']).add_to(m)
            map_html = m.get_root().render()
            return render_template('indexu.html',map_html=map_html)
        
        else:
            return "NO SUCH MAP PRESESNT"
        

    else:
        n = 250  # number of points
        lat0 = 23.5120
        lon0 = 80.3290
        eps = 0.1
        v_min, v_max = 0, 300  # min, max values

        # generating values
        lat = np.random.normal(lat0, eps, n)
        lon = np.random.normal(lon0, eps, n)
        value = np.random.uniform(v_min, v_max, n)

        # set up the grid
        step = 0.01
        xi, yi = np.meshgrid(
            np.arange(lat.min() - step / 2, lat.max() + step / 2, step),
            np.arange(lon.min() - step / 2, lon.max() + step / 2, step),
        )

        # interpolate and normalize values
        zi = griddata((lat, lon), value, (xi, yi), method='linear')
        zi /= np.nanmax(zi)
        g = np.stack([
            xi.flatten(),
            yi.flatten(),
            zi.flatten(),
        ], axis=1)

        # geo_json returns a single square
        def geo_json(lat, lon, value, step):
            cmap = mpl.cm.RdBu
            return {
                "type": "FeatureCollection",
                "features": [
                    {
                        "type": "Feature",
                        "properties": {
                            'color': 'white',
                            'weight': 1,
                            'fillColor': mpl.colors.to_hex(cmap(value)),
                            'fillOpacity': 0.5,
                        },
                        "geometry": {
                            "type": "Polygon",
                            "coordinates": [[
                                [lon - step / 2, lat - step / 2],
                                [lon - step / 2, lat + step / 2],
                                [lon + step / 2, lat + step / 2],
                                [lon + step / 2, lat - step / 2],
                                [lon - step / 2, lat - step / 2],
                            ]]}}]}

        # generating a map...
        m = folium.Map(location=[lat0, lon0], zoom_start=9)

        # ...with squares...
        for gi in g:
            if ~np.isnan(gi[2]):
                folium.GeoJson(geo_json(gi[0], gi[1], gi[2], step),
                            lambda x: x['properties']).add_to(m)
        map_html = m.get_root().render()
        return render_template('indexu.html', map_html=map_html)
        


if __name__ == "__main__":
    app.run(debug=True,port=5004)
