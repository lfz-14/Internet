# IP

## 一.端口号（重点）port  1024-65536

dest ip(目的ip):

src ip(源ip):

dest port(目标端口)：7788

src port(源端口)：

content： 数据流





## 二.socket简介



### 发送接收流程
 发送数据的流程：
 ```python
# 1. 创建套接字
import socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 2. 使用套接字发送数据
udp_socket.sendto("XXXXX".encode("utf-8"), ("192.168.33.11", 8080))
udp_socket.recvfrom(1024)
# 3. 关闭套接字
udp_socket.close()
```

 


 接收数据的流程：
 1. 创建套接字
 2. 绑定本地自己的信息（ip和port）
 3. 接收数据
 4. 关闭


### 单工，半双工，全双工
单工：收音机 只能单方向传输数据
半双工：对讲机 同一时刻只能单方向传输数据
全双工： socket套接字是全双工










 

