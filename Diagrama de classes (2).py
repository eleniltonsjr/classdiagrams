class IP():
    def __init__(self, addr:int) -> None:
        self.addr = addr

class Service():
    def __init__(self, scr_port:int, dst_port:int) -> None:
        self._scr_port = scr_port
        self._dsr_port = dst_port
    def Protocolo():
        pass

class Host():
    def __init__(self,_addr, port:int) -> None:
        self._addr = _addr
        self.port = port
    def get_addr(self):
        return self._addr
    def get_addr_IP(self, IP):
        pass

class Protocolo():
    def send(self,data):
        pass
    def receive(self):
        pass

class UDP(Protocolo):
    def send(self,data):
        pass
    def receive(self):
        pass
    
class TCP(Protocolo):
    def handshake(self):
        pass
    def open(self):
        pass
    def close(self):
        pass
    def send(self, data):
        pass
    def receive(self):
        pass
