import argparse
from subsceneAPI import subtitle


def main():
	
	parser = argparse.ArgumentParser(description= "subscene-API")

	parser.add_argument("-v","--version",help="display version",action="store_true")

	parser.add_argument("-t","--title",default=None,type=str.lower,help="enter the movie title")
	parser.add_argument("-y","--year",type=str,help="enter the released year")
	parser.add_argument("-lng","--language",type=str.lower,default="english",choices=["english","arabic","albanian","arabic","bengali","turkish","spanish","swedish","thai","slovenian","russian","portuguese","malay","farsi/persian"],help="enter any language from choice")
	args = parser.parse_args()

	if args.version:
		print("subscene-API 0.2")

	elif args.title != None :
		obj = subtitle.search(title=args.title,year=args.year,language=args.language,limit=2)
		print("obj  :")
		print(obj)
		print("\nDownload links :")
		print(obj.ZIPlinks)

if __name__ == "__main__":
	main()