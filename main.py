import socket


def main():
    host = ''
    port = 50007
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        while True:
            print("Awaiting connection")
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                data = conn.recv(1024)
                print('Received data:', data)
                ans = b"answer"
                conn.sendall(ans)


if __name__ == "__main__":
    main()