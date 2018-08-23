# 创建socket服务端
import socket

host = ''  # 监听在0000上
port = 12345
addr = (host, port)
s = socket.socket()
# 如果下面不设置，系统保留套接字60s，加上设置，程序可以立即重新启动
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)
cli_sock, cli_addr = s.accept()
print("client connected from :", cli_addr)
print(cli_sock.recv(1024))
# cli_sock.setsockopt(b'I 4 C U\r\n')
cli_sock.send(b'I 4 C U\r\n')
cli_sock.close()
s.close()
# telnet 127.0.0.1 12345 测试端口是否开启,验证
"""
def foo():
    return 'hello world',100
a=foo()
s,i=foo()
s
i
"""
