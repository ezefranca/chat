from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

class Send:
    def __init__(self):
        self.__msg=''
        self.new = True
        self.con = None

    def put(self, msg):
        self.__msg=msg
        if self.con != None:
            # envia mensagem
            self.con.send(str.encode(self.__msg))

    def get(self):
        return self.__msg

    def loop(self):
        return self.new

def wait(tcp, send, host="", port=5700):
    origin=(host, port)
    #cria vinculo
    tcp.bind(origin)
    #deixa em espera
    tcp.listen(1)

    while True:
        #aceita conexao
        con, cliente = tcp.accept()
        print("Cliente: ", cliente, " conectado!")
        #atribui a conexao ao manipulador
        send.con = con

        while True:
            #aceita uma mensagem
            msg = con.recv(1024)
            if not msg: break
            print(str(msg, 'utf-8'))

if __name__ == "__main__":
    #cria um socket
    tcp=socket(AF_INET, SOCK_STREAM)
    send = Send()
    #cria uma Thread e usa a funcao wait com dois parametros
    process = Thread(target=wait, args=(tcp, send))
    process.start()
    print("Iniciando servidor de chat!")
    print("Aguarde alguém se conectar")

    msg = input()

    while True:
        send.put(msg)
        msg = input()

    process.join()
    tcp.close()
    exit()

