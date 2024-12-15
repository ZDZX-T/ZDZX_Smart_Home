# 小爱本地化

b站视频链接[https://www.bilibili.com/video/BV11hB7YFE9o/?vd_source=39491253fa18502cd3cec1aac25976b5](https://www.bilibili.com/video/BV11hB7YFE9o/?vd_source=39491253fa18502cd3cec1aac25976b5)

## 文件夹包含内容介绍

| 文件                                 | 介绍        |
|------------------------------------|-----------|
| [mi2local.yaml](./mi2local.yaml)   | esp配置文件   |
| [flows_new.json](./flows_new.json) | Node-RED流 |

## 使用方法

1. 将mi2local.yaml（进行必要的改写）烧录到你自己的开发板内，并根据代码内容焊接电路。完成后将设备添加到HA中。
2. 根据代码中选择的空调品牌在米家建立相同的遥控器。通过Xiaomi Miot Auto将遥控器同步到HA中
3. 将flows_new.json导入到Node-RED中，需要：  
   a. 小爱本地化trigger设置server与目标Entities（即第一步中添加到HA中的空调）；  
   b. 复原状态action设置server与目标Targets（即第二步中添加到HA中的遥控器的Turn Off按钮）。
4. 在米家新建手动控制，执行动作为“开空调并调整至制定状态”，记录下设置的空调状态，在Node-RED中的对应路径添加具体要执行的内容。
