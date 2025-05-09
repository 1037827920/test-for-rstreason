# 服务端代码（触发RST的主动方）
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 12345))
server.listen(1)

client_sock, addr = server.accept()

# 接收数据但不读取（模拟未消费数据）
data = client_sock.recv(1024, socket.MSG_PEEK)  # 仅窥探数据而不移出缓冲区

# 立即关闭连接（触发RST）
client_sock.close()  