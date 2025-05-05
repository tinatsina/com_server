# COM SERVER

captures RFDI read values via pyserial and then posts them to a Flask API server, which is then brodacasted via CORS to our webapp

## Made With

- Flask
- Flask-CORS
- Arduino
- pyserial
- NodeJS
- Ant React
## Getting Started

To use the COM SERVER system, follow these steps:

1. Connect the Arduino device with the RFID reader
2. Install the required Python packages:
   ```
   pip install flask flask-cors pyserial
   ```
3. Start the Flask server to begin capturing RFID reads
4. Launch the web application to view the data in real-time

## System Architecture

The system consists of three main components:
- Arduino hardware with RFID reader that captures tag data
- Flask backend server that processes the RFID data via serial communication
- React frontend that displays the captured information

## Configuration

Configure the serial port settings in the `config.json` file:
```json
{
  "port": "COM3",
  "baudrate": 9600,
  "timeout": 1
}
```
