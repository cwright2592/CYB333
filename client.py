import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client_socket.connect(('127.0.0.1', 65432))
    client_socket.sendall(b"Hello Server!")
    data = client_socket.recv(1024)
    print("Received from server:", data.decode())
except Exception as e:
    print("Error:", e)
finally:
    client_socket.close()
    print("Client connection closed.")
