#------------------------------------------------------------
### extracting the number of any website's(url) shares on facebook with graph facbeook API ###
#------------------------------------------------------------
# url of that format needed: 'http://graph.facebook.com/' + 'https://apple.com/mac'
# it returns a >>>json string<<<
# So we want to work with that json string an parse in over to python. (learn basics: http://python-guide-pt-br.readthedocs.io/en/latest/scenarios/json/ )
# parsed_json = json.loads(json_string)   <<< works like this


import json
import urllib






def addLink(): #adds link by user input over console
	list = []

	addElement = raw_input("Add a link here: ")

	list.append(addElement)

	return list


def addBunchOfLinks():
	print '> Howdy! I can tell you how often a certain website was shared on facebook.'

	stream = raw_input("""
	> Paste your links(URLs) of the websites below, each separated by one space, similar to:
	
	url1 url2 url3 

	> Then press [ENTER] to continue.

	""")

	list = stream.split() #use split(,) if they are comma separated like url1,url2,url3 (NOT url1, url2, url3!!!)
	
	return list

	


def extractShareCount(listOfLinks): #takes a list 

	resultset = []

	for url in listOfLinks:

		json_string = urllib.urlopen('http://graph.facebook.com/' + url).read()
		parsed_json = json.loads(json_string)

		numOfShares = parsed_json['share']['share_count'] # thats the way to adress json-objects and its attributes 

		entry = (beautyUrl(url), numOfShares)

		resultset.append(entry)

	return resultset	


		

def beautyUrl(url):
	#only works with urls which contains at least 3 slashes(inkl. 2 after http)

	beast = url
	inpoint = beast.find('www.')

	beauty = beast[inpoint:] #if you want everything of the url except 'https://' 

	#outpoint = beast.find('/', inpoint) #use it if you want only the domain 
	#beauty = beast[inpoint:outpoint]    #use it if you want only the domain 

	return beauty
	


#------------------------------------------------------------
# T E S T ?
#------------------------------------------------------------

"""
def section(url):
	json_string = urllib.urlopen('http://graph.facebook.com/' + url).read()
	parsed_json = json.loads(json_string)

	numOfShares = parsed_json['share']['share_count']

	return (url, numOfShares)

print section('https://www.facebook.com/abc')	
"""


def test1(): # add 1 link and processing
	while True:
		pass
		addLink()

		for i in listOfLinks:
			print extractShareCount(i)


		print listOfLinks


def test2():

	print beautyUrl('https://www.tutorialspoint.com/python/string_find.htm')


def testFinal(): # add n links and processing #>>BESTANDEN!

	inputStream = addBunchOfLinks()	

	print 
	print "> Okay buddy! I copied all links"
	print
	for link in inputStream:
		print link + ' --copied'

	print
	print
	print '> And here is what I found out about your links presented in the format(website, numberOfShares)'
	print

	tupels = extractShareCount(inputStream)	

	for tupel in tupels:
		print tupel 

"""
Sample-Set:
https://www.indiegogo.com/projects/the-mindfulness-movement-health-inspirational#/ https://www.indiegogo.com/products/hooded-travel-pillow https://www.indiegogo.com/products/soma-smart-shades-automate-blinds-and-shades-home-bluetooth--2 https://www.indiegogo.com/products/the-bruw-filter https://www.indiegogo.com/projects/the-chameleon-kid#/ https://www.indiegogo.com/projects/oeuvre-manquante-a-mtl-artwork-missing-in-mtl-art#/ https://www.indiegogo.com/projects/rigiet-the-most-advanced-smartphone-stabilizer#/ https://www.indiegogo.com/projects/code-8-a-film-from-robbie-stephen-amell#/

"""		

#>>>>>>>>>> S E L E C T   A   T E S T   C A S E <<<<<<<<<<<

testFinal()



#------------------------------------------------------------
# D O N E !
#------------------------------------------------------------

