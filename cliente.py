from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

from servidor import Send


class Send:
    def __init__(self):
        self.__msg=''
        self.new = True
        self.con = None

    def put(self, msg):
        self.__msg=msg
        if self.con != None:
            #envia uma mensagem atraves de uma conexao socket
            self.con.send(str.encode(self.__msg))

    def get(self):
        return self.__msg

    def loop(self):
        return self.new

    def wait(tcp, send, host='localhost', port=5700):
        destiny = (host, port)
        #conecta a um servidor
        tcp.connect(destiny)

        while send.loop():
            print("Conectado a: ", host, ".")
            #atribui a conexao ao manipulador
            send.con=tcp
            while send.loop():
                #aceita uma mensagem
                msg = tcp.recv(1024)
                if not msg: break
                print(str(msg, "utf-8"))

    if __name__ == "__main__":
        print("Digite o nome ou IP do servidor (localhost): ")
        host=input()

        if host=='':
            host = '127.0.0.1'
    #cria um socket
    tcp=socket(AF_INET, SOCK_STREAM)
    send=Send()
    #cria um Thread e ysa a funçao esperar com dois argumentos
    process=Thread(target=wait, args=(tcp, send, host))
    process.start()
    print("")

    msg = input()
    while True:
        send.put(msg)
        msg=input()

    process.join()
    tcp.close()
    exit()