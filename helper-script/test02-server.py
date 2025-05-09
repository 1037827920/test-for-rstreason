# server.py
import socket
import time

def tcp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('0.0.0.0', 50000))
    server.listen()
    
    conn, addr = server.accept()
    print(f"Connected by {addr}")
    
    # 发送两段数据，制造窗口变化
    conn.send(b'First data segment')
    time.sleep(2)  # 等待窗口更新
    conn.send(b'Second data segment')
    
    # 保持连接不关闭
    while True:
        time.sleep(1)

if __name__ == '__main__':
    tcp_server()