# 安装Docker  
菜鸟教程[https://www.runoob.com/docker/ubuntu-docker-install.html](https://www.runoob.com/docker/ubuntu-docker-install.html)  
官网教程[https://docs.docker.com/engine/install/ubuntu/](https://docs.docker.com/engine/install/ubuntu/)  
清华镜像站[https://mirror.tuna.tsinghua.edu.cn/help/docker-ce/](https://mirror.tuna.tsinghua.edu.cn/help/docker-ce/)

下方流程使用官网教程的使用apt的安装方法

## 1. 设置docker的apt存储库  
添加 Docker 的官方 GPG 密钥  
```shell
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```
将存储库添加到apt源  
```shell
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

## 2. 下载最新版本docker包  
```shell  
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```  

## 3. 镜像加速  
设置目录在`/etc/docker/daemon.json`，具体的加速网站要时刻现搜，写的格式如下
```json
{
  "registry-mirrors":[
    "https://registry.docker-cn.com",
    "https://docker.mirrors.ustc.edu.cn/",
    "https://hub-mirror.c.163.com/"
  ]
}
```
之后重启服务
```shell
sudo systemctl daemon-reload
sudo systemctl restart docker
```


什么？没有镜像加速？那还是悄咪咪用代理吧，仅对当前终端有效
```shell
export HTTP_PROXY=http://:port
export HTTPS_PROXY=https://:port
```

## 4. 验证docker是否安装成功
```shell
sudo docker run hello-world
```