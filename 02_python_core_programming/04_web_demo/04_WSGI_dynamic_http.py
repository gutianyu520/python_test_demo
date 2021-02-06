# -*- coding: utf-8 -*-
# @Time    : 2021/2/6 10:53
# @Author  : Lim Yoona
# @Site    : 
# @File    : 04_WSGI_dynamic_http.py
# @Software: PyCharm

"""
    服务器动态资源请求
"""
"""
    http请求过程：
        1.【浏览器】发出http请求动态资源                                 【浏览器】       =====>      【web服务器】
        2.【web服务器】通过wsgi向【应用程序框架】调用一个属性                【web服务器】    =====>       【应用程序框架】
        3.【应用程序框架】调用【web服务器】的方法，设置返回的状态和头信息       【应用程序框架】    =====>       【web服务器】
        4.【web服务器】调用返回，并且保存刚刚【应用程序框架】设置的信息         【web服务器】    =====>       【应用程序框架】
        5.【应用程序框架】处理请求，生成动态页面body信息                    【应用程序框架】    <=====>      【应用程序框架】
        6.【应用程序框架】将生成的动态body信息返回给【web服务器】             【应用程序框架】    =====>       【web服务器】
        7.【web服务器】将结果返回给【浏览器】                              【web服务器】    =====>       【浏览器】
"""

"""
    WSGI（web server gateway interface）：将web框架与web服务器分开，让不同框架进行协同工作
    类似于java中的servlet api
    
"""

"""
    定义WSGI接口(例)
        environ：一个包含所有HTTP请求信息的dict对象；
        start_response：一个发送HTTP响应的函数。
"""


def application(environ,start_response):
    start_response('200 OK',[('Content-Type', 'text/html')])
    return 'hello world'

