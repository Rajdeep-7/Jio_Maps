from flask import Flask, render_template,request,jsonify
import folium
import matplotlib.cm
import matplotlib as mpl
import pandas as pd
import numpy as np
from scipy.interpolate import griddata

app = Flask(__name__)

df = pd.read_csv('jio_dataset.csv')
print(df)

@app.route("/",methods=["GET","POST"])
def base():


    if request.method == "POST":
        Country = request.form.get("Country")
        State = request.form.get("State")
        Jio_Centre = request.form.get("Jio_Centre")
        Network_Technology = request.form.get("Network_Technology")
        print(Country)
        print(State)
        print(Jio_Centre)
        print(Network_Technology)
        action = request.form.get("action")

        #For Andaman & Nicobar region, 4G
        if action == "apply_filters" and State == "Andaman & Nicobar" and Jio_Centre == "Port Blair" and Network_Technology == '4G':

            n = 150  # number of points
            lat0 = df['Latitude'][0]
            lon0 = df['Longitude'][0]
            eps = 0.03
            v0 = df['4G'][0]

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
        
        #For Andaman & Nicobar region, 5G
        if action == "apply_filters" and State == "Andaman & Nicobar" and Jio_Centre == "Port Blair" and Network_Technology == '5G':

            n = 150  # number of points
            lat0 = df['Latitude'][0]
            lon0 = df['Longitude'][0]
            eps = 0.03
            v0 = df['5G'][0]


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
        
        #For Andhra Pradesh State
        if action == "apply_filters" and State == "Andhra Pradesh":
            #For 4G Network
            if Network_Technology == "4G" :
                if Jio_Centre == "Adilabad":
                    n = 150  
                    lat0 = df['Latitude'][1]
                    lon0 = df['Longitude'][1]
                    eps = 0.03
                    v0 = df['4G'][1]

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
                
                if Jio_Centre == "Adoni":
                    n = 150  
                    lat0 = df['Latitude'][2]
                    lon0 = df['Longitude'][2]
                    eps = 0.03
                    v0 = df['4G'][2]

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
                
                if Jio_Centre == "Anantapur":
                    n = 150  
                    lat0 = df['Latitude'][3]
                    lon0 = df['Longitude'][3]
                    eps = 0.03
                    v0 = df['4G'][3]

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
                
                if Jio_Centre == "Bhimavaram":
                    n = 150  
                    lat0 = df['Latitude'][4]
                    lon0 = df['Longitude'][4]
                    eps = 0.03
                    v0 = df['4G'][4]

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
                
                if Jio_Centre == "Chilakaluripet":
                    n = 150  
                    lat0 = df['Latitude'][5]
                    lon0 = df['Longitude'][5]
                    eps = 0.03
                    v0 = df['4G'][5]

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
                
                if Jio_Centre == "Chittoor":
                    n = 150  
                    lat0 = df['Latitude'][6]
                    lon0 = df['Longitude'][6]
                    eps = 0.03
                    v0 = df['4G'][6]

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
                
                if Jio_Centre == "Dharmavaram":
                    n = 150  
                    lat0 = df['Latitude'][7]
                    lon0 = df['Longitude'][7]
                    eps = 0.03
                    v0 = df['4G'][7]

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
                
                if Jio_Centre == "Eluru":
                    n = 150  
                    lat0 = df['Latitude'][8]
                    lon0 = df['Longitude'][8]
                    eps = 0.03
                    v0 = df['4G'][8]

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
                
                if Jio_Centre == "Hyderabad":
                    n = 150  
                    lat0 = df['Latitude'][9]
                    lon0 = df['Longitude'][9]
                    eps = 0.03
                    v0 = df['4G'][9]

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
                
                if Jio_Centre == "Gudivada":
                    n = 150  
                    lat0 = df['Latitude'][10]
                    lon0 = df['Longitude'][10]
                    eps = 0.03
                    v0 = df['4G'][10]

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
                
                if Jio_Centre == "Guntakal":
                    n = 150  
                    lat0 = df['Latitude'][11]
                    lon0 = df['Longitude'][11]
                    eps = 0.03
                    v0 = df['4G'][11]

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
                
                if Jio_Centre == "Guntur":
                    n = 150  
                    lat0 = df['Latitude'][12]
                    lon0 = df['Longitude'][12]
                    eps = 0.03
                    v0 = df['4G'][12]

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
                
                if Jio_Centre == "Hindupur":
                    n = 150  
                    lat0 = df['Latitude'][13]
                    lon0 = df['Longitude'][13]
                    eps = 0.03
                    v0 = df['4G'][13]

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
                
                if Jio_Centre == "Kadapa":
                    n = 150  
                    lat0 = df['Latitude'][14]
                    lon0 = df['Longitude'][14]
                    eps = 0.03
                    v0 = df['4G'][14]

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
                
                if Jio_Centre == "Kakinada":
                    n = 150  
                    lat0 = df['Latitude'][15]
                    lon0 = df['Longitude'][15]
                    eps = 0.03
                    v0 = df['4G'][15]

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
                
                if Jio_Centre == "Karimnagar":
                    n = 150  
                    lat0 = df['Latitude'][16]
                    lon0 = df['Longitude'][16]
                    eps = 0.03
                    v0 = df['4G'][16]

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
                
                if Jio_Centre == "Khammam":
                    n = 150  
                    lat0 = df['Latitude'][17]
                    lon0 = df['Longitude'][17]
                    eps = 0.03
                    v0 = df['4G'][17]

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
                
                if Jio_Centre == "Kurnool":
                    n = 150  
                    lat0 = df['Latitude'][18]
                    lon0 = df['Longitude'][18]
                    eps = 0.03
                    v0 = df['4G'][18]

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
                
                if Jio_Centre == "Secunderabad":
                    n = 150  
                    lat0 = df['Latitude'][32]
                    lon0 = df['Longitude'][32]
                    eps = 0.03
                    v0 = df['4G'][32]

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
                
                if Jio_Centre == "Srikakulam":
                    n = 150  
                    lat0 = df['Latitude'][33]
                    lon0 = df['Longitude'][33]
                    eps = 0.03
                    v0 = df['4G'][33]

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
                
                if Jio_Centre == "Suryapet":
                    n = 150  
                    lat0 = df['Latitude'][34]
                    lon0 = df['Longitude'][34]
                    eps = 0.03
                    v0 = df['4G'][34]

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
                
                if Jio_Centre == "Tirupati":
                    n = 150  
                    lat0 = df['Latitude'][38]
                    lon0 = df['Longitude'][38]
                    eps = 0.03
                    v0 = df['4G'][38]

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
                
                if Jio_Centre == "Vijayawada":
                    n = 150  
                    lat0 = df['Latitude'][39]
                    lon0 = df['Longitude'][39]
                    eps = 0.03
                    v0 = df['4G'][39]

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
                
                if Jio_Centre == "Visakhapatnam":
                    n = 150  
                    lat0 = df['Latitude'][40]
                    lon0 = df['Longitude'][40]
                    eps = 0.03
                    v0 = df['4G'][40]

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
                
                if Jio_Centre == "Warangal":
                    n = 150  
                    lat0 = df['Latitude'][44]
                    lon0 = df['Longitude'][44]
                    eps = 0.03
                    v0 = df['4G'][44]

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
                
            #For 5G Network   
            if Network_Technology == "5G" :
                if Jio_Centre == "Adilabad":
                    n = 150  
                    lat0 = df['Latitude'][1]
                    lon0 = df['Longitude'][1]
                    eps = 0.03
                    v0 = df['5G'][1]

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
                
                if Jio_Centre == "Adoni":
                    n = 150  
                    lat0 = df['Latitude'][2]
                    lon0 = df['Longitude'][2]
                    eps = 0.03
                    v0 = df['5G'][2]

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
                
                if Jio_Centre == "Anantapur":
                    n = 150  
                    lat0 = df['Latitude'][3]
                    lon0 = df['Longitude'][3]
                    eps = 0.03
                    v0 = df['5G'][3]

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
                
                if Jio_Centre == "Bhimavaram":
                    n = 150  
                    lat0 = df['Latitude'][4]
                    lon0 = df['Longitude'][4]
                    eps = 0.03
                    v0 = df['5G'][4]

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
                
                if Jio_Centre == "Chilakaluripet":
                    n = 150  
                    lat0 = df['Latitude'][5]
                    lon0 = df['Longitude'][5]
                    eps = 0.03
                    v0 = df['5G'][5]

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
                
                if Jio_Centre == "Chittoor":
                    n = 150  
                    lat0 = df['Latitude'][6]
                    lon0 = df['Longitude'][6]
                    eps = 0.03
                    v0 = df['5G'][6]

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
                
                if Jio_Centre == "Dharmavaram":
                    n = 150  
                    lat0 = df['Latitude'][7]
                    lon0 = df['Longitude'][7]
                    eps = 0.03
                    v0 = df['5G'][7]

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
                
                if Jio_Centre == "Eluru":
                    n = 150  
                    lat0 = df['Latitude'][8]
                    lon0 = df['Longitude'][8]
                    eps = 0.03
                    v0 = df['5G'][8]

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
                
                if Jio_Centre == "Hyderabad":
                    n = 150  
                    lat0 = df['Latitude'][9]
                    lon0 = df['Longitude'][9]
                    eps = 0.03
                    v0 = df['5G'][9]

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
                
                if Jio_Centre == "Gudivada":
                    n = 150  
                    lat0 = df['Latitude'][10]
                    lon0 = df['Longitude'][10]
                    eps = 0.03
                    v0 = df['5G'][10]

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
                
                if Jio_Centre == "Guntakal":
                    n = 150  
                    lat0 = df['Latitude'][11]
                    lon0 = df['Longitude'][11]
                    eps = 0.03
                    v0 = df['5G'][11]

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
                
                if Jio_Centre == "Guntur":
                    n = 150  
                    lat0 = df['Latitude'][12]
                    lon0 = df['Longitude'][12]
                    eps = 0.03
                    v0 = df['5G'][12]

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
                
                if Jio_Centre == "Hindupur":
                    n = 150  
                    lat0 = df['Latitude'][13]
                    lon0 = df['Longitude'][13]
                    eps = 0.03
                    v0 = df['5G'][13]

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
                
                if Jio_Centre == "Kadapa":
                    n = 150  
                    lat0 = df['Latitude'][14]
                    lon0 = df['Longitude'][14]
                    eps = 0.03
                    v0 = df['5G'][14]

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
                
                if Jio_Centre == "Kakinada":
                    n = 150  
                    lat0 = df['Latitude'][15]
                    lon0 = df['Longitude'][15]
                    eps = 0.03
                    v0 = df['5G'][15]

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
                
                if Jio_Centre == "Karimnagar":
                    n = 150  
                    lat0 = df['Latitude'][16]
                    lon0 = df['Longitude'][16]
                    eps = 0.03
                    v0 = df['5G'][16]

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
                
                if Jio_Centre == "Khammam":
                    n = 150  
                    lat0 = df['Latitude'][17]
                    lon0 = df['Longitude'][17]
                    eps = 0.03
                    v0 = df['5G'][17]

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
                
                if Jio_Centre == "Kurnool":
                    n = 150  
                    lat0 = df['Latitude'][18]
                    lon0 = df['Longitude'][18]
                    eps = 0.03
                    v0 = df['5G'][18]

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
                
                if Jio_Centre == "Secunderabad":
                    n = 150  
                    lat0 = df['Latitude'][32]
                    lon0 = df['Longitude'][32]
                    eps = 0.03
                    v0 = df['5G'][32]

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
                
                if Jio_Centre == "Srikakulam":
                    n = 150  
                    lat0 = df['Latitude'][33]
                    lon0 = df['Longitude'][33]
                    eps = 0.03
                    v0 = df['5G'][33]

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
                
                if Jio_Centre == "Suryapet":
                    n = 150  
                    lat0 = df['Latitude'][34]
                    lon0 = df['Longitude'][34]
                    eps = 0.03
                    v0 = df['5G'][34]

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
                
                if Jio_Centre == "Tirupati":
                    n = 150  
                    lat0 = df['Latitude'][38]
                    lon0 = df['Longitude'][38]
                    eps = 0.03
                    v0 = df['5G'][38]

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
                
                if Jio_Centre == "Vijayawada":
                    n = 150  
                    lat0 = df['Latitude'][39]
                    lon0 = df['Longitude'][39]
                    eps = 0.03
                    v0 = df['5G'][39]

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
                
                if Jio_Centre == "Visakhapatnam":
                    n = 150  
                    lat0 = df['Latitude'][40]
                    lon0 = df['Longitude'][40]
                    eps = 0.03
                    v0 = df['5G'][40]

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
                
                if Jio_Centre == "Warangal":
                    n = 150  
                    lat0 = df['Latitude'][44]
                    lon0 = df['Longitude'][44]
                    eps = 0.03
                    v0 = df['5G'][44]

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
                

        #For Arunachal Pradesh State
        if action == "apply_filters" and State == "Arunachal Pradesh":
            #For 4G Network
            if Network_Technology == "4G" :
                if Jio_Centre == "Pasighat":
                    n = 150  
                    lat0 = df['Latitude'][43]
                    lon0 = df['Longitude'][43]
                    eps = 0.03
                    v0 = df['4G'][43]

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
                
                if Jio_Centre == "Tawang":
                    n = 150  
                    lat0 = df['Latitude'][44]
                    lon0 = df['Longitude'][44]
                    eps = 0.03
                    v0 = df['4G'][44]

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

                if Jio_Centre == "Ziro":
                    n = 150  
                    lat0 = df['Latitude'][45]
                    lon0 = df['Longitude'][45]
                    eps = 0.03
                    v0 = df['4G'][45]

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
                
                if Jio_Centre == "Itanagar":
                    n = 150  
                    lat0 = df['Latitude'][46]
                    lon0 = df['Longitude'][46]
                    eps = 0.03
                    v0 = df['4G'][46]

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
                
            #For 5G Network
            if Network_Technology == "5G" :
                if Jio_Centre == "Pasighat":
                    n = 150  
                    lat0 = df['Latitude'][43]
                    lon0 = df['Longitude'][43]
                    eps = 0.03
                    v0 = df['5G'][43]

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
                
                if Jio_Centre == "Tawang":
                    n = 150  
                    lat0 = df['Latitude'][44]
                    lon0 = df['Longitude'][44]
                    eps = 0.03
                    v0 = df['5G'][44]

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

                if Jio_Centre == "Ziro":
                    n = 150  
                    lat0 = df['Latitude'][45]
                    lon0 = df['Longitude'][45]
                    eps = 0.03
                    v0 = df['5G'][45]

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
                
                if Jio_Centre == "Itanagar":
                    n = 150  
                    lat0 = df['Latitude'][46]
                    lon0 = df['Longitude'][46]
                    eps = 0.03
                    v0 = df['5G'][46]

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
        
        #For Assam State
        if action == "apply_filters" and State == "Assam":
            #For 4G Network
            if Network_Technology == "4G" :
                if Jio_Centre == "Dibrugarh":
                    n = 150  
                    lat0 = df['Latitude'][47]
                    lon0 = df['Longitude'][47]
                    eps = 0.03
                    v0 = df['4G'][47]

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
                
                if Jio_Centre == "Guwahati":
                    n = 150  
                    lat0 = df['Latitude'][48]
                    lon0 = df['Longitude'][48]
                    eps = 0.03
                    v0 = df['4G'][48]

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

                if Jio_Centre == "Nagaon":
                    n = 150  
                    lat0 = df['Latitude'][49]
                    lon0 = df['Longitude'][49]
                    eps = 0.03
                    v0 = df['4G'][49]

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
                
                if Jio_Centre == "Silchar":
                    n = 150  
                    lat0 = df['Latitude'][50]
                    lon0 = df['Longitude'][50]
                    eps = 0.03
                    v0 = df['4G'][50]

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
                
            #For 5G Network
            if Network_Technology == "5G" :
                if Jio_Centre == "Dibrugarh":
                    n = 150  
                    lat0 = df['Latitude'][47]
                    lon0 = df['Longitude'][47]
                    eps = 0.03
                    v0 = df['5G'][47]

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
                
                if Jio_Centre == "Guwahati":
                    n = 150  
                    lat0 = df['Latitude'][48]
                    lon0 = df['Longitude'][48]
                    eps = 0.03
                    v0 = df['5G'][48]

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

                if Jio_Centre == "Nagaon":
                    n = 150  
                    lat0 = df['Latitude'][49]
                    lon0 = df['Longitude'][49]
                    eps = 0.03
                    v0 = df['5G'][49]

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
                
                if Jio_Centre == "Silchar":
                    n = 150  
                    lat0 = df['Latitude'][50]
                    lon0 = df['Longitude'][50]
                    eps = 0.03
                    v0 = df['5G'][50]

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
                

        #For Bihar State
        if action == "apply_filters" and State == "Bihar":
            #For 4G Network
            if Network_Technology == "4G" :
                if Jio_Centre == "Begusarai":
                    n = 150  
                    lat0 = df['Latitude'][54]
                    lon0 = df['Longitude'][54]
                    eps = 0.03
                    v0 = df['4G'][54]

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
                
                if Jio_Centre == "Buxar":
                    n = 150  
                    lat0 = df['Latitude'][58]
                    lon0 = df['Longitude'][58]
                    eps = 0.03
                    v0 = df['4G'][58]

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

                if Jio_Centre == "Gaya":
                    n = 150  
                    lat0 = df['Latitude'][63]
                    lon0 = df['Longitude'][63]
                    eps = 0.03
                    v0 = df['4G'][63]

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
                
                if Jio_Centre == "Patna":
                    n = 150  
                    lat0 = df['Latitude'][72]
                    lon0 = df['Longitude'][72]
                    eps = 0.03
                    v0 = df['4G'][72]

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
                
            #For 5G Network
            if Network_Technology == "5G" :
                if Jio_Centre == "Begusarai":
                    n = 150  
                    lat0 = df['Latitude'][54]
                    lon0 = df['Longitude'][54]
                    eps = 0.03
                    v0 = df['5G'][54]

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
                
                if Jio_Centre == "Buxar":
                    n = 150  
                    lat0 = df['Latitude'][58]
                    lon0 = df['Longitude'][58]
                    eps = 0.03
                    v0 = df['5G'][58]

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

                if Jio_Centre == "Gaya":
                    n = 150  
                    lat0 = df['Latitude'][63]
                    lon0 = df['Longitude'][63]
                    eps = 0.03
                    v0 = df['5G'][63]

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
                
                if Jio_Centre == "Patna":
                    n = 150  
                    lat0 = df['Latitude'][72]
                    lon0 = df['Longitude'][72]
                    eps = 0.03
                    v0 = df['5G'][72]

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
        
        #For Chattisgarh State
        if action == "apply_filters" and State == "Chhattisgarh":
            #For 4G Network
            if Network_Technology == "4G" :
                if Jio_Centre == "Ambikapur":
                    n = 150  
                    lat0 = df['Latitude'][78]
                    lon0 = df['Longitude'][78]
                    eps = 0.03
                    v0 = df['4G'][78]

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
                
                if Jio_Centre == "Bilaspur":
                    n = 150  
                    lat0 = df['Latitude'][80]
                    lon0 = df['Longitude'][80]
                    eps = 0.03
                    v0 = df['4G'][80]

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

                if Jio_Centre == "Raigarh":
                    n = 150  
                    lat0 = df['Latitude'][84]
                    lon0 = df['Longitude'][84]
                    eps = 0.03
                    v0 = df['4G'][84]

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
                
                if Jio_Centre == "Raipur":
                    n = 150  
                    lat0 = df['Latitude'][85]
                    lon0 = df['Longitude'][85]
                    eps = 0.03
                    v0 = df['4G'][85]

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
                
            #For 5G Network
            if Network_Technology == "5G" :
                if Jio_Centre == "Ambikapur":
                    n = 150  
                    lat0 = df['Latitude'][78]
                    lon0 = df['Longitude'][78]
                    eps = 0.03
                    v0 = df['5G'][78]

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
                
                if Jio_Centre == "Bilaspur":
                    n = 150  
                    lat0 = df['Latitude'][80]
                    lon0 = df['Longitude'][80]
                    eps = 0.03
                    v0 = df['5G'][80]

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

                if Jio_Centre == "Raigarh":
                    n = 150  
                    lat0 = df['Latitude'][84]
                    lon0 = df['Longitude'][84]
                    eps = 0.03
                    v0 = df['5G'][84]

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
                
                if Jio_Centre == "Raipur":
                    n = 150  
                    lat0 = df['Latitude'][85]
                    lon0 = df['Longitude'][85]
                    eps = 0.03
                    v0 = df['5G'][85]

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
                
        
        #For Delhi State
        if action == "apply_filters" and State == "Delhi":
            #For 4G Network
            if Network_Technology == "4G" :
                if Jio_Centre == "Burari":
                    n = 150  
                    lat0 = df['Latitude'][88]
                    lon0 = df['Longitude'][88]
                    eps = 0.03
                    v0 = df['4G'][88]

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
                
                if Jio_Centre == "Hastsal":
                    n = 150  
                    lat0 = df['Latitude'][94]
                    lon0 = df['Longitude'][94]
                    eps = 0.03
                    v0 = df['4G'][94]

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

                if Jio_Centre == "Mandoli":
                    n = 150  
                    lat0 = df['Latitude'][97]
                    lon0 = df['Longitude'][97]
                    eps = 0.03
                    v0 = df['4G'][97]

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
                
                if Jio_Centre == "New Delhi":
                    n = 150  
                    lat0 = df['Latitude'][100]
                    lon0 = df['Longitude'][100]
                    eps = 0.03
                    v0 = df['4G'][100]

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
                
            #For 5G Network
            if Network_Technology == "5G" :
                if Jio_Centre == "Burari":
                    n = 150  
                    lat0 = df['Latitude'][88]
                    lon0 = df['Longitude'][88]
                    eps = 0.03
                    v0 = df['5G'][88]

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
                
                if Jio_Centre == "Hastsal":
                    n = 150  
                    lat0 = df['Latitude'][94]
                    lon0 = df['Longitude'][94]
                    eps = 0.03
                    v0 = df['5G'][94]

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

                if Jio_Centre == "Mustafabad":
                    n = 150  
                    lat0 = df['Latitude'][98]
                    lon0 = df['Longitude'][98]
                    eps = 0.03
                    v0 = df['5G'][98]

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
                
                if Jio_Centre == "New Delhi":
                    n = 150  
                    lat0 = df['Latitude'][100]
                    lon0 = df['Longitude'][100]
                    eps = 0.03
                    v0 = df['5G'][100]

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
        

        #For Gujarat State
        if action == "apply_filters" and State == "Gujarat":
            #For 4G Network
            if Network_Technology == "4G" :
                if Jio_Centre == "Ahmedabad":
                    n = 150  
                    lat0 = df['Latitude'][102]
                    lon0 = df['Longitude'][102]
                    eps = 0.03
                    v0 = df['4G'][102]

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
                
                if Jio_Centre == "Bharuch":
                    n = 150  
                    lat0 = df['Latitude'][105]
                    lon0 = df['Longitude'][105]
                    eps = 0.03
                    v0 = df['4G'][105]

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

                if Jio_Centre == "Bhavnagar":
                    n = 150  
                    lat0 = df['Latitude'][106]
                    lon0 = df['Longitude'][106]
                    eps = 0.03
                    v0 = df['4G'][106]

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
                
                if Jio_Centre == "Gandhinagar":
                    n = 150  
                    lat0 = df['Latitude'][111]
                    lon0 = df['Longitude'][111]
                    eps = 0.03
                    v0 = df['4G'][111]

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
                
                if Jio_Centre == "Jamnagar":
                    n = 150  
                    lat0 = df['Latitude'][114]
                    lon0 = df['Longitude'][114]
                    eps = 0.03
                    v0 = df['4G'][114]

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
                
                if Jio_Centre == "Rajkot":
                    n = 150  
                    lat0 = df['Latitude'][125]
                    lon0 = df['Longitude'][125]
                    eps = 0.03
                    v0 = df['4G'][125]

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

                if Jio_Centre == "Surat":
                    n = 150  
                    lat0 = df['Latitude'][126]
                    lon0 = df['Longitude'][126]
                    eps = 0.03
                    v0 = df['4G'][126]

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
                
                if Jio_Centre == "Vadodara":
                    n = 150  
                    lat0 = df['Latitude'][128]
                    lon0 = df['Longitude'][128]
                    eps = 0.03
                    v0 = df['4G'][128]

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
                
            #For 5G Network
            if Network_Technology == "5G" :
                if Jio_Centre == "Ahmedabad":
                    n = 150  
                    lat0 = df['Latitude'][102]
                    lon0 = df['Longitude'][102]
                    eps = 0.03
                    v0 = df['5G'][102]

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
                
                if Jio_Centre == "Bharuch":
                    n = 150  
                    lat0 = df['Latitude'][105]
                    lon0 = df['Longitude'][105]
                    eps = 0.03
                    v0 = df['5G'][105]

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

                if Jio_Centre == "Bhavnagar":
                    n = 150  
                    lat0 = df['Latitude'][106]
                    lon0 = df['Longitude'][106]
                    eps = 0.03
                    v0 = df['5G'][106]

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
                
                if Jio_Centre == "Gandhinagar":
                    n = 150  
                    lat0 = df['Latitude'][111]
                    lon0 = df['Longitude'][111]
                    eps = 0.03
                    v0 = df['5G'][111]

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
                
                if Jio_Centre == "Jamnagar":
                    n = 150  
                    lat0 = df['Latitude'][114]
                    lon0 = df['Longitude'][114]
                    eps = 0.03
                    v0 = df['5G'][114]

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
                
                if Jio_Centre == "Rajkot":
                    n = 150  
                    lat0 = df['Latitude'][125]
                    lon0 = df['Longitude'][125]
                    eps = 0.03
                    v0 = df['5G'][125]

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

                if Jio_Centre == "Surat":
                    n = 150  
                    lat0 = df['Latitude'][126]
                    lon0 = df['Longitude'][126]
                    eps = 0.03
                    v0 = df['5G'][126]

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
                
                if Jio_Centre == "Vadodara":
                    n = 150  
                    lat0 = df['Latitude'][128]
                    lon0 = df['Longitude'][128]
                    eps = 0.03
                    v0 = df['5G'][128]

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

        if action == "apply_filters" and State == "Haryana":
            #For 4G Network
            if Network_Technology == "4G" :
                if Jio_Centre == "Ambala":
                    n = 150  
                    lat0 = df['Latitude'][132]
                    lon0 = df['Longitude'][132]
                    eps = 0.03
                    v0 = df['4G'][132]

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
                
                if Jio_Centre == "Gurgaon":
                    n = 150  
                    lat0 = df['Latitude'][136]
                    lon0 = df['Longitude'][136]
                    eps = 0.03
                    v0 = df['4G'][136]

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

                if Jio_Centre == "Kaithal":
                    n = 150  
                    lat0 = df['Latitude'][140]
                    lon0 = df['Longitude'][140]
                    eps = 0.03
                    v0 = df['4G'][140]

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
                
                if Jio_Centre == "Panipat":
                    n = 150  
                    lat0 = df['Latitude'][144]
                    lon0 = df['Longitude'][144]
                    eps = 0.03
                    v0 = df['4G'][144]

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
                
                if Jio_Centre == "Rewari":
                    n = 150  
                    lat0 = df['Latitude'][145]
                    lon0 = df['Longitude'][145]
                    eps = 0.03
                    v0 = df['4G'][145]

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
                
                if Jio_Centre == "Rohtak":
                    n = 150  
                    lat0 = df['Latitude'][146]
                    lon0 = df['Longitude'][146]
                    eps = 0.03
                    v0 = df['4G'][146]

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

                if Jio_Centre == "Sonipat":
                    n = 150  
                    lat0 = df['Latitude'][148]
                    lon0 = df['Longitude'][148]
                    eps = 0.03
                    v0 = df['4G'][148]

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
                
                if Jio_Centre == "Thanesar":
                    n = 150  
                    lat0 = df['Latitude'][128]
                    lon0 = df['Longitude'][128]
                    eps = 0.03
                    v0 = df['4G'][128]

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
                
            #For 5G Network
            if Network_Technology == "5G" :
                if Jio_Centre == "Ambala":
                    n = 150  
                    lat0 = df['Latitude'][131]
                    lon0 = df['Longitude'][131]
                    eps = 0.03
                    v0 = df['5G'][131]

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
                
                if Jio_Centre == "Gurgaon":
                    n = 150  
                    lat0 = df['Latitude'][136]
                    lon0 = df['Longitude'][136]
                    eps = 0.03
                    v0 = df['5G'][136]

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

                if Jio_Centre == "Kaithal":
                    n = 150  
                    lat0 = df['Latitude'][140]
                    lon0 = df['Longitude'][140]
                    eps = 0.03
                    v0 = df['5G'][140]

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
                
                if Jio_Centre == "Panipat":
                    n = 150  
                    lat0 = df['Latitude'][144]
                    lon0 = df['Longitude'][144]
                    eps = 0.03
                    v0 = df['5G'][144]

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
                
                if Jio_Centre == "Rewari":
                    n = 150  
                    lat0 = df['Latitude'][145]
                    lon0 = df['Longitude'][145]
                    eps = 0.03
                    v0 = df['5G'][145]

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
                
                if Jio_Centre == "Rohtak":
                    n = 150  
                    lat0 = df['Latitude'][146]
                    lon0 = df['Longitude'][146]
                    eps = 0.03
                    v0 = df['5G'][146]

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

                if Jio_Centre == "Sonipat":
                    n = 150  
                    lat0 = df['Latitude'][148]
                    lon0 = df['Longitude'][148]
                    eps = 0.03
                    v0 = df['5G'][148]

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
                
                if Jio_Centre == "Thanesar":
                    n = 150  
                    lat0 = df['Latitude'][149]
                    lon0 = df['Longitude'][149]
                    eps = 0.03
                    v0 = df['5G'][149]

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
        
        #For Himachal Pradesh, 4G
        if action == "apply_filters" and State == "Himachal Pradesh" and Jio_Centre == "Shimla" and Network_Technology == '4G':

            n = 150  # number of points
            lat0 = df['Latitude'][151]
            lon0 = df['Longitude'][151]
            eps = 0.03
            v0 = df['4G'][151]

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
        
        #For Himachal Pradesh, 5G
        if action == "apply_filters" and State == "Himachal Pradesh" and Jio_Centre == "Shimla" and Network_Technology == '5G':

            n = 150  # number of points
            lat0 = df['Latitude'][151]
            lon0 = df['Longitude'][151]
            eps = 0.03
            v0 = df['5G'][151]


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
        
        #For Jammu & Kashmir State
        if action == "apply_filters" and State == "Jammu & Kashmir":
            #For 4G Network
            if Network_Technology == "4G" :
                if Jio_Centre == "Anantnag":
                    n = 150  
                    lat0 = df['Latitude'][152]
                    lon0 = df['Longitude'][152]
                    eps = 0.03
                    v0 = df['4G'][152]

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
                
                if Jio_Centre == "Jammu":
                    n = 150  
                    lat0 = df['Latitude'][155]
                    lon0 = df['Longitude'][155]
                    eps = 0.03
                    v0 = df['4G'][155]

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

                if Jio_Centre == "Srinagar":
                    n = 150  
                    lat0 = df['Latitude'][154]
                    lon0 = df['Longitude'][154]
                    eps = 0.03
                    v0 = df['4G'][154]

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
                
                    
            #For 5G Network
            if Network_Technology == "5G" :
                if Jio_Centre == "Anantnag":
                    n = 150  
                    lat0 = df['Latitude'][152]
                    lon0 = df['Longitude'][152]
                    eps = 0.03
                    v0 = df['5G'][152]

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
                
                if Jio_Centre == "Jammu":
                    n = 150  
                    lat0 = df['Latitude'][153]
                    lon0 = df['Longitude'][153]
                    eps = 0.03
                    v0 = df['5G'][153]

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

                if Jio_Centre == "Srinagar":
                    n = 150  
                    lat0 = df['Latitude'][154]
                    lon0 = df['Longitude'][154]
                    eps = 0.03
                    v0 = df['5G'][154]

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
                
                
        #For Jharkhand state
        if action == "apply_filters" and State == "Jharkhand":
            #For 4G Network
            if Network_Technology == "4G" :
                if Jio_Centre == "Adityapur":
                    n = 150  
                    lat0 = df['Latitude'][155]
                    lon0 = df['Longitude'][155]
                    eps = 0.03
                    v0 = df['4G'][155]

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
                
                if Jio_Centre == "Dhanbad":
                    n = 150  
                    lat0 = df['Latitude'][159]
                    lon0 = df['Longitude'][159]
                    eps = 0.03
                    v0 = df['4G'][159]

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

                if Jio_Centre == "Jamshedpur":
                    n = 150  
                    lat0 = df['Latitude'][162]
                    lon0 = df['Longitude'][162]
                    eps = 0.03
                    v0 = df['4G'][162]

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
                
                if Jio_Centre == "Ranchi":
                    n = 150  
                    lat0 = df['Latitude'][164]
                    lon0 = df['Longitude'][164]
                    eps = 0.03
                    v0 = df['4G'][164]

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
                
            #For 5G Network
            if Network_Technology == "5G" :
                if Jio_Centre == "Adityapur":
                    n = 150  
                    lat0 = df['Latitude'][155]
                    lon0 = df['Longitude'][155]
                    eps = 0.03
                    v0 = df['5G'][155]

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
                
                if Jio_Centre == "Dhanbad":
                    n = 150  
                    lat0 = df['Latitude'][159]
                    lon0 = df['Longitude'][159]
                    eps = 0.03
                    v0 = df['5G'][159]

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

                if Jio_Centre == "Jamshedpur":
                    n = 150  
                    lat0 = df['Latitude'][162]
                    lon0 = df['Longitude'][162]
                    eps = 0.03
                    v0 = df['5G'][162]

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
                
                if Jio_Centre == "Ranchi":
                    n = 150  
                    lat0 = df['Latitude'][164]
                    lon0 = df['Longitude'][164]
                    eps = 0.03
                    v0 = df['5G'][164]

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

        #For Karnataka State
        if action == "apply_filters" and State == "Karnataka":
            #For 4G Network
            if Network_Technology == "4G" :
                if Jio_Centre == "Belgaum":
                    n = 150  
                    lat0 = df['Latitude'][166]
                    lon0 = df['Longitude'][166]
                    eps = 0.03
                    v0 = df['4G'][166]

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
                
                if Jio_Centre == "Bengaluru":
                    n = 150  
                    lat0 = df['Latitude'][168]
                    lon0 = df['Longitude'][168]
                    eps = 0.03
                    v0 = df['4G'][168]

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

                if Jio_Centre == "Gulbarga":
                    n = 150  
                    lat0 = df['Latitude'][177]
                    lon0 = df['Longitude'][177]
                    eps = 0.03
                    v0 = df['4G'][177]

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
                
                if Jio_Centre == "Mangalore":
                    n = 150  
                    lat0 = df['Latitude'][183]
                    lon0 = df['Longitude'][183]
                    eps = 0.03
                    v0 = df['4G'][183]

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
                
                if Jio_Centre == "Mysore":
                    n = 150  
                    lat0 = df['Latitude'][184]
                    lon0 = df['Longitude'][184]
                    eps = 0.03
                    v0 = df['4G'][184]

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
                
                if Jio_Centre == "Raichur":
                    n = 150  
                    lat0 = df['Latitude'][185]
                    lon0 = df['Longitude'][185]
                    eps = 0.03
                    v0 = df['4G'][185]

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

                if Jio_Centre == "Shimoga":
                    n = 150  
                    lat0 = df['Latitude'][190]
                    lon0 = df['Longitude'][190]
                    eps = 0.03
                    v0 = df['4G'][190]

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
                
                if Jio_Centre == "Udupi":
                    n = 150  
                    lat0 = df['Latitude'][190]
                    lon0 = df['Longitude'][190]
                    eps = 0.03
                    v0 = df['4G'][190]

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
                
            #For 5G Network
            if Network_Technology == "5G" :
                if Jio_Centre == "Belgaum":
                    n = 150  
                    lat0 = df['Latitude'][166]
                    lon0 = df['Longitude'][166]
                    eps = 0.03
                    v0 = df['5G'][166]

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
                
                if Jio_Centre == "Bengaluru":
                    n = 150  
                    lat0 = df['Latitude'][168]
                    lon0 = df['Longitude'][168]
                    eps = 0.03
                    v0 = df['5G'][168]

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

                if Jio_Centre == "Gulbarga":
                    n = 150  
                    lat0 = df['Latitude'][177]
                    lon0 = df['Longitude'][177]
                    eps = 0.03
                    v0 = df['5G'][177]

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
                
                if Jio_Centre == "Mangalore":
                    n = 150  
                    lat0 = df['Latitude'][183]
                    lon0 = df['Longitude'][183]
                    eps = 0.03
                    v0 = df['5G'][183]

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
                
                if Jio_Centre == "Mysore":
                    n = 150  
                    lat0 = df['Latitude'][184]
                    lon0 = df['Longitude'][184]
                    eps = 0.03
                    v0 = df['5G'][184]

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
                
                if Jio_Centre == "Raichur":
                    n = 150  
                    lat0 = df['Latitude'][185]
                    lon0 = df['Longitude'][185]
                    eps = 0.03
                    v0 = df['5G'][185]

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

                if Jio_Centre == "Shimoga":
                    n = 150  
                    lat0 = df['Latitude'][188]
                    lon0 = df['Longitude'][188]
                    eps = 0.03
                    v0 = df['5G'][188]

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
                
                if Jio_Centre == "Udupi":
                    n = 150  
                    lat0 = df['Latitude'][190]
                    lon0 = df['Longitude'][190]
                    eps = 0.03
                    v0 = df['5G'][190]

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

        #For Kerala State
        if action == "apply_filters" and State == "Kerala":
            #For 4G Network
            if Network_Technology == "4G" :
                if Jio_Centre == "Kochi":
                    n = 150  
                    lat0 = df['Latitude'][192]
                    lon0 = df['Longitude'][192]
                    eps = 0.03
                    v0 = df['4G'][192]

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
                
                if Jio_Centre == "Kozhikode":
                    n = 150  
                    lat0 = df['Latitude'][194]
                    lon0 = df['Longitude'][194]
                    eps = 0.03
                    v0 = df['4G'][194]

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

                if Jio_Centre == "Thiruvananthapuram":
                    n = 150  
                    lat0 = df['Latitude'][196]
                    lon0 = df['Longitude'][196]
                    eps = 0.03
                    v0 = df['4G'][196]

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
                
                if Jio_Centre == "Thrissur":
                    n = 150  
                    lat0 = df['Latitude'][197]
                    lon0 = df['Longitude'][197]
                    eps = 0.03
                    v0 = df['4G'][197]

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
                
            #For 5G Network
            if Network_Technology == "5G" :
                if Jio_Centre == "Kochi":
                    n = 150  
                    lat0 = df['Latitude'][194]
                    lon0 = df['Longitude'][194]
                    eps = 0.03
                    v0 = df['5G'][194]

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
                
                if Jio_Centre == "Kozhikode":
                    n = 150  
                    lat0 = df['Latitude'][194]
                    lon0 = df['Longitude'][194]
                    eps = 0.03
                    v0 = df['5G'][194]

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

                if Jio_Centre == "Thiruvananthapuram":
                    n = 150  
                    lat0 = df['Latitude'][198]
                    lon0 = df['Longitude'][198]
                    eps = 0.03
                    v0 = df['5G'][198]

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
                
                if Jio_Centre == "Thrissur":
                    n = 150  
                    lat0 = df['Latitude'][197]
                    lon0 = df['Longitude'][197]
                    eps = 0.03
                    v0 = df['5G'][197]

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

        #For Madhya Pradesh State      
        if action == "apply_filters" and State == "Madhya Pradesh":
            #For 4G Network
            if Network_Technology == "4G" :
                if Jio_Centre == "Bhopal":
                    n = 150  
                    lat0 = df['Latitude'][200]
                    lon0 = df['Longitude'][200]
                    eps = 0.03
                    v0 = df['4G'][200]

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
                
                if Jio_Centre == "Gwalior":
                    n = 150  
                    lat0 = df['Latitude'][208]
                    lon0 = df['Longitude'][208]
                    eps = 0.03
                    v0 = df['4G'][208]

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

                if Jio_Centre == "Indore":
                    n = 150  
                    lat0 = df['Latitude'][210]
                    lon0 = df['Longitude'][210]
                    eps = 0.03
                    v0 = df['4G'][210]

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
                
                if Jio_Centre == "Jabalpur":
                    n = 150  
                    lat0 = df['Latitude'][211]
                    lon0 = df['Longitude'][211]
                    eps = 0.03
                    v0 = df['4G'][211]

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
                
                if Jio_Centre == "Khandwa":
                    n = 150  
                    lat0 = df['Latitude'][214]
                    lon0 = df['Longitude'][214]
                    eps = 0.03
                    v0 = df['4G'][214]

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
                
                if Jio_Centre == "Neemuch":
                    n = 150  
                    lat0 = df['Latitude'][218]
                    lon0 = df['Longitude'][218]
                    eps = 0.03
                    v0 = df['4G'][218]

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

                if Jio_Centre == "Ratlam":
                    n = 150  
                    lat0 = df['Latitude'][220]
                    lon0 = df['Longitude'][220]
                    eps = 0.03
                    v0 = df['4G'][220]

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
                
                if Jio_Centre == "Ujjain":
                    n = 150  
                    lat0 = df['Latitude'][228]
                    lon0 = df['Longitude'][228]
                    eps = 0.03
                    v0 = df['4G'][228]

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
                
            #For 5G Network
            if Network_Technology == "5G" :
                if Jio_Centre == "Bhopal":
                    n = 150  
                    lat0 = df['Latitude'][200]
                    lon0 = df['Longitude'][200]
                    eps = 0.03
                    v0 = df['5G'][200]

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
                
                if Jio_Centre == "Gwalior":
                    n = 150  
                    lat0 = df['Latitude'][210]
                    lon0 = df['Longitude'][210]
                    eps = 0.03
                    v0 = df['5G'][210]

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

                if Jio_Centre == "Indore":
                    n = 150  
                    lat0 = df['Latitude'][212]
                    lon0 = df['Longitude'][212]
                    eps = 0.03
                    v0 = df['5G'][212]

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
                
                if Jio_Centre == "Jabalpur":
                    n = 150  
                    lat0 = df['Latitude'][211]
                    lon0 = df['Longitude'][211]
                    eps = 0.03
                    v0 = df['5G'][211]

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
                
                if Jio_Centre == "Khandwa":
                    n = 150  
                    lat0 = df['Latitude'][214]
                    lon0 = df['Longitude'][214]
                    eps = 0.03
                    v0 = df['5G'][214]

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
                
                if Jio_Centre == "Neemuch":
                    n = 150  
                    lat0 = df['Latitude'][218]
                    lon0 = df['Longitude'][218]
                    eps = 0.03
                    v0 = df['5G'][218]

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

                if Jio_Centre == "Ratlam":
                    n = 150  
                    lat0 = df['Latitude'][220]
                    lon0 = df['Longitude'][220]
                    eps = 0.03
                    v0 = df['5G'][220]

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
                
                if Jio_Centre == "Ujjain":
                    n = 150  
                    lat0 = df['Latitude'][228]
                    lon0 = df['Longitude'][228]
                    eps = 0.03
                    v0 = df['5G'][228]

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


        #For Maharashtra State
        
        if action == "apply_filters" and State == "Maharashtra":
            #For 4G Network
            if Network_Technology == "4G" :
                if Jio_Centre == "Mumbai":
                    n = 150  
                    lat0 = df['Latitude'][244]
                    lon0 = df['Longitude'][244]
                    eps = 0.03
                    v0 = df['4G'][244]

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
                
                if Jio_Centre == "Mira Bhayander":
                    n = 150  
                    lat0 = df['Latitude'][252]
                    lon0 = df['Longitude'][252]
                    eps = 0.03
                    v0 = df['4G'][252]

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

                if Jio_Centre == "Nagpur":
                    n = 150  
                    lat0 = df['Latitude'][253]
                    lon0 = df['Longitude'][253]
                    eps = 0.03
                    v0 = df['4G'][253]

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
                
                if Jio_Centre == "Pune":
                    n = 150  
                    lat0 = df['Latitude'][263]
                    lon0 = df['Longitude'][263]
                    eps = 0.03
                    v0 = df['4G'][263]

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
                
                if Jio_Centre == "Satara":
                    n = 150  
                    lat0 = df['Latitude'][265]
                    lon0 = df['Longitude'][265]
                    eps = 0.03
                    v0 = df['4G'][265]

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
                
                if Jio_Centre == "Thane":
                    n = 150  
                    lat0 = df['Latitude'][267]
                    lon0 = df['Longitude'][267]
                    eps = 0.03
                    v0 = df['4G'][267]

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

                if Jio_Centre == "Ulhasnagar":
                    n = 150  
                    lat0 = df['Latitude'][269]
                    lon0 = df['Longitude'][269]
                    eps = 0.03
                    v0 = df['4G'][269]

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
                
                if Jio_Centre == "Yavatmal":
                    n = 150  
                    lat0 = df['Latitude'][272]
                    lon0 = df['Longitude'][272]
                    eps = 0.03
                    v0 = df['4G'][272]

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
                
            #For 5G Network
            if Network_Technology == "5G" :
                if Jio_Centre == "Mumbai":
                    n = 150  
                    lat0 = df['Latitude'][244]
                    lon0 = df['Longitude'][244]
                    eps = 0.03
                    v0 = df['5G'][244]

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
                
                if Jio_Centre == "Mira Bhayander":
                    n = 150  
                    lat0 = df['Latitude'][252]
                    lon0 = df['Longitude'][252]
                    eps = 0.03
                    v0 = df['5G'][252]

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

                if Jio_Centre == "Nagpur":
                    n = 150  
                    lat0 = df['Latitude'][253]
                    lon0 = df['Longitude'][253]
                    eps = 0.03
                    v0 = df['5G'][253]

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
                
                if Jio_Centre == "Pune":
                    n = 150  
                    lat0 = df['Latitude'][263]
                    lon0 = df['Longitude'][263]
                    eps = 0.03
                    v0 = df['5G'][263]

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
                
                if Jio_Centre == "Satara":
                    n = 150  
                    lat0 = df['Latitude'][265]
                    lon0 = df['Longitude'][265]
                    eps = 0.03
                    v0 = df['5G'][265]

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
                
                if Jio_Centre == "Thane":
                    n = 150  
                    lat0 = df['Latitude'][267]
                    lon0 = df['Longitude'][267]
                    eps = 0.03
                    v0 = df['5G'][267]

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

                if Jio_Centre == "Ulhasnagar":
                    n = 150  
                    lat0 = df['Latitude'][269]
                    lon0 = df['Longitude'][269]
                    eps = 0.03
                    v0 = df['5G'][269]

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
                
                if Jio_Centre == "Yavatmal":
                    n = 150  
                    lat0 = df['Latitude'][272]
                    lon0 = df['Longitude'][272]
                    eps = 0.03
                    v0 = df['5G'][272]

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


        #For Manipur State
        if action == "apply_filters" and State == "Manipur":
            #For 4G Network
            if Network_Technology == "4G" :
                if Jio_Centre == "Imphal":
                    n = 150  
                    lat0 = df['Latitude'][273]
                    lon0 = df['Longitude'][273]
                    eps = 0.03
                    v0 = df['4G'][273]

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
                
            #For 5G Network
            if Network_Technology == "5G" :
                if Jio_Centre == "Imphal":
                    n = 150  
                    lat0 = df['Latitude'][273]
                    lon0 = df['Longitude'][273]
                    eps = 0.03
                    v0 = df['5G'][273]

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

        #For Meghalaya State
        if action == "apply_filters" and State == "Meghalaya":
            #For 4G Network
            if Network_Technology == "4G" :
                if Jio_Centre == "Shillong":
                    n = 150  
                    lat0 = df['Latitude'][274]
                    lon0 = df['Longitude'][274]
                    eps = 0.03
                    v0 = df['4G'][274]

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
                
            #For 5G Network
            if Network_Technology == "5G" :
                if Jio_Centre == "Shillong":
                    n = 150  
                    lat0 = df['Latitude'][274]
                    lon0 = df['Longitude'][274]
                    eps = 0.03
                    v0 = df['5G'][274]

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

        #For Mizoram State
        if action == "apply_filters" and State == "Mizoram":
            #For 4G Network
            if Network_Technology == "4G" :
                if Jio_Centre == "Aizawl":
                    n = 150  
                    lat0 = df['Latitude'][275]
                    lon0 = df['Longitude'][275]
                    eps = 0.03
                    v0 = df['4G'][275]

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
                
            #For 5G Network
            if Network_Technology == "5G" :
                if Jio_Centre == "Aizawl":
                    n = 150  
                    lat0 = df['Latitude'][275]
                    lon0 = df['Longitude'][275]
                    eps = 0.03
                    v0 = df['5G'][275]

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


        #For Nagaland State
        if action == "apply_filters" and State == "Nagaland":
            #For 4G Network
            if Network_Technology == "4G" :
                if Jio_Centre == "Dimapur":
                    n = 150  
                    lat0 = df['Latitude'][276]
                    lon0 = df['Longitude'][276]
                    eps = 0.03
                    v0 = df['4G'][276]

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
                
            #For 5G Network
            if Network_Technology == "5G" :
                if Jio_Centre == "Dimapur":
                    n = 150  
                    lat0 = df['Latitude'][276]
                    lon0 = df['Longitude'][276]
                    eps = 0.03
                    v0 = df['5G'][276]

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

        #For Odisha State
        if action == "apply_filters" and State == "Odisha":
            #For 4G Network
            if Network_Technology == "4G" :
                if Jio_Centre == "Bhadrak":
                    n = 150  
                    lat0 = df['Latitude'][279]
                    lon0 = df['Longitude'][279]
                    eps = 0.03
                    v0 = df['4G'][279]

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
                
                if Jio_Centre == "Bhubaneswar":
                    n = 150  
                    lat0 = df['Latitude'][280]
                    lon0 = df['Longitude'][280]
                    eps = 0.03
                    v0 = df['4G'][280]

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

                if Jio_Centre == "Cuttack":
                    n = 150  
                    lat0 = df['Latitude'][282]
                    lon0 = df['Longitude'][282]
                    eps = 0.03
                    v0 = df['4G'][282]

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
                
                if Jio_Centre == "Puri":
                    n = 150  
                    lat0 = df['Latitude'][283]
                    lon0 = df['Longitude'][283]
                    eps = 0.03
                    v0 = df['4G'][283]

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
                
            #For 5G Network
            if Network_Technology == "5G" :
                if Jio_Centre == "Bhadrak":
                    n = 150  
                    lat0 = df['Latitude'][279]
                    lon0 = df['Longitude'][279]
                    eps = 0.03
                    v0 = df['5G'][279]

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
                
                if Jio_Centre == "Bhubaneswar":
                    n = 150  
                    lat0 = df['Latitude'][280]
                    lon0 = df['Longitude'][280]
                    eps = 0.03
                    v0 = df['5G'][280]

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

                if Jio_Centre == "Cuttack":
                    n = 150  
                    lat0 = df['Latitude'][282]
                    lon0 = df['Longitude'][282]
                    eps = 0.03
                    v0 = df['5G'][282]

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
                
                if Jio_Centre == "Puri":
                    n = 150  
                    lat0 = df['Latitude'][283]
                    lon0 = df['Longitude'][283]
                    eps = 0.03
                    v0 = df['5G'][283]

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

        #For Punjab State
        if action == "apply_filters" and State == "Punjab":
            #For 4G Network
            if Network_Technology == "4G" :
                if Jio_Centre == "Amritsar":
                    n = 150  
                    lat0 = df['Latitude'][290]
                    lon0 = df['Longitude'][290]
                    eps = 0.03
                    v0 = df['4G'][290]

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
                
                if Jio_Centre == "Jalandhar":
                    n = 150  
                    lat0 = df['Latitude'][296]
                    lon0 = df['Longitude'][296]
                    eps = 0.03
                    v0 = df['4G'][296]

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

                if Jio_Centre == "Ludhiana":
                    n = 150  
                    lat0 = df['Latitude'][298]
                    lon0 = df['Longitude'][298]
                    eps = 0.03
                    v0 = df['4G'][298]

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
                
                if Jio_Centre == "Pathankot":
                    n = 150  
                    lat0 = df['Latitude'][302]
                    lon0 = df['Longitude'][302]
                    eps = 0.03
                    v0 = df['4G'][302]

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
                
            #For 5G Network
            if Network_Technology == "5G" :
                if Jio_Centre == "Amritsar":
                    n = 150  
                    lat0 = df['Latitude'][290]
                    lon0 = df['Longitude'][290]
                    eps = 0.03
                    v0 = df['5G'][290]

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
                
                if Jio_Centre == "Jalandhar":
                    n = 150  
                    lat0 = df['Latitude'][296]
                    lon0 = df['Longitude'][296]
                    eps = 0.03
                    v0 = df['5G'][296]

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

                if Jio_Centre == "Ludhiana":
                    n = 150  
                    lat0 = df['Latitude'][298]
                    lon0 = df['Longitude'][298]
                    eps = 0.03
                    v0 = df['5G'][298]

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
                
                if Jio_Centre == "Pathankot":
                    n = 150  
                    lat0 = df['Latitude'][302]
                    lon0 = df['Longitude'][302]
                    eps = 0.03
                    v0 = df['5G'][302]

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

        #For Rajasthan State
        if action == "apply_filters" and State == "Rajasthan":
            #For 4G Network
            if Network_Technology == "4G" :
                if Jio_Centre == "Ajmer":
                    n = 150  
                    lat0 = df['Latitude'][305]
                    lon0 = df['Longitude'][305]
                    eps = 0.03
                    v0 = df['4G'][305]

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
                
                if Jio_Centre == "Bikaner":
                    n = 150  
                    lat0 = df['Latitude'][313]
                    lon0 = df['Longitude'][313]
                    eps = 0.03
                    v0 = df['4G'][313]

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

                if Jio_Centre == "Jaipur":
                    n = 150  
                    lat0 = df['Latitude'][322]
                    lon0 = df['Longitude'][322]
                    eps = 0.03
                    v0 = df['4G'][322]

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
                
                if Jio_Centre == "Jodhpur":
                    n = 150  
                    lat0 = df['Latitude'][324]
                    lon0 = df['Longitude'][324]
                    eps = 0.03
                    v0 = df['4G'][324]

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
                
                if Jio_Centre == "Kota":
                    n = 150  
                    lat0 = df['Latitude'][326]
                    lon0 = df['Longitude'][326]
                    eps = 0.03
                    v0 = df['4G'][326]

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
                
                if Jio_Centre == "Pali":
                    n = 150  
                    lat0 = df['Latitude'][328]
                    lon0 = df['Longitude'][328]
                    eps = 0.03
                    v0 = df['4G'][328]

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

                if Jio_Centre == "Sikar":
                    n = 150  
                    lat0 = df['Latitude'][330]
                    lon0 = df['Longitude'][330]
                    eps = 0.03
                    v0 = df['4G'][330]

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
                
                if Jio_Centre == "Udaipur":
                    n = 150  
                    lat0 = df['Latitude'][333]
                    lon0 = df['Longitude'][333]
                    eps = 0.03
                    v0 = df['4G'][333]

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
                
            #For 5G Network
            if Network_Technology == "5G" :
                if Jio_Centre == "Ajmer":
                    n = 150  
                    lat0 = df['Latitude'][305]
                    lon0 = df['Longitude'][305]
                    eps = 0.03
                    v0 = df['5G'][305]

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
                
                if Jio_Centre == "Bikaner":
                    n = 150  
                    lat0 = df['Latitude'][313]
                    lon0 = df['Longitude'][313]
                    eps = 0.03
                    v0 = df['5G'][313]

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

                if Jio_Centre == "Jaipur":
                    n = 150  
                    lat0 = df['Latitude'][322]
                    lon0 = df['Longitude'][322]
                    eps = 0.03
                    v0 = df['5G'][322]

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
                
                if Jio_Centre == "Jodhpur":
                    n = 150  
                    lat0 = df['Latitude'][324]
                    lon0 = df['Longitude'][324]
                    eps = 0.03
                    v0 = df['5G'][324]

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
                
                if Jio_Centre == "Kota":
                    n = 150  
                    lat0 = df['Latitude'][326]
                    lon0 = df['Longitude'][326]
                    eps = 0.03
                    v0 = df['5G'][326]

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
                
                if Jio_Centre == "Pali":
                    n = 150  
                    lat0 = df['Latitude'][328]
                    lon0 = df['Longitude'][328]
                    eps = 0.03
                    v0 = df['5G'][328]

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

                if Jio_Centre == "Sikar":
                    n = 150  
                    lat0 = df['Latitude'][330]
                    lon0 = df['Longitude'][330]
                    eps = 0.03
                    v0 = df['5G'][330]

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
                
                if Jio_Centre == "Udaipur":
                    n = 150  
                    lat0 = df['Latitude'][333]
                    lon0 = df['Longitude'][333]
                    eps = 0.03
                    v0 = df['5G'][333]

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
    app.run(debug=True,port=5002)
