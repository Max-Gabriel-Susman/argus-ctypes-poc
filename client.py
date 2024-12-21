
from pyrtmp.client import RTMPClient

# Connect to the RTMP server
client = RTMPClient('rtmp://localhost:1935/live')
client.connect()

# Stream data
client.publish('stream_key', 'Test data')
client.close()