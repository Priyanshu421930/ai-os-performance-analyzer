import React, { useEffect, useState } from "react";
import "./App.css";

const API = "http://127.0.0.1:5000";

function App() {
  const [metrics, setMetrics] = useState({});
  const [processes, setProcesses] = useState([]);
  const [forecast, setForecast] = useState(0);
  const [suggestions, setSuggestions] = useState([]);

  useEffect(() => {
    const interval = setInterval(() => {
      fetch(API + "/metrics").then(r => r.json()).then(setMetrics);
      fetch(API + "/processes").then(r => r.json()).then(setProcesses);
      fetch(API + "/forecast").then(r => r.json()).then(d => setForecast(d.cpu_forecast));
      fetch(API + "/suggestions").then(r => r.json()).then(setSuggestions);
    }, 3000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="app">
      <header className="header">
        <h1>🧠 System Architect AI</h1>
        <span className="status">REAL-TIME MONITORING ACTIVE</span>
      </header>

      <div className="cards">
        <div className="card">CPU Usage: {metrics.cpu}%</div>
        <div className="card">Memory: {metrics.memory} GB</div>
        <div className="card">Disk: {metrics.disk} MB/s</div>
        <div className="card alert">Forecast CPU: {forecast}%</div>
      </div>

      <h2 className="section">Active Processes</h2>
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>CPU</th>
            <th>RAM</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {processes.map(p => (
            <tr key={p.pid} className={p.status}>
              <td>{p.name}</td>
              <td>{p.cpu}%</td>
              <td>{p.memory} GB</td>
              <td>{p.status}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <h2 className="section">AI Suggestions</h2>
      <ul>
        {suggestions.map((s, i) => <li key={i}>{s}</li>)}
      </ul>
    </div>
  );
}

export default App;
