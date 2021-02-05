# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 12:52
# @Author  : Lim Yoona
# @Site    : 
# @File    : 04_udp_communication_model.py
# @Software: PyCharm

"""
    TCP相关介绍
"""
"""
    udp通信模型
        通信开始前，不需要建立连接，只负责发送数据
        
    UDP服务器：socket()--> bind()--> recvfrom()--> (收到数据)-->sendto()
    UDP客户端：socket()--> sendto()--> (收到回复)--> recvfrom()--> close()
    
    TCP通信模型
        通信之前，需要建立连接
    
    TCP服务器：socket()--> bind()--> listen()--> accept()--> (建立与客户端的连接)--> read()--> write()--> (数据应答)--> (客户端结束通知)--> close()
    TCP客户端：socket()--> connect()--> (TCP三次握手)--> write()--> (发送请求数据)--> (服务端应答)--> read()--> close()
        
"""