import requests

# Send some requests
for i in range(10):
    data = {"user": f"user{i}", "message": f"hello world {i}"}
    requests.post("http://localhost:5001/send", json=data)
