import requests
import time

t = time.time()
n = 10
# Send some requests
for i in range(n):
    data = {"user": f"user{i}", "message": f"hello world {i}"}
    requests.post("http://localhost:5001/send", json=data)

data = {"user": f"user{n}", "message": f"hello mango-world{n}"}
requests.post("http://localhost:5001/send", json=data)
t = time.time() - t
print(f"Total execution time: {t}")