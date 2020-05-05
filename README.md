# SUBSCENE-API (v 0.2)[:link:](https://github.com/s-4-m-a-n/subscene-API/tree/master/subsceneAPI)<br/>

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source-150x25.png?v=103)](https://github.com/s-4-m-a-n) 
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.png?v=103)](https://opensource.org/licenses/mit-license.php)
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)<br/>
[![Generic badge](https://img.shields.io/badge/python-3.7+-<COLOR>.svg)](https://www.python.org/)
[![Generic badge](https://img.shields.io/badge/Pypi-v0.2-<COLOR>.svg)](https://pypi.org/project/subsceneAPI/)
[![Generic badge](https://img.shields.io/badge/Python-Automation-<COLOR>.svg)](https://pypi.org/project/subsceneAPI/)

subscene API also known as subtitle API is an unofficial API of [subscene subtitle provider](https://www.subscene.com/) which is written in python3 by using web scrapping tools and techniques.This api allows you to fetch subtitles list,download links as well as subtitles(in ZIP format) on the basis of the movie's title and other parameters (they are discribed below in the [Usage](#usage) section).<br/><br/>

## [:small_blue_diamond:](https://github.com/s-4-m-a-n)<ins>How to install<ins> ?
#### Dependencies :
  Subscene API requires:
   - python (>=3.7)
   - requests (==2.23.0)
   - beautifulsoup4 (==4.9.0)
  
    
   ***below given code works in both terminal and cmd***:heavy_check_mark:
      It can be installed using [pip](https://pypi.org/project/subsceneAPI/)
``` 
  $  pip install subsceneAPI==<version>
  
```
  since the current version is 0.1. You can write 
  
```
  $  pip install subsceneAPI==0.2

``` 
  To test if the installation was sucessiful,try:
```
  $  subsceneAPI -v 
    OR
  $  subsceneAPI --version

```
For successful installation, the expected output is :
```
  $  subscene-API 0.2

``` 
## <ins>Usage<ins>:
  subscene API can be use both from command line and as a python package.
  Command line is not recommended here because it is just for testing purpose and all the features of the package are not included in CLI version. This API can be useful for developing subtitle downloader and any other web based project which includes subtitle information.
  
### :computer: Command Line Usage:
All the commands for subscene API can be found using ***help*** flag.
```
  $  subsceneAPI -h
    OR
  $  subsceneAPI --help
```
To get the list of available subtitles along with download links, try :
```
  $  subsceneAPI -t "movie title/name" -y "2020" -lng "english"
    OR
  $  subsceneAPI --title "movie title/name" --year "2020" --language "english"
```

***Remember,<br/>
  -t or --title and -y or --year is mandatory. The default argument for  -lng or --language is "english".You can find the possible choices for language in --help result*** <br/><br/>
  
### :page_with_curl: Library Usage: (recommended):heavy_check_mark:
    Import module subtitle from the package subsceneAPI
    
  ```python
    import subsceneAPI
    from subsceneAPI import subtitle
  ```
  Now,<br/>
      create an instance of subscene object by using function : 
      
  ```python  
      search(title="<movie name>",year="<yrs>,language="<language>",limit="<no of subtitles that you want>")
  ```
  :heavy_exclamation_mark:Note, the title is mandatory but not the limit and year.Although,year argument should be pass for more accurate and expected result.In addition, the default value for limit is 1 and all other possible values are positive integers and 'all'. With the value 'all', every available subtitles' information will be fetched.
  
   For instance , 
  ```python
    import subsceneAPI
    # or more ofthen,
    from subsceneAPI import subtitle    
    obj = subtitle.search(title="extraction",year="2020",language="english",limit="1")
 ```
 ### A simple implementation  :
 ```python
 >>>   from subsceneAPI import subtitle
 >>>   sub = subtitle.search(title="extraction",year="2020",language="english",limit="2")
 >>>   print(sub.ZIPlinks) # or obj.showZIPlinks()
 
 [('후아유 학교 2015.E01~E16.HDTV.H264.720p-WITH ',
  'https://www.subscene.com/subtitles/arabic-text/PU109MKIN052gH-c1GWyOCfTWLMLKmlfMrQXJcMMwO6b288LtEhtMIfkExgzB7hs8R0xZVR460THHwMT1PZ4iOPs6Vh_BjVhUJUfUxTc9yW8wCJ_tUbDzkpFsw4ofmIL0'),
 ('Who.Are.You.School-2015.E02-16.END.XviD-WITH-iPOP ',
  'https://www.subscene.com/subtitles/arabic-text/EgiL6LXr7Kp3bTtOT9fezovIu-6a5NcuPm66f8JPgPEP9HYHdM3yCXr9pQME2-hTCZeiPHusemyNgyVxVcW9qp6hmY3GCPJxXPuFBDWmb4XP58RNtbs8Gkij9EBxBiuv0')]
 ```
  obj.ZIPlinks 
  - contains the list of tuples of subtitle name and the download link of ZIPPed .srt file
 
 ### To download ZIP files:
   - download in current directory:
  ```python
    >>> sub.downloadZIP()
  ```
  - download at any absolute path:
   ```python
    >>> sub.downloadZIP(path="<abs path>")
  ```

## Developement:
   Contibuters of all experience levels are warmly welcomed to be the part of the subscene API community.The community goals are to be helpful,welcoming,effective.
   #### important links:
  - official source code repo : [https://github.com/s-4-m-a-n/subscene-API](https://github.com/s-4-m-a-n/subscene-API)
  - Download release : [https://pypi.org/project/subsceneAPI/](https://pypi.org/project/subsceneAPI/)<br/>
   #### <ins>source code:<ins>
   you can check the latest sources with the command :
   ```bash
          git clone https://github.com/s-4-m-a-n/subscene-API.git
   ```
   

## LICENSE:
  It is an open source project and is being licensed under MIT LICENSE - [click me](https://github.com/s-4-m-a-n/subscene-API/blob/master/LICENSE) to get to the license file for more details.
  ***It is not an official [subscene version : 4.0](https://www.subscene.com/) product.***
  
  
 

[![Facebook](https://img.shields.io/static/v1.svg?label=follow&message=@me&color=9cf&logo=facebook&style=flat&logoColor=white&colorA=informational)](https://www.facebook.com/suman.dhakal.39982) 
[![Twitter](https://img.shields.io/static/v1.svg?label=follow&message=@&color=grey&logo=twitter&style=flat&logoColor=white&colorA=critical)](https://twitter.com/s_4_m_A_N)
      

  
  