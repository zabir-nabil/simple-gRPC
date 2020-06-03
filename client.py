import grpc

# import the generated classes
import image_procedure_pb2
import image_procedure_pb2_grpc

# data encoding

import numpy as np 
import base64
import zlib
import time

# open a gRPC channel
channel = grpc.insecure_channel('127.0.0.1:5005')

# create a stub (client)
stub = image_procedure_pb2_grpc.ImageProcedureStub(channel)

# encoding image/numpy array

t1 = time.time()
for _ in range(1000):
    frame = np.random.randint(0,255, (416,416,3), dtype=np.uint8) # dummy rgb image

    # compress

    data = frame # zlib.compress(frame)

    data = base64.b64encode(data)


    # create a valid request message
    image_req = image_procedure_pb2.B64Image(b64image = data, width = 416, height = 416)

    # make the call
    response = stub.ImageMeanWH(image_req)
t2 = time.time()

print(t2-t1)
# printing response
# print(response.channel)
# print(response.mean)