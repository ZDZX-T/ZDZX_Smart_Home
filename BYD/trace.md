递归找到所有所需参数的获取方法，

## 获取位置
* 请求属性  

| 名称 | 值                |
|----|------------------|
| 方法 | GET              |
| 路径 | /wechat/location |

* 请求查询参数  

| 名称            | 释义  | 样例                                   | 备注     |
|---------------|-----|--------------------------------------|--------|
| caridentifier | 车架号 | XXXXXXXXXXXXXXXXX                    | 根据实际填写 |
| timeStamp     | 时间戳 | 1721059643055                        | 根据实际生成 |
| random        | 随机值 | 0de802b2-ad6e-372b-0793-5d29879625d4 | 自己随机生成 |
| longitude     | 经度  | 0                                    | 填0即可   |
| latitude      | 纬度  | 0                                    | 填0即可   |

*  cookies  

| 名称                                   | 释义           | 样例                                            | 备注                  |
|--------------------------------------|--------------|-----------------------------------------------|---------------------|
| HWWAFSESTIME                         | HWWAFSES设置时间 | 1721059618198                                 | 非必须，可其他请求获得         |
| HWWAFSESID                           | HWWAFSES值    | abc123def456hij789                            | 非必须，可其他请求获得         |
| openid                               | 猜测与微信授权有关    | abc123qwerty123456qwerty123456qwerty123456abc | 关键参数，其他请求获得，24h过期   |
| xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx | 猜测名称与微信账号有关  | qwerty123456qwert123456qwerty12               | 非必须，可其他请求获得，20min过期 |

*  其他  

| 名称         | 值     |
|------------|-------|
| Connection | close |

