import socket
try:
    settings = open('settings.txt', 'r')
except FileNotFoundError:
    settings = open("settings.txt", "w")
    settings.write('localhost 8686')
    settings.close()
    settings = open("settings.txt", "r")
read = settings.readline().split()
settings.close()
try:
    SERVER_ADDRESS = (read[0], int(read[1]))
except IndexError: SERVER_ADDRESS = ("localhost", 8686)
BUF_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(SERVER_ADDRESS)
sock.listen(0)  # очередь = 0
print("Сервер запущен под адресом " +SERVER_ADDRESS[0] + ":" + str(SERVER_ADDRESS[1]))

connection, address = sock.accept()
print("Подключение с " + str(address[0]) + ":" +str(address[1]))
while True:
    try:  # если клиент разорвал соединение
        data = connection.recv(BUF_SIZE).decode()
    except OSError:
        sock.listen(0)
        connection, address = sock.accept()
        data = connection.recv(BUF_SIZE).decode()
    print("Запрос с " + str(address[0]) + ":" + str(address[1]) + " - " + data)

    newdata = ""
    i = 1
    try:
        for letter in str(data):  # делаем все чётные буквы заглавными
            if letter.isalpha():
                if i % 2 == 0:
                    newdata += letter.upper()
                    i += 1
                else:
                    newdata += letter
                    i += 1
            else: newdata += letter  # не буква, поэтому её не считаем
        newdata += "\n"
        connection.send(bytes(newdata.encode("UTF-8")))
    except NameError: pass
    #connection.close()
