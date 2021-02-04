# -*- coding: utf-8 -*-
# @Time    : 2021/2/4 14:15
# @Author  : Lim Yoona
# @Site    : 
# @File    : 01_udp.py
# @Software: PyCharm

"""
    1.TCP/IP协议（族）Transmission Control Protocol/Internet Protocol
        定义：传输控制协议/网际协议）是指能够在多个不同网络间实现信息传输的协议簇。TCP/IP协议不仅仅指的是TCP 和IP两个协议，
        而是指一个由FTP、SMTP、TCP、UDP、IP等协议构成的协议簇， 只是因为在TCP/IP协议中TCP协议和IP协议最具代表性，所以被称为TCP/IP协议

        应用层--传输层--网际层--网络接口层
        TCP/UDP：传输层
        IP/ICMP/ARP/IGMP/RARP：网际层
"""

"""
     2.ip地址
        组成：网络地址+主机地址
        分类（IPV4）：
            A类IP：0开头，后7位为网络号，最后24位是主机号
                范围：1.0.0.1 -- 126.255.255.254
                网络号126个，每个网络号可容纳1677214个主机
            B类IP：10开头，后14位为网络号，最后16位是主机号
                范围：128.0.1.1 -- 191.255.255.254
                网络号16384个，每个网络号可容纳65534个主机
            C类IP：110开头，后21位为网络号，最后8位是主机号
                范围：192.0.1.1 -- 223.255.255.254
                网络号2097152个，每个网络号可容纳254个主机
            D类IP：第一个字节是1110，应用于多点广播（multicast）
                范围：224.0.0.1 -- 239.255.255.254
            E类IP：第一个字节是1111，保留地址，仅用于实验和开发
            私有IP：应用于局域网
                范围：10.0.0.0 --10.255.255.255
                     172.16.0.0 -- 172.31.255.255
                     192.168.0.0 -- 192.168.255.255

        需要注意：127.0.0.1 -- 127.255.255.255用于回路测试（127.0.0.1也代表本机IP地址）
"""

"""
    3.子网掩码（32位）
        作用：是将某个IP地址划分成网络地址和主机地址两部分子网掩码的设定必须遵循一定的规则。
        常用：255.255.255.0
            主机号全为0，表示网络号
            主机号全为1，表示网络广播

        注意：
            子网设置过大，会使数据无法找到正确的主机，导致网络传输错误；设置过小，造成跨子网传输，导致网络效率下降
            所以在一般的局域网中，在不超过254台主机的情况下使用255.255.255.0
"""

"""
    4.socket
        4.1 本地进程通信（IPC）：队列，同步（互斥锁、条件变量等）
        4.2 网络进程通信：利用TCP/IP协议，使用IP+端口，唯一标识主机进程应用
        4.3 socket（套接字）定义：进程间通信的一种方式，可实现不同主机之间的进程间通信，例如浏览网页，QQ....
        4.4 创建：socket.socket(AddressFamily,type)
            AddressFamily:可以选择 AF_INET（用于 Internet 进程间通信） 或者 AF_UNIX（用于同一台机器进程间通信）,实际工作中常用AF_INET
            type（套接字类型）:可以是 SOCK_STREAM（流式套接字，主要用于 TCP 协议）或者 SOCK_DGRAM（数据报套接字，主要用于 UDP 协议）
"""
import socket

# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # TCP socket
# s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)  # UDP socket
# print('socket created....')


"""
    5.UDP（用户数据报协议）
        定义：无连接的简单的面向数据包的运输协议。
        非可靠性，无需建立连接，没有重发机制，传输速度很快
        
        特点：
            数据包包含端口号+源端口号信息，可实现广播发送
            数据包大小有限制，在64KB之内，而且发送顺序和到达顺序不一定一致
        
        用途：多点通信，实时数据业务（QQ,语音广播,视频,TFTP(简单文件传送),SNMP(简单网络管理协议),RIP(路由信息协议，股票，航空),DNS（域名解析））
        注重点：速度流畅
        
        使用场景：局域网中可靠性搞得分散系统中client/server应用程序（视频会议，保证连贯性）
"""

"""
    6.UDP网络程序-发送数据
        
        流程：
            1.创建套接字
            2.发送/接收数据
            3.关闭套接字

        windows使用网络调试助手       
        
        需要注意的是：创建udp套接字，作为发送方的端口号是由系统随机分配的,可以通过
        socket.bind()来绑定发送方ip和端口信息
"""

# 创建套接字
udpso = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


#绑定端口号
binda = ('',7788)
udpso.bind(binda)


# 发送地址
sender = ('192.168.159.1', 8080)

# 获取数据 python2使用raw_input,python3使用input
data = input('请输入数据：')

#发送数据
udpso.sendto(bytes(data, 'utf-8'), sender)

#接收数据 recvfrom，接收的信息包含ip和端口信息，而直接使用recv不会包含这类信息
while True:
    redat = udpso.recvfrom(1024)
    print(str(redat))

#关闭
udpso.close()

"""
    总结：
        1.udp是TCP/IP协议族中的一种协议，能够完成不同机器上的程序见的数据通信
        2.udp服务器、客户端
            服务器：提供服务
            客户端：请求服务
        3.udp绑定问题
            一般情况，服务器端需要绑定端口号，目的是为了让其他客户端能够正确发送到此进程
            客户端，一般不需要绑定，有操作系统直接分配，这样就不会因为指定的端口号被占用而导致程序无法运行
"""
