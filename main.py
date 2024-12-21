import ctypes

# Load the shared library
rtmp_lib = ctypes.CDLL('./librtmp_server.so')

# Set the argument and return types for the function
rtmp_lib.start_rtmp_server.argtypes = [ctypes.c_int]
rtmp_lib.start_rtmp_server.restype = None

# Start the RTMP server
port = 1935
print(f"Starting RTMP server on port {port}")
rtmp_lib.start_rtmp_server(port)

