# Monitor-For-lo-li.art
 lo-li.art 服务器监控客户端

## 使用方法

###  Windows 系统
1. 在 `Releases` 页面下载最新版本
2. 将程序放在服务器任意位置
3. 运行目录下名为 `main.exe` 的可执行文件
4. 你可以在 `config.yml` 中修改配置文件

### Linux 系统
1. 克隆项目库
2. 将程序放在服务器任意位置
3. 使用 `python main.py` 运行程序
4. 你可以在 `config.yml` 中修改配置文件

## 隐私安全
### 程序将会采集什么？
* CPU 使用率
* 内存使用率
* 设备名称（即 `hostname`）

## 注意事项
程序原理类似于计划任务，按照设定的间隔时间，向监控服务器发送服务器状态

因此，若想监控持续进行，请勿关闭程序

### Windows 系统
* 窗口右上角 “_” 形按钮左键单击即可最小化

### Linux 系统
若你的系统支持 `screen` 则可以使用如下方法后台运行：
1. `cd` 到程序目录
2. 使用 `screen npm start` 命令
3. 使用 `screen -S python ./main.py` 命令
4. 同时按下 `Ctrl + A + D` 退出
