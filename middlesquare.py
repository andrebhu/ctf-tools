from socket import socket

def middlesqrt(n):
	l = len(str(n))
	return str(pow(n, 2))[l//2: -l//2]


sock = socket()
sock.connect(('challenge.rgbsec.xyz', 23456))
sock.recv(1024)
sock.send(b"2\n")

while True:
	num = 0
	data = sock.recv(1024)
	print(data.decode("utf-8").strip())
	if b"rgbCTF" in data:
		break
	elif b"Incorrect" in data:
		break
	data = data.split(b" ")
	for d in data:
		if d[:-1].decode("utf-8").isnumeric():
			num = int(d[:-1])
	sock.send(middlesqrt(num).encode("utf-8") + b"\n")
	
sock.close()

