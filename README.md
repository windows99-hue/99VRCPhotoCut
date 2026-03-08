# 99VRCPhotoCut

> Create, Share, Play

## 介绍

这是一个小程序，用来便利的裁剪掉vrchat拍立得保存的图片的白边，只留下正图。

> [!WARNING]
>
> 本程序只适用于Windows操作系统，不过在修改任意键检测后可能支持MacOS/Linux

## 安装

### 下载

你可以去[Releases](https://github.com/windows99-hue/99VRCPhotoCut/releases)下载我编译完的版本

### 自行编译

本程序需要被编译为`exe`文件才可用

> [!NOTE]
>
> 本程序使用python3.14开发，理论上python3即可

1. 下载本仓库

2. 运行

   ~~~shell
   pip install -r requirements.txt
   ~~~

3. 运行

   ~~~shell
   pyinstaller -F main.py
   ~~~

   有关`pyinstaller`的更多用法请参阅官方文档

## 使用

将需要处理的图片直接拖入`main.exe`，如图

图片

可以一次拖入多张照片，如果有重名程序会询问您是否要覆盖文件

## 在最后

本程序使用`MIT`协议，祝您游玩愉快！

> 时间暂停本是神的技能，而摄影可以让我们窥探神的技能。 ——Tim