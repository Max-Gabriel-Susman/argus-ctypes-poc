
cmpl: 
	gcc -shared -o librtmp_server.so -fPIC rtmp_server.c

request:
	ffmpeg -re -i input.mp4 -c:v libx264 -preset fast -b:v 2000k -maxrate 2000k -bufsize 4000k \
-c:a aac -b:a 128k -f flv rtmp://localhost:1935/live/stream_key
