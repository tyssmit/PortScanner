import socket

class Scanner:
    def __init__(self, ip):
        self.ip=ip
        self.openPort=[]

    def __repr__(self):
        return 'Scanner: {}'.format(self.ip)

    def add_port(self, port):
        self.openPort.append(port)

    def scan(self, lowerport, upperport):
        for port in range(lowerport, upperport + 1):
            if(self.isOpen(port)):
                self.add_port(port)

    def isOpen(self, port):
        sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((self.ip,port))
        result=sock.connect_ex((self.ip, port))
        sock.close()
        return result==0

    def write(self, filepath):
        with open(filepath, 'w') as f:
            f.write('\n'.join(self.openPort))
def main():
    ip='192.168.1.245'
    scanner=Scanner(ip)
    scanner.scan(1,100)
    print(scanner.openPort)

if __name__ == "__main__":
    main()


