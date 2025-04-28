import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 65432))
server_socket.listen()

print("Server is listening for connections...")

try:
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print("Received from client:", data.decode())
        conn.sendall(b"Hello Client, I got your message!")
except Exception as e:
    print("Error:", e)
finally:
    conn.close()
    server_socket.close()
    print("Server connection closed.")
