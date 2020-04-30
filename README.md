# SUBSCENE-API[:link:](https://github.com/s-4-m-a-n/subscene-API/tree/master/subsceneAPI)<br/>

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source-150x25.png?v=103)](https://github.com/s-4-m-a-n) 
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.png?v=103)](https://opensource.org/licenses/mit-license.php)<br/>
![versions](https://img.shields.io/pypi/pyversions/pybadges.svg)

subscene API also known as subtitle API is an unofficial API of [subscene subtitle provider](https://www.subscene.com/) which is written in python3 by using web scrapping tools and techniques.This api allows you to fetch subtitles list,download links as well as subtitles(in ZIP format) on the basis of the movie title and other parameters that are discribed below in the documentation section.<br/><br/>

## [:small_blue_diamond:](https://github.com/s-4-m-a-n)<ins>How to install<ins> ?
   ***below given code works in both terminal and cmd***:heavy_check_mark:
      It can be installed using [pip](https://pypi.org/project/subsceneAPI/)
``` 
  $  pip install subsceneAPI==<version>
  
```
  since the current version is 0.1. You can write 
  
```
  $  pip install subsceneAPI==0.1

``` 
  To test if the installation was sucessiful,try:
```
  $  subsceneAPI -v 
    OR
  $  subsceneAPI --version

```
For sucessiful installation the expected output is :
```
  $  subscene-API 0.1

``` 
## <ins>Usage<ins>:
  subscene API can be use both from command line and as a python package.
  Command line is not recommended here because it is just for testing purpose and all the features of the package are not included in CLI version. This API can be used for developing subtitle downloader and any other web based project.
  
### :computer: Command Line Usage:
All the commands for subscene API can be found using help flag.
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
    For instance , 
  ```python
    import subsceneAPI
    from subsceneAPI import subtitle    
    obj = subtitle.search(title="extraction",year="2020",language="english",limit="1")
 ```
  

## LICENSE:
  It is an open source project and is being licensed under MIT LICENSE - [click me](https://github.com/s-4-m-a-n/subscene-API/blob/master/LICENSE) to get to the license file for more details.
  ***It is not an official [subscene version : 4.0](https://www.subscene.com/) product.***
  
  
 

[![Facebook](https://img.shields.io/static/v1.svg?label=follow&message=@me&color=9cf&logo=facebook&style=flat&logoColor=white&colorA=informational)](https://www.facebook.com/suman.dhakal.39982) 
[![Twitter](https://img.shields.io/static/v1.svg?label=follow&message=@&color=grey&logo=twitter&style=flat&logoColor=white&colorA=critical)](https://twitter.com/s_4_m_A_N)
      

  
  