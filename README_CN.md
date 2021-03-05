# curl2pyreqs

一款基于 Python 内置库实现的 curl 转换工具，可以直接将 curl 请求转换为使用 python-requests 的 Python 脚本。

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

1. 可以作为程序直接运行转换:

```Shell
$ curl2pyreqs -F example.curl
Convertion Finished.
Please open example.curl to check the code.
```

2. 在 Python 中 import 后，解析从 Chrome 或 Firefox 中获取的 Curl 字符串：

```Python
>>> from curl2pyreqs import parseCurlString
>>> output = parseCurlString("""curl -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0' -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8' -H 'accept-language: en-US,en;q=0.5' --compressed -H 'upgrade-insecure-requests: 1' -H 'te: trailers' https://pypi.org/""")
>>> print(output)
```

3. 或在 Python 中 import 后，解析存有从 Chrome 或 Firefox 中获取的 Curl 字符串的文件：

```Python
>>> from curl2pyreqs import parseCurlFile
>>> output = parseCurlFile('./example.curl')
>>> print(output)
```
