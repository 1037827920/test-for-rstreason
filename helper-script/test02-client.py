# client.py
import socket
import struct
import time

def send_old_ack(dst_ip, dst_port, old_ack_seq):
    # 构造原始套接字
    raw_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    
    # 伪造IP头部
    ip_header = struct.pack('!BBHHHBBH4s4s',
        69, 0, 40,  # TTL=40
        12345, 0, 64, socket.IPPROTO_TCP, 0,
        socket.inet_aton('127.0.0.1'),  # 源IP（伪造客户端）
        socket.inet_aton(dst_ip)
    )
    
    # 伪造TCP头部（关键：设置旧ACK和时间戳）
    tcp_header = struct.pack('!HHLLBBHHH',
        50000, dst_port,        # 源端口、目标端口
        0, old_ack_seq,         # 序列号设为0，ACK号为旧值
        5 << 4, 0x10,           # Header长度+ACK标志
        8192, 0,               # Window size
        0x0000                 # 校验位暂空
    )
    
    # 添加过期时间戳（模拟1秒前的包）
    # TCP时间戳实际只需要32位，应该使用毫秒时间戳的低32位
    ts_val = int(time.time() * 1000) & 0xFFFFFFFF
    ts_ecr = (int(time.time() * 1000) - 1000) & 0xFFFFFFFF
    tcp_options = struct.pack('!BBII', 8, 10, ts_ecr, ts_val)

    tcp_header += tcp_options
    
    # 计算校验和
    pseudo_header = struct.pack('!4s4sBBH',
        socket.inet_aton('127.0.0.1'),
        socket.inet_aton(dst_ip),
        0, socket.IPPROTO_TCP, len(tcp_header)
    )
    data = pseudo_header + tcp_header
    checksum = 0
    # 处理完整的16位字
    for i in range(0, len(data) - len(data) % 2, 2):
        word = (data[i] << 8) + data[i+1]
        checksum += word
    # 处理最后一个字节（如果是奇数长度）
    if len(data) % 2:
        checksum += data[-1] << 8
    checksum = (checksum & 0xffff) + (checksum >> 16)
    checksum = ~checksum & 0xffff
    
    # 更新TCP头校验位
    tcp_header = tcp_header[:16] + struct.pack('H', checksum) + tcp_header[18:]
    
    # 发送伪造包
    raw_socket.sendto(ip_header + tcp_header, (dst_ip, dst_port))
    print("Sent old ACK with seq: ", old_ack_seq)

if __name__ == '__main__':
    # 正常连接获取初始ACK
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 50000))
    first_ack = client.recv(1024)[-4:]  # 获取第一个数据包的ACK号
    old_ack_seq = struct.unpack('!I', first_ack)[0]
    client.close()
    
    # 延迟发送旧ACK
    time.sleep(3)
    send_old_ack('127.0.0.1', 50000, old_ack_seq)