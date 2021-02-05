# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 16:40
# @Author  : Lim Yoona
# @Site    : 
# @File    : 04_other_network_info.py
# @Software: PyCharm

"""

"""
"""
    手动配置IP
        设置IP和子网掩码：ifconfig eth0 192.168.5.40 netmask 255.255.255.0
    设置网关
        route add default gw 192.168.5.1
        
    常见网络攻击：
        1.TCP半连接打击（SYN Flood，SYN洪水）：典型的DOS攻击，服务器TCP连接资源耗尽，影响正常TCP连接请求
        2.DNS攻击：
            2.1 DNS服务器劫持：流氓渔民服务器更改域名的解析结果，将用户引入错误的目标地址，阻止用户访问特定的网站，或者引入广告网页
            2.2 DNS欺骗：先来一个家的DNS应答，而抛弃了后面真正的DNS应答
                查看域名解析的IP地址：nslookup 域名
        3.ARP攻击：
        
"""








