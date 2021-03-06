#coding=utf-8
import sys
import os
import configparser
base_path = os.getcwd()
sys.path.append(base_path)
import requests
import json
from Util.handle_json import get_value
from Util.handle_init1 import handle_ini

class BaseRequest:
    def send_post(self,url,data):
        #发送post请求
        res = requests.post(url=url,data=data).text
        return res

    def send_get(self,url,data):
        #发送get请求
        res = requests.get(url=url,params=data).text
        return res

    
    def run_main(self,method,url,data):
        # 执行方法，传递method、url、data参数

        base_url = handle_ini.get_value('host')
        if 'http' not in url:
            url = base_url+url
        print(url)

        if method == 'get':
            res = self.send_get(url,data)
        else:
            res =self.send_post(url,data)
            try:
                res = json.loads(res)
            except:
                print("这个结果是一个text")
        return res
#request = BaseRequest()
if __name__ == "__main__":
    request = BaseRequest()
    request.run_main('post','login',"{'username':'111111'}")
