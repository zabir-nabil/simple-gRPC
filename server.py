import grpc
from concurrent import futures
import time

import image_procedure

# import the generated classes
import image_procedure_pb2
import image_procedure_pb2_grpc


# based on .proto service
class ImageProcedureServicer(image_procedure_pb2_grpc.ImageProcedureServicer):

    def ImageMeanWH(self, request, context):
        response = image_procedure_pb2.Prediction()
        response.channel, response.mean  = image_procedure.predict(request.b64image, request.width, request.height)
        return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=12))


# add the defined class to the server
image_procedure_pb2_grpc.add_ImageProcedureServicer_to_server(
        ImageProcedureServicer(), server)

# listen on port 5005
print('Starting server. Listening on port 5005.')
server.add_insecure_port('[::]:5005')
server.start()

try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    server.stop(0)
