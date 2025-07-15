## IP Geolocation App

This is a simple web application built with **Flask** that allows users to enter an IP address and retrieve geolocation information using the `ip-api.com` service. The location is displayed on an interactive map powered by **Folium (Leaflet.js)**, along with details like city, region, ISP, and more.

---

## Features

* Enter any IPv4 or IPv6 address
* View city, region, country, ISP, and organization details
* See the location on an interactive map (Folium + Leaflet.js)
* Fully responsive layout with modern UI

---

## Tech Behind The Project

* **Backend:** Flask (Python)
* **Frontend:** HTML, CSS, JavaScript (for Leaflet map)
* **Map Rendering:** [Folium](https://python-visualization.github.io/folium/)
* **IP Data Provider:** [ip-api.com](https://ip-api.com/)

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/DragonSenseiGuy/ip-geolocation.git
cd ip-geolocation
```

### 2. Create a virtual environment and install dependencies

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip3 install -r requirements.txt
```

### 3. Create a `.env` file

```env
APP_SECRET_KEY=your_flask_secret_key
```

### 4. Run the app

```bash
python3 main.py
```

Then open `http://localhost:5000/ip` in your browser.

---

## Project Structure

```
ip-geolocation/
├── static/
│   └── ip.css
├── templates/
│   └── index.html
├── main.py
├── .env
├──README.md
└── LICENSE
```

---

## Notes

* The app uses `http://ip-api.com/json/{ip}` — which is **free and doesn't require an API key** for light use.
* Map tiles are loaded via [OpenStreetMap](https://www.openstreetmap.org) and rendered using Folium.

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

## Credits

* [ip-api.com](https://ip-api.com/) — IP geolocation service
* [Folium](https://python-visualization.github.io/folium/) — Mapping library
* [Flask](https://flask.palletsprojects.com/) — Python web framework

