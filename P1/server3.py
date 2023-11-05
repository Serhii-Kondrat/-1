import socket
import datetime
import time
import threading


def process (client_socket):

        while True:  # Зациклюємо обмін повідомленнями
            try:
             data = client_socket.recv(1024).decode('utf-8')
            
            except Exception as e:
             print(f"Помилка у відправці повідомленя або клієнт написав exit{e}")
             break
            if data.lower() == 'close':
             response_close = "Сервер завершив свою роботу"
             client_socket.send(response_close.encode('utf-8'))
             print ("Сервер завершив свою роботу")
             client_socket.close() 

             break
            print(f"Отримані дані: {data}")

            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f"Час отримання повідомлення: {current_time}")

        
            time.sleep(5)
            current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            response = f"Повідомлення отримано: {data}\nЧас отримання: {current_time}"
            
            try:
            # amount = 0
                total_send = 0
                while total_send < len(response):
                    sendd = client_socket.send(response[total_send:].encode('utf-8'))
                    if sendd == 0:
                     print("Зєднання розірвано")
                    total_send += sendd

                print("Відповідь успішно доставлено клієнту")
            
            except Exception as e:
             print(f"Зєднання з клієнтом втрачено {e}")
            
        
    
        client_socket.close() 

host = '127.0.0.1'
port = 12345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)
print(f"Сервер слухає на {host}:{port}")

while True:
        client_socket, addr = server_socket.accept()
        print(f"З'єднано з {addr}")
        handel = threading.Thread(target= lambda: process( client_socket))
        handel.start()