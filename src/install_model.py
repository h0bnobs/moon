import requests
import json

url = "http://localhost:11434/api/pull"
model = "gemma3:4b"

with requests.post(url, json={"name": model}, stream=True) as r:
    for line in r.iter_lines():
        if line:
            try:
                data = json.loads(line.decode('utf-8'))
                if "completed" in data and "total" in data:
                    pct = (data["completed"] / data["total"]) * 100
                    print(f"{pct:.2f}% complete")
                else:
                    print(data.get("status", data))
            except json.JSONDecodeError:
                continue
