import socket

host = ''  # 表示所有客户端
port = 12345
addr = (host, port)
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)
while True:
    #一个客户端链接断开后，服务端等待下一个链接
    cli_sock, cli_addr = s.accept()
    print("client connected from :", cli_addr)
    print(cli_sock)
    while True:
        #某个指定的客户机链接过程
        data = cli_sock.recv(1024)
        if data.strip() == b'quit':
            break
        print(data.decode('utf8'),end='')
        sdata = input(">")
        sdata = "%s\r\n" % sdata
        cli_sock.send(sdata.encode("utf8"))
    # print(cli_sock.recv(1024))
    # cli_sock.send(b'I 4 C U\r\n')
    cli_sock.close()
s.close()
