from fastapi import FastAPI
import psutil
import platform
from typing import Dict, Any

app = FastAPI(title="Cloud Monitoring API")

@app.get("/health")
def health() -> Dict[str, str]:
    return {"status": "healthy"}

@app.get("/metrics")
def metrics() -> Dict[str, Any]:
    """
    Basic system metrics returned as JSON.
    (In production you'd expose Prometheus format; for demo JSON is fine.)
    """
    return {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "memory_percent": psutil.virtual_memory().percent,
        "disk_percent": psutil.disk_usage('/').percent,
        "system": platform.system(),
        "node": platform.node()
    }