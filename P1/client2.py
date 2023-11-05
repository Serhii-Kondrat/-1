import socket
import time

host = '127.0.0.1'
port = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

while True:  # Зациклюємо обмін повідомленнями
    message = input("Введіть повідомлення для сервера (або 'close' для завершення): ")
    client_socket.send(message.encode('utf-8'))

    if message.lower() == 'close':
        cl = client_socket.recv(1024)
        print(cl.decode('utf-8'))
        break

    data = client_socket.recv(1024)
    print(f"\nВідповідь від сервера:")
    time.sleep(1)
    print(f"{data.decode('utf-8')}")

client_socket.close()
