import socket


def main():
    '''socket 的基本使用'''

    # 创建udp的套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # ...这里是使用套接字的功能（省略）...
    # udp_socket.sendto("hahahah", 对方的ip和端口号：元组)
    udp_socket.sendto(b"Lfz    hello", ("59.68.5.145", 8080))  # 发送的数据类型必须是字节类型
    # 5. 不用的时候，关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()