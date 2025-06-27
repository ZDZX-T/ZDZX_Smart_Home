# 安装Ubuntu Server  
**！！重要！！**  
**如有旧HA系统，请提前进行数据备份，包括但不限于Node-RED流、ESPHome配置文件。关机指令`sudo shutdown now`**  
**SD卡根据HA官网推荐，建议选择A2级别**

## 烧录
从官网下载镜像（从树莓派上直接下载也行），我下载的是Ubuntu服务器版24.04.2 LTS
[https://cn.ubuntu.com/download/raspberry-pi](https://cn.ubuntu.com/download/raspberry-pi)  
然后打开树莓派镜像烧录工具（下载地址[https://www.raspberrypi.com/software/](https://www.raspberrypi.com/software/)），树莓派设备选择自己的树莓派型号；操作系统选择最后的使用自定义镜像，然后选择刚刚下载的镜像；储存设备选择插入的SD卡。  
点击下一步后选择编辑设置，通用页需要设置主机名、设置用户名及密码、本地化设置时区选Asia/Shanghai键盘选us，服务页勾选开启SSH，选择使用密码登录。
然后进行写入即可。

## 初始化
将SD卡插入树莓派，同时使用网线将树莓派与路由器连接起来。上电开机。  
稍等片刻后在路由器管理界面查看树莓派分配到的IP，然后使用ssh工具连接树莓派。用户名和密码是刚刚在树莓派烧录器设置的。

## 换源  
备份ubuntu.sources
```shell
cd /etc/apt/sources.list.d
sudo cp ubuntu.sources ubuntu.sources.bak
```
编辑ubuntu.sources，换成[https://mirror.tuna.tsinghua.edu.cn/help/ubuntu-ports/](https://mirror.tuna.tsinghua.edu.cn/help/ubuntu-ports/)(arm版)中DEB822 格式的内容
```shell
sudo vim ubuntu.sources
```
更新软件包列表
```shell
sudo apt-get update
sudo apt-get upgrade
```

## 查看时区
```shell
timedatectl
```
显示之前设置的时区说明正常

## 设置私钥登录
在服务器上生成公私钥，保存位置默认，密码可选
```shell
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```
把公钥追加到 authorized_keys
```shell
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
```
将`~/.ssh/id_rsa`文件保存到本地  
使用ssh软件或命令行尝试使用私钥登录服务器，**成功后**删除服务器上的私钥
```shell
rm ~/.ssh/id_rsa
```
修改`/etc/ssh/sshd_config`文件内容，修改以下两项，同时查看`/etc/ssh/sshd_config.d`内有没有文件与下方设置冲突的，也需要一并改掉
```text
PermitRootLogin no
PasswordAuthentication no
```
重启ssh
```shell
sudo systemctl restart ssh
```