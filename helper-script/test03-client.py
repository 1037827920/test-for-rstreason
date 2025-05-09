import socket
import sys

def main():
    server_ip = '::1'  # IPv6 的本地回环地址
    server_port = 12345  # 选择一个没有服务监听的端口

    s = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    s.settimeout(3)
    try:
        s.connect((server_ip, server_port))
        print("Connection successful (unexpected)")
    except ConnectionRefusedError:
        print("Connection refused, RST received (expected behavior)")
    except Exception as e:
        print("Other exceptions occurred: ", e)
    finally:
        s.close()

if __name__ == '__main__':
    main()
