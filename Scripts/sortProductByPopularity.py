##################################
#Code by Chris Schild for NAU ISA#
#Questions? cvs46@nau.edu        #
##################################

#Open the Data File
rawdata = open('rawdata.csv', 'r').read()

#Split File by line (possible b/c of Excel's export)
splitByItem = rawdata.split('\n')

#remove first line (header)
del splitByItem[0]

#Declare variables for later
output = "" #string
res = {} #Dictionary

#Iterate through each row
for item in splitByItem:

	#"this" prefix is used in each iteration
	#split current row by comma
	thisItem = item.split(',')

	#set variables for ID and QTY of current row
	thisID = thisItem[0]
	thisQty = thisItem[1]

	#check if ID already exists in dictionary
	if thisID in res:

		#if ID exists, set var equal to old qty (as int for math's sake)
		oldValue = int(res[thisID])
		
		#add qty of old and new recore
		newValue = oldValue + int(thisQty)
		
		#write updated row into dict
		res[thisID] = newValue

	else:
		#set new item in dict
		res[thisID] = int(thisQty)

#Loop through finished dict and output in reverse sorted order
for key in sorted(res, key=res.get, reverse=True):
	#output each value to console
	print(key, res[key])



