from flask import Flask, jsonify
from flask_cors import CORS
from collector import get_system_metrics, get_processes
from anomaly import detect_bottlenecks
from forecast import forecast_cpu

app = Flask(__name__)
CORS(app)

cpu_history = []

@app.route("/metrics")
def metrics():
    m = get_system_metrics()
    cpu_history.append(m["cpu"])
    return jsonify(m)

@app.route("/processes")
def processes():
    procs = detect_bottlenecks(get_processes())
    return jsonify(procs)

@app.route("/forecast")
def forecast():
    return jsonify({"cpu_forecast": forecast_cpu(cpu_history[-10:])})

@app.route("/suggestions")
def suggestions():
    return jsonify([
        "Close unused background apps",
        "Reduce browser tabs",
        "Increase RAM for heavy workloads"
    ])

if __name__ == "__main__":
    app.run(debug=True)
