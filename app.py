from flask import Flask, render_template, request, redirect, url_for, jsonify
import json, subprocess, os, csv

app = Flask(__name__)

# ← Adjust these paths for your setup →
WIFIINFOVIEW_EXE = r"E:\programs\Wifi\wifiinfoview-x64\WifiInfoView.exe"
EXPORT_CSV       = r"E:\programs\Wifi\wifiinfoview-x64\wifi.csv"
MAPPING_FILE     = "ssid_mapping.json"

def load_mapping():
    if not os.path.exists(MAPPING_FILE):
        return {}
    with open(MAPPING_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_mapping(mapping):
    with open(MAPPING_FILE, "w", encoding="utf-8") as f:
        json.dump(mapping, f, indent=4)

def scan_and_inject(mapping):
    # 1) Export
    subprocess.run([WIFIINFOVIEW_EXE, "/scomma", EXPORT_CSV], check=True)
    # 2) Read & inject
    with open(EXPORT_CSV, newline='', encoding='utf-8') as inf:
        reader  = csv.DictReader(inf)
        columns = reader.fieldnames
        networks = []
        for row in reader:
            orig = row.get("SSID","").strip()
            mac  = row.get("MAC Address","").strip().lower()
            hidden = (orig == "")
            mapped = hidden and (mac in mapping)
            if mapped:
                row["SSID"] = mapping[mac]
            # flags
            row["__hidden"] = hidden
            row["__mapped"] = mapped
            row["__mac"]    = mac
            networks.append(row)
    return columns, networks

@app.route("/", methods=["GET"])
def index():
    # Initial scan for page-render
    mapping = load_mapping()
    columns, networks = scan_and_inject(mapping)
    # find RSSI column index
    try:
        rssi_index = columns.index("RSSI")
    except ValueError:
        rssi_index = 0
    return render_template(
        "index.html",
        columns=columns,
        networks=networks,
        rssi_index=rssi_index
    )

@app.route("/api/networks", methods=["GET"])
def api_networks():
    mapping = load_mapping()
    columns, networks = scan_and_inject(mapping)
    return jsonify(columns=columns, networks=networks)

@app.route("/update_mapping", methods=["POST"])
def update_mapping():
    data = request.get_json() or {}
    mac  = data.get("mac","").strip().lower()
    name = data.get("name","").strip()
    if not mac or not name:
        return jsonify(status="error", error="Missing MAC or name"), 400

    mapping = load_mapping()
    mapping[mac] = name
    save_mapping(mapping)
    return jsonify(status="ok")

if __name__ == "__main__":
    app.run(debug=True)
