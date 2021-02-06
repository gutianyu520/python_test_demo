# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 14:23
# @Author  : Lim Yoona
# @Site    : 
# @File    : 01_packet_tracer.py
# @Software: PyCharm


"""
    通过packet tracer学习网络通信
"""
"""
    分类：
        电脑组网：
            1.点击左下角[End Devices],选择PC，将图标拖入编写框
            2.左击PC，在[physical]栏确保电脑处于开机状态
            3.[config]栏，选择[FastEnternet0]，配置静态IP和子网掩码
            4.点击左下角的[Connections],选择第一个，将两台电脑连接
            5.连接线上显示绿色，表明，连接正常
            6.左击PC，[Desktop]栏选择[Command Prompt]，这个就是DOS窗口，通过ping另一台电脑的ip查看网络状态
            7.点击右下角的[simulation]，可以debug网络通信过程
        
        集线器组网：
            1.设置电脑还是上面的方式
            2.点击[Network Devices],选择[Hubs],然后选择[PT-Hub]
            3.使用连接线将所有电脑与集线器连接
            4.使用[Command Prompt]进行测试网络状况，使用[simulation]查看ping的通信方式
        总结：
            1.集线器可以连接多台设备
            2.每个数据包都是以广播形式进行，容易堵塞网络
            
        交换机组网：
            1.设置电脑还是上面的方式
            2.点击[Network Devices],选择[Switches],然后选择[2950-24]
            3.使用连接线将所有电脑与集线器连接,稍等一会儿，等到线上都变绿了，就可以通信了
        总结：
            1.交换机可以连接多台设备
            2.每个数据包还是以广播形式进行，容易堵塞网络
            3.先进行arp广播，得到目标IP的MAC地址，然后只向目标IP发送数据
            
        路由器组网：
            1.设置电脑还是上面的方式
            2.加入交换机和路由器
        总结：
            1.需要设置默认弯管
            2.数据包通过路由器决定发送到那个ip
            
        交换机、路由器、服务器组网：
            1.设置PC：IP,NETMASK,DFGATEWAY,DNS
            2.设置ROUTER：IP,NETMASK,路由表
        总结：
            1.DNS服务器用来解析IP
            2.DFGATEWAY(默认网关)用来对顶，当数据包的目的IP不是当前网络时，此数据包转发到目的IP
            3.在路由器中路由表指定数据包的"下一跳"的地址
"""
