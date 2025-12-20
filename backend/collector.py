import psutil

def get_system_metrics():
    return {
        "cpu": psutil.cpu_percent(interval=1),
        "memory": round(psutil.virtual_memory().used / (1024**3), 2),
        "disk": round(psutil.disk_io_counters().read_bytes / 1e6, 2)
    }

def get_processes():
    processes = []
    for p in psutil.process_iter(['pid','name','cpu_percent','memory_info','io_counters']):
        try:
            processes.append({
                "pid": p.info['pid'],
                "name": p.info['name'],
                "cpu": p.info['cpu_percent'],
                "memory": round(p.info['memory_info'].rss / (1024**3), 2),
                "disk": round(p.info['io_counters'].read_bytes / 1e6, 2)
            })
        except:
            pass
    return processes
