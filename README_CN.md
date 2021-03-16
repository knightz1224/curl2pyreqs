# curl2pyreqs

一款基于 Python 实现的 curl 转换工具，可以直接将 curl 请求转换为使用 python-requests 的 Python 脚本。

## 系统要求

Python >= 3.6

pyperclip >= 1.8.0

rich >= 9.13.0

Linux 环境下需要安装 xclip 或 xsel 库

```Shell
sudo apt-get install xclip
or
sudo apt-get install xsel
```

## 安装

Windows 下，输入：

```Shell
> pip install curl2pyreqs
```

MacOS 或 Linux 下，输入：

```Shell
$ pip3 install curl2pyreqs
```

## 使用方法

### 作为程序直接运行

-   将存有 curl 请求的文本文件转换为 Python 文件

```Shell
$ curl2pyreqs -F example.curl
```

-   读取剪贴板里的 curl 请求，转换为 Python 代码

```Shell
$ curl2pyreqs -F example.curl
Convertion Finished.
Please open example.py to check the code.
```

### 通过 import

-   解析从 Chrome 或 Firefox 中获取的 Curl 字符串：

```Python
>>> from curl2pyreqs.ulti import parseCurlString
>>> output = parseCurlString("""curl -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0' -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8' -H 'accept-language: en-US,en;q=0.5' --compressed -H 'upgrade-insecure-requests: 1' -H 'te: trailers' https://pypi.org/""")
>>> print(output)
```

-   解析存有从 Chrome 或 Firefox 中获取的 Curl 字符串的文件：

```Python
>>> from curl2pyreqs.ulti import parseCurlFile
>>> output = parseCurlFile('./example.curl')
>>> print(output)
```
