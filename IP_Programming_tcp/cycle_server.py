import socket


def main():
    """
    循环为多个客户端服务器
    """
    # 1.买个手机（socket）
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TODO 固定

    # 2.插入手机卡(bind)
    tcp_server_socket.bind(("", 7896))  # TODO 固定

    # 3.将手机设置为正常的 响铃模式(listen)
    tcp_server_socket.listen(128)  # TODO 固定

    while True:
        print("等待一个新的客户端的到来...")
        # 4. 等待别人的电话到来(accept) 返回值是一个元组 监听套接字 负责 等待有新的客户端进行连接 accept产生的新的套接字用来 为客户端服务
        new_client_socket, client_addr = tcp_server_socket.accept()  # TODO 固定

        # TODO 具体动能需求  此处也可以有循环  因为客户端可能有多个服务请求
        print("一个新的客户端已经到来 %s" % str(client_addr))

        # 接收客户端发送过来的请求
        recv_data = new_client_socket.recv(1024)
        print("客户端发送过来的请求是：%s" % recv_data)

        # 回送一部分数据给客户端
        new_client_socket.send("hahahahah-----ok----".encode("utf-8"))
        # TODO 功能结束

        # 关闭套接字
        new_client_socket.close()  # TODO 固定
        print("已经服务器完毕....")

        # 如果将监听套接字 关闭了， 那么会导致  不能再次等待新客户端的到来，即xxxx.accept就会失败
    tcp_server_socket.close()  # TODO 固定


if __name__ == "__main__":
    main()
