from flask import Flask, render_template, request, redirect, url_for, session
import requests
import folium
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("APP_SECRET_KEY")

@app.route("/ip", methods=["GET", "POST"])
def ip_lookup():
    if request.method == "POST":
        ip = request.form.get("ip")

        try:
            response = requests.get(f"http://ip-api.com/json/{ip}")
            if response.status_code == 200:
                data = response.json()
                lat=data["lat"]
                lon=data["lon"]
                map_obj = folium.Map(location=[lat, lon], zoom_start=10)
                folium.Marker([lat, lon], popup=f"IP: {ip}").add_to(map_obj)
                map_html = map_obj._repr_html_()
                session['map'] = map_html
                session['data'] = data
        except Exception as e:
            session['data'] = {"ip": ip, "error": str(e)}
            session['map'] = None

        return redirect(url_for("ip_lookup"))

    data = session.pop("data", None)
    map_html = session.pop("map", None)

    return render_template("index.html", data=data, map_html=map_html)

if __name__=="__main__":
    app.run()
