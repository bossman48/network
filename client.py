import socket
message = "Mesaj atiyorum"
bytesToSend         = str.encode(message)

serverAddress   = ("localhost", 20001)

bufferSize          = 1024


UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPClientSocket.sendto(bytesToSend, serverAddress)

gelenMesaj = UDPClientSocket.recvfrom(bufferSize)

message = "Serverın mesajı {}".format(gelenMesaj[0])

print(message)