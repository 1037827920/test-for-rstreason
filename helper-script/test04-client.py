# FILEPATH:/data/testcase-for-nettrace/TCP_STATE/client.py
import socket
import struct

def main():
    # 创建TCP套接字
    sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 设置服务器地址
    serv_addr = ('127.0.0.1', 8080)
    
    # 设置SO_LINGER选项(立即发送RST)
    # l_onoff=1表示启用, l_linger=0表示立即放弃连接
    linger_option = struct.pack('ii', 1, 0)
    sockfd.setsockopt(socket.SOL_SOCKET, socket.SO_LINGER, linger_option)
    
    # 连接服务器
    sockfd.connect(serv_addr)
    
    # 关闭连接(将触发RST)
    sockfd.close()

if __name__ == '__main__':
    main()
