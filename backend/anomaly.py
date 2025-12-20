def detect_bottlenecks(processes):
    for p in processes:
        if p["cpu"] > 90:
            p["status"] = "Critical"
        elif p["cpu"] > 70:
            p["status"] = "Warning"
        else:
            p["status"] = "Normal"
    return processes
