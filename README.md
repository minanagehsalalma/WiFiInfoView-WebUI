
# WIFI-INFO-VIEW Interactive GUI

An **interactive, web-based front-end** for NirSoft’s amazing [WifiInfoView](https://www.nirsoft.net/utils/wifi_information_view.html) utility. This project wraps the original `.exe` to provide a modern, browser-based interface for monitoring Wi-Fi networks.
<img width="1897" height="865" alt="image" src="https://github.com/user-attachments/assets/de2cab4d-d386-4a7e-9194-c0b82f39accc" />
-----

## ✨ Features

  * **Modern UI**: A full-width, searchable, sortable, and paginated table of all network data exported by WifiInfoView.
  * **Smart Sorting**: Defaults to sorting by RSSI (signal strength) in descending order, showing the strongest networks first.
  * **Flexible Viewing**: Show all entries by default, with an "All" option available for pagination.
  * **Hidden SSID Naming**: Double-click any hidden SSID cell to assign a friendly, memorable name. 🟩
  * **Persistent Mappings**: Your custom SSID names are saved in `ssid_mapping.json`, acting as a simple "database."
  * **Visual Highlighting**:
      * Newly mapped SSIDs are marked with a ⭐ and a light-yellow background.
      * User-added rows get a distinct light-blue background.
  * **Auto-Refresh**: Automatically refresh the network list at a chosen interval without reloading the page.
  * **Manual Rescan**: A "Rescan Now" button for on-demand network scans.
  * **JSON API**: Includes a `/api/networks` endpoint, allowing you to build your own custom scripts or front-ends.

-----

## 🏗️ Motivation

While WifiInfoView is a fantastic portable tool for inspecting Wi-Fi networks, it is closed-source and cannot be extended. This GUI wrapper was created to:

1.  **Mark hidden SSIDs** by name and have those names persist between sessions.
<img width="477" height="243" alt="Enter-SSID" src="https://github.com/user-attachments/assets/944b2e9d-c4eb-4e7f-b721-77cdc85cfc1b" />

2.  **Interact** with live scan data in your browser: search, filter, sort, and page through the results.
3.  **Auto-refresh** continuously without losing your state or reloading the entire page.

-----

## ⚙️ Requirements

  * **OS**: Windows 10/11 (required for `WifiInfoView.exe`)
  * **Python**: Version 3.7+
  * **PIP**: Python package manager
  * **Browser**: A modern browser like Chrome, Firefox, or Edge.

### Python Dependencies

The application relies on the Flask web framework. You can install it using pip:

```bash
pip install flask
```

-----

## 🚀 Installation & Usage

Follow these steps to get the application running.

### 1\. Clone the Repository

```bash
git clone https://github.com/minanagehsalalma/WiFiInfoView-WebUI.git
cd WiFiInfoView-WebUI
```

### 2\. Configure Paths

Before running, you must edit `app.py` and set the correct paths for the `WifiInfoView.exe` utility and the temporary CSV file it generates.

```python
# Edit these paths in app.py
WIFIINFOVIEW_EXE = r"C:\path\to\your\WifiInfoView.exe"
EXPORT_CSV       = r"C:\path\to\your\wifi.csv"
```

### 3\. Create Mapping File

Create an empty JSON file named `ssid_mapping.json` in the same directory as `app.py`. This file will store your custom names for hidden SSIDs.

```json
{}
```

### 4\. Run the App

Start the Flask server from your terminal:

```bash
python app.py
```

### 5\. Open in Browser

Once the server is running, open your web browser and navigate to:

http://127.0.0.1:5000/

You should now see the interactive Wi-Fi network table.

## 📡 API Endpoint

* **GET** `/api/networks`
  Returns JSON:

  ```json
  {
    "columns": [ "SSID", "MAC Address", "Signal Quality", "...", "RSSI", … ],
    "networks": [
      { "SSID":"MySSID", "MAC Address":"aa-bb-…", "Signal Quality":"85", "…": "...", "__hidden":false, "__mapped":false, "__mac":"aa-bb-…"},
      …
    ]
  }
  ```

You can use this endpoint to build your own scripts or integrations.

---

## 🎨 Customization

* **Columns & Sorting**
  Every column from WifiInfoView’s CSV is displayed. Change the default sort in `app.py` or in the DataTables `order` config in `index.html`.

* **Styling**
  Tweak the CSS in `templates/index.html`:

  * `.ssid-mapped` for cell highlights and ⭐
  * `.table-info` for user-added row background
  * `.ssid-editable:hover` for edit cursor hints

* **Mapping Storage**
  Mappings live in `ssid_mapping.json`. You can swap this out for SQLite, YAML, or any other store by editing `load_mapping()` / `save_mapping()` in `app.py`.

---

## 🤝 Contributing

1. Fork it!
2. Create a branch: `git checkout -b feature/my-feature`
3. Commit: `git commit -m "Add amazing feature"`
4. Push: `git push origin feature/my-feature`
5. Open a Pull Request

Bug reports, feature requests, and pull requests are all welcome.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE). Use it, modify it, and distribute it freely.

---

## 🙏 Acknowledgements

* **NirSoft** for creating [WifiInfoView](https://www.nirsoft.net/utils/wifi_information_view.html).
* **DataTables**, **Bootstrap**, and **jQuery** for their outstanding open-source libraries.

Enjoy your new interactive Wi-Fi scanner GUI! 🚀
