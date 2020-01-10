# Netease Cloud Music Copyright Protection File Dump

## Origin

 - [nondanee/ncmdump](https://github.com/nondanee/ncmdump)

## Introduce

This repository is a tool to transfer .ncm to .mp3 by using python and PyQt5.The transfer function depend on [nondanee/ncmdump](https://github.com/nondanee/ncmdump).

## Environment

window10+python3.7+pyqt5.10.1  
Mac10.14+python3.7+pyqt5.9.1

## Future

- [ ] support Threading
- [ ] Beautify the GUI
- [ ] More function

## Dependency

```
$ pip install pycryptodome mutagen pyqt5 pyinstaller 
```

## Install

 - if your os is windows ,you will get a exe application ;
 - if your os version is Mac, you will get a app applciaiton and a bash application; If your app file doesn't work,please check your source,you must use 
absolute path

```
$ cd config 
$ python pyinstaller
```

## Usage

![启动页面](https://www.zhangbohan.xyz/images/usage/ncmdump-pyqt5-1.png)  
![选择页面](https://www.zhangbohan.xyz/images/usage/ncmdump-pyqt5-2.png)  
![结果页面](https://www.zhangbohan.xyz/images/usage/ncmdump-pyqt5-3.png)  


