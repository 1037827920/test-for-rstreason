# 客户端代码（触发RST的被动方）
import socket
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 12345))

# 发送测试数据
sock.send(b"test data")  

# 等待服务端关闭连接
time.sleep(1)

# 尝试继续发送数据（会触发ECONNRESET错误）
try:
    sock.send(b"more data")  
except ConnectionResetError:
    print("RST received by client")  