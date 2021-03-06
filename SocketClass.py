import socket

class Socket_Class():

    listening = True

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.allDataReceived = []

    """
    A function that opens a socket with Matlab PC
    """
    def openSocket(self):
        try:
            self.sockett = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print ("Socket successfully created")
        except socket.error as err:
            print ("socket creation failed with error %s" %(err))
            return False

        try:
            # connecting to the server
            self.sockett.connect((self.host, self.port))
            print ("the socket has successfully connected to Matlab on port == %s" %(self.host))
        except Exception as e:
            print(e)
            return False
        return True

    """
    function that sends data throught the socket to Matlab PC
    """
    def sendData(self, data):
        try:
            self.sockett.sendall(data.encode('utf-8')) # send marker data to Matlab PC
        except Exception as e:
            print(e)

    """
    Get method that returns allDataRecieved list
    """
    def getAllDataReceived (self):
        return self.allDataReceived

    """
    A function that closes the socket
    """
    def closeSocket(self):
        try:
            self.listening = False
            self.sockett.close()
        except Exception as e:
            print(e)
