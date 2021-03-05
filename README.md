# curl2pyreqs

A library to convert curl to python requests file.

## Install

```Bash
$ pip install curl2pyreqs
```

## Usage

Use as binary to export curl request to python script.

```Bash
$ curl2pyreqs -F example.curl
Convertion Finished.
Please open multi_test.py to check the code.
```

Convert a curl string to python-requests, copyed from Chrome or Firefox:

```Python
>>> from curl2pyreqs import parseCurlString
>>> output = parseCurlString("""curl -H 'user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0' -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8' -H 'accept-language: en-US,en;q=0.5' --compressed -H 'upgrade-insecure-requests: 1' -H 'te: trailers' https://pypi.org/""")
>>> print(output)
```

Convert curl file stream to python-requests, copyed from Chrome or Firefox:

```Python
>>> from curl2pyreqs import parseCurlFile
>>> output = parseCurlFile('./example.curl')
>>> print(output)
```
