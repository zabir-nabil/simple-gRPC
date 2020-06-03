import numpy as np 
import base64
import zlib
import requests
import time

t1 = time.time()
for _ in range(1000):

    frame = np.random.randint(0,256, (416,416,3), dtype=np.uint8) # dummy rgb image


    # compress

    data = frame # zlib.compress(frame)

    data = base64.b64encode(data)


    data_send = data

    #data2 = base64.b64decode(data)

    #data2 = zlib.decompress(data2)


    #fdata = np.frombuffer(data2, dtype=np.uint8)


    r = requests.post("http://127.0.0.1:5000/predict", json={'imgb64' : data_send.decode(), 'w': 416, 'h': 416})
t2 = time.time()

print(t2-t1)