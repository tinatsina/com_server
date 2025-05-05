from flask import Flask, jsonify
from flask_cors import CORS
import random
from datetime import datetime, timedelta

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# List of drone models
drone_models = [
    "Mavic Air 2",
    "Phantom 4 Pro",
    "Inspire 2",
    "Mini 3 Pro",
    "Skydio 2+",
    "Autel EVO II",
    "Parrot Anafi",
    "PowerEgg X",
    "Yuneec Typhoon H3",
    "ZeroZero Hover 2",
    "Ryze Tello",
    "DJI FPV",
    "Potensic D88",
    "Holy Stone HS720",
    "Ruko F11 Pro",
    "Autel EVO Lite+",
    "Blade Chroma",
    "BetaFPV Pavo30",
    "Walkera Voyager 5",
    "SwellPro Splash Drone 4"
]

# List of drone statuses
drone_statuses = [
    "Active",
    "Maintenance Required",
    "Standby",
    "Charging",
    "Out of Service"
]

# List of drone images (from the provided list)
drone_images = [
    "https://images.unsplash.com/photo-1473186639016-1451879a06f0",
    "https://images.unsplash.com/premium_photo-1714618849685-89cad85746b1",
    "https://images.unsplash.com/photo-1479152471347-3f2e62a2b2a7",
    "https://images.unsplash.com/photo-1456615913800-c33540eac399",
    "https://images.unsplash.com/photo-1506947411487-a56738267384"
]

@app.route('/get_rfid', methods=['GET'])
def get_rfid():
    # Generate a random RFID
    rfid = f"RFID-{random.randint(1000, 9999)}"

    # Generate a random date between 2020 and 2025
    start_date = datetime(2020, 1, 1)
    end_date = datetime(2025, 12, 31)
    random_days = random.randint(0, (end_date - start_date).days)
    random_date = start_date + timedelta(days=random_days)
    maintenance_date = random_date.strftime("%Y-%m-%d")

    # Generate drone data
    drone_data = {
        "id": f"DR-{random.randint(1000, 9999)}",
        "model": random.choice(drone_models),
        "rfid": rfid,
        "status": random.choice(drone_statuses),
        "lastMaintenance": maintenance_date,
        "image": random.choice(drone_images)
    }

    return jsonify(drone_data)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
