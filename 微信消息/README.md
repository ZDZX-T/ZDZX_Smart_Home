# wxMsg（暂未完成）
**注意：需要一下公网ip（用来通过企业微信可信IP认证，只使用一下）**  
**本项目代码部署部分以部署在云服务器上进行演示**
  
## 目录
  * [企业微信接收消息服务器设置](#企业微信接收消息服务器设置)
  * [Node-RED微信推送能力流设置](#Node-RED微信推送能力流设置)
  
## 企业微信接收消息服务器设置
1. 将[code](code)文件夹上传至有公网ip的服务器，**_并进入code文件夹内_**  
    文件夹中的[WXWXBizMsgCrypt3.py](code/WXBizMsgCrypt3.py)与[ierror.py](code/ierror.py)均来自于github项目[weworkapi_python](https://github.com/sbzhu/weworkapi_python/tree/master/callback)
2. 安装gunicorn等，注意此时工作目录在第1步上传的文件夹内（[gunicorn参考教程1](https://www.cnblogs.com/Mystogan/p/16144753.html)）（[gunicorn参考教程2](https://www.cnblogs.com/Ray-liang/p/4837850.html)）
    * 安装virtualenv  
        `sudo pip install virtualenv`
    * 创建虚拟环境  
        `virtualenv venv`
    * 进入虚拟环境  
        `source venv/bin/activate`
    * 安装所需的包，有gunicorn、flask、pycryptodome  
        `(venv) pip3 install -r requirements.py`  
3. 测试服务是否正常可用（可跳过）  
    * 运行test.py  
        `python3 test.py`
    * 虚拟环境内启动gunicorn  
        `(venv) gunicorn -w 1 -b 0.0.0.0:8080 test:app`  
        其中8080是你要从外网访问的端口，可以自己设，与flask使用的端口无关，**_记得在服务器安全组中开放_**。test是文件名，app是test文件内的实例名。
    * 浏览器访问服务器ip:8080，如果能看到页面显示“Hello World!”说明成功
    * ctrl+c结束本步骤中启动的gunicorn
    * ctrl+c结束本步骤中启动的test.py
4. 认证接收消息服务器  
    * 进入企业微信->应用管理->自建应用->企业可信IP->接收消息服务器配置界面  
        ![接收消息服务器配置界面](img/接收消息服务器配置.png)  
    * 随机获取Token与EncodingAESKey  
        将生成的Token填入[wxRes.py](code/wxRes.py)的sToken变量  
        将生成的EncodingAESKey填入[wxRes.py](code/wxRes.py)的sEncodingAESKey变量  
        将企业ID（在企业微信“我的企业”tab最底下）填入[wxRes.py](code/wxRes.py)的sCorpID变量
    * 运行[wxRes.py](code/wxRes.py)  
        `python3 wxRes.py`  
    * 虚拟环境内启动gunicorn  
        `(venv) gunicorn -w 1 -b 0.0.0.0:8080 wxRes:app`  
    * 将http://\<ip\>:8080填入接收消息服务器配置界面的URL处，点击保存，顺利的话会弹出“保存成功”字样  
        ![保存成功](img/保存成功.png)  
    * ctrl+c结束本步骤中启动的gunicorn  
    * 退出虚拟环境  
        `(venv) deactivate`  
    * ctrl+c结束本步骤中启动的test.py  
    * 关闭云服务器开放的8080端口  
  
## Node-RED微信推送能力流设置  
**_前面的区域以后再来探索吧_**  
TODO修改flows.json敏感信息