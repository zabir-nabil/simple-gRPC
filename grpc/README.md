# installation

`pip install grpcio`

`pip install grpcio-tools`

# Generating code

`python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. f_name.proto`