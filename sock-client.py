import socket
import sys

class SocketClient:
    def __init__(self, host, port, timeout):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.settimeout(timeout)
        try:
            self.sock.connect((host, int(port)))
            print("\u001b[32;1m### Connected.")
        except ValueError:
            print("\u001b[31;1m!!! Host must be number!")
            print("\u001b[0m")
            sys.exit(0)

    def send_message(self):
        message = input("\u001b[34;1m--> ")
        self.sock.send(message.encode())
    
    def get_response(self):
        try:
            while True:
                response = self.sock.recv(1024)
                try:
                    print("\u001b[33;1m<--", response.decode())
                except:
                    print("\u001b[33;1m<--", str(response))
        except:
            pass

    def close_sock(self):
        self.sock.close()

if __name__ == "__main__":

    help_message = """
    Basic Python Socket Client

    FOR HELP:
    $ python3 sock-client.py help

    USAGE:
    $ python3 sock-client.py <host> <port> <timeout:optional>
    """
    
    if len(sys.argv) >= 2 and sys.argv[1] == "help":
        print(help_message)
        sys.exit(0)

    try:
        host    = sys.argv[1] if len(sys.argv) >= 2 else input("\u001b[35;1m### Host : ")
        port    = sys.argv[2] if len(sys.argv) >= 3 else input("\u001b[35;1m### Port : ")
        timeout = sys.argv[3] if len(sys.argv) >= 4 else 3

        client = SocketClient(host, port, timeout)

        while True:
            client.send_message()
            client.get_response()

    except KeyboardInterrupt:
        print("\n\u001b[32;1m### Bye!")
        print("\u001b[0m")
        if "client" in locals():
            client.close_sock()