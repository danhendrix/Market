
def initialize():
	currentMenu = {}

	beerList = ["Coors", "Ninkasi", "Bud"]

	for i in beerList:
		currentMenu[i] = {}
		currentMenu[i]['Demand']=100
		currentMenu[i]['Supply']=100
		currentMenu[i]['Price']=5
		
	return currentMenu


