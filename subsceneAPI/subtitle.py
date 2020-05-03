from bs4 import BeautifulSoup
import requests
import os
import re




class Subscene:
				def __init__(self,**kwargs):
								self.args = kwargs
								self.__header = { 
				"user-agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
																								}
								self.__setup()
				
				def __str__(self):
								return dicToStr(**self.args,URL=self.Domain)  

				def __repr__(self):
								return ("{}".format(self.args))

				
				def __getHTML(self,url):
								self.__htmlResponse = requests.get(url).text
								return BeautifulSoup(self.__htmlResponse,'lxml')
				
				def __postHTML(self,url):
								self.__htmlResponse =requests.post(url,data={'query':self.args['title']},headers=self.__header).text
								return BeautifulSoup(self.__htmlResponse,'lxml')
				
				def __setup(self): 
						        self.__Domain = "https://www.subscene.com" #home page
						        self.__pageSearch = "/subtitles/searchbytitle" # query page
						        self.__soupSearch =  self.__postHTML(self.__Domain+self.__pageSearch) #subtitles 
						    
						        self.__linkToSub = self.__searchBestResult(self.__soupSearch)
						        
						        if (self.__linkToSub == "not-found"):
						            raise Exception("\nerror : !!!!!!Result not found!!!!\n make sure you have entered correct 'title' and 'year'")        
						            
						        
						        self.__subtitleResponse = self.__getHTML(self.__Domain+self.__linkToSub)
						        
						        self.__getSubList(self.__subtitleResponse,self.args['language'])
						        
						        self.__getZIPlinks() # array of  absolute(full) download url  
   
			    def __searchBestResult(self,soupSearch):
			                searchList = soupSearch.select(".title a")
			                searchedMovie = self.__Normalization(self.args['title']+self.args['year'])
			                for item in searchList:
			                    availableMovie = self.__Normalization(item.text)
			                    if availableMovie == searchedMovie:
			                        return (item.attrs['href'])            
			                return "not-found"
			            
			    def __Normalization(self,string):
			            return (re.sub("\s|\(|\)|-|\.","",(string).lower()))
											
				
				def __getSubList(self,soup,lang):
								link = list( x.attrs["href"] for x in soup.select(".a1 a"))
								movieTitle = list(x.text for x in soup.select(".a1 span:last-child"))
								pattern = "[\r\n\t]"
								
								movieTitle = list(re.sub(pattern,"",movieName) for movieName in movieTitle)

								subtitles = list(zip(movieTitle,link))
								
								self.__requiredSubtitleList = list((x,v) for x,v in subtitles if lang.lower() in v ) # default english subtitles tuples
								#[('www.TamilRockers.ws - Extraction (2020)[HDRip - [Tamil + Telugu] - XviD - MP3 - 700MB - ESubs] ',
#               '/subtitles/extraction-2020/english/2198327'),
#                  ('Official Trailer - Extraction (2020) ',
#                   '/subtitles/extraction-2020/english/2183629')]

				def __getZIPlinks(self): #zip file download link
								self.ZIPlinks = [] 
								
								self.__totalAvailable = len(self.__requiredSubtitleList)
								self.__searchLimit =self.__totalAvailable  if (str(self.args['limit'])).lower() == 'all'  else int(self.args['limit'])
								
								for i in range(min(self.__totalAvailable,self.__searchLimit)):
												soup = self.__getHTML(self.Domain+self.__requiredSubtitleList[i][1])
												self.ZIPlinks.append((self.__requiredSubtitleList[i][0],self.Domain+soup.select_one("#downloadButton").attrs["href"])) #list of tuple of (name,zipURL)
																																#(movie name + zip download full link) 
				def ZIPfile(self):
								files = []
								for i in range(len(self.ZIPlinks)):
												files.append(requests.get(self.ZIPlinks[i][1])) #request for zip file / zip file download
								return files  # returns zip file as a response 
				
				def showZIP(self): 
								print(self.ZIPlinks) # display movie title with zip download link in list of tuple
				
				
				def downloadZIP(self,path=os.path.abspath(os.path.curdir)):
								self.ZIPfile()
								normPath = os.path.normpath(path) 
								
								if(os.path.isdir(normPath)):
												for i in range(min(self.__totalAvailable,self.__searchLimit)):
																fileName = self.ZIPlinks[i][0]+".zip"
																with open(os.path.join(os.path.normpath(path),fileName),"wb") as file:
																				ZIPfileList = self.ZIPfile()
																				file.write(ZIPfileList[0].content)
								else:
												try:
																raise Exception("legal path is required / path to a dir ")
												except Exceptiton as  e:
																print("ERROR:"+e)
	

#----------- functions----------------------------------------------

def dicToStr(**kwargs): # returing string of the dictionary type
				string=''
				for item,value in kwargs.items():
								string +="  "+item+" : "+str(value)+",\n"
				
				string = "{}\n{} {}".format('{',string,'}')
				return string

	


#------------ returns instance of the subscene object ---------------
#------------ main function to be called----------------------------               
def search(title=None,year ='',language="English",domain="subscene",limit='all'): # limit specifies nos. of subtitle to be fetched
				try:
						if title == None or year == None:
							raise Exception("'title' and 'year' cannot be of None type ")
				except ValueError as e :
							print("value Error :" + repr(e))
				
				args = {'title':title,'year':year,'language':language,'domain':domain,'limit':limit}
				return Subscene(**args)


# if __name__ == "__main__":

# 	obj = search(title="extraction",year="2015",language="Arabic",limit=2)
# 	obj.ZIPfile()
# 	print(obj.ZIPlinks)
# 	print(dir(obj))
# 	print(obj.Domain)
# 	print(obj)
