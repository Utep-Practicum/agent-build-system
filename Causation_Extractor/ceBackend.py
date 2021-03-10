import json         #for reading files
import os           #for accessing files
import datetime     #For observation grouping
import re 			#for regex in artifact discovery
from dateutil.parser import parse #normalize packet time method

class ceBackend:

	#defines the relationships based on the master json file created by ce_gui
	def relationshipDefiner(self):
		with open("demo1.json") as jsonFile:
			#jsons are loaded as a list of dicts. each dict is a json block
			data = json.load(jsonFile)
			
			#DO THE CONVERSION FOR PACKET DATA HERE
			for observation in data:
				if observation["content"] == "network":
					observation["start"] = parse(observation["start"])
					observation["start"] = observation["start"]+datetime.timedelta(hours=5)
					observation["start"] = observation["start"].strftime('%Y-%m-%dT%H:%M:%S')

			sortTest = sorted(data, key = lambda i: i["start"])
		timeframe = datetime.timedelta(seconds=5) #Check in 15 second blocks
		startTime = datetime.datetime.strptime(sortTest[0]["start"], '%Y-%m-%dT%H:%M:%S') #Init time to check against
		endTime   = startTime+timeframe
		relationshipList = []
		tempList = []
		auditD_found = 0

		for block in sortTest: #Sort through json blocks, adding each to their relationship 
			dateTimeObj = datetime.datetime.strptime(block["start"], '%Y-%m-%dT%H:%M:%S')

			if 'timed_id' in block.keys(): #Screenshot elements are only important after commands, and we only want 1
				if auditD_found:
					tempList.append(block)
					auditD_found = 0
				else: #If a screenshot is found but not before a command, we ignore it
					pass
			else: #All logs that aren't screenshots get added

				if 'auditd_id' or 'keypresses_id' in block.keys(): #Turn boolean back on if we find an audit/keypress log
					auditD_found = 1
				tempList.append(block)

			if dateTimeObj > endTime: #Once 1st element outside of timeframe appears, store relationship and reset vars.
				relationshipList.append(tempList)
				startTime = datetime.datetime.strptime(block["start"], '%Y-%m-%dT%H:%M:%S')
				endTime = startTime+timeframe
				tempList = []
		#print(len(relationshipList))
		self.outputRelationships(relationshipList)

		#Relationships look like the following
		#relationshipList[0], Each index is a relationship
		#relationshipList[0][0], each index is an observation
		#relationship[0][0]["fieldName"], each index is a key:value pair from the json.
		return relationshipList

	#Finds artifacts
	def makeArtifacts(self, relationshipList):
		regexList = [line.rstrip() for line in open('regexLists/userKeywords.txt')]
		networkList = [line.rstrip() for line in open('regexLists/networkKeywords.txt')]
		count = 0

		for relationship in relationshipList:
			for observation in relationship:

				#Check to see if observation qualifies as salient artifact and searches accordingly
				if 'auditd_id' in observation.keys() or 'keypresses_id' in observation.keys(): 
					for regex in regexList: 
						if re.findall(regex, observation["content"]):
							#print("regex:%s found in observation:%s"% (regex, observation["content"]))
							observation['artifact'] = 1
							count+=1
							break #stops to avoid re-adding field
				elif 'data' in observation.keys():
					for regex in networkList:
						if re.findall(regex, str(observation["data"])):
							#print("network artifact:," observation["data"]) #DEBUG
							observation['artifact'] = 1
							count+=1
							#observation['data'] = 1 #DEBUG. Reduces output for better testing 
							break
				else: #observation is some type of screenshot
					observation['artifact'] = 0

		#print(json.dumps(relationshipList, sort_keys=True, indent=4)) #Debug, prints out entire json list in a pretty format
		return count
		

	#creates individual files for each relationship
	def createRelationshipFile(self, relationshipList):
		#relationshipList[0], Each index is a relationship
		#relationshipList[0][0], each index is an observation
		#relationship[0][0]["fieldName"], each index is a key:value pair from the json.

		#if relationships folder doesn't exist, create it
		if not os.path.isdir("relationships"):
			os.mkdir("relationships") 

		#print each relationship into relationships/relationship_x.json
		for i in range(len(relationshipList)):
			filename = "relationships/relationship_"+str(i+1)+".json"
			with open(filename, 'w') as json_file:
				json.dump(relationshipList[i], json_file)



	#Formats the relationship output, used pretty much only for debugging.
	def outputRelationships(self, relationshipList):
		for i in range(len(relationshipList)):
			print("Relationship:%i----------------------------------------------------------"%(i+1))
			#print(json.dumps(relationshipList[i], sort_keys=True, indent=4)) #Debug, prints out entire json list in a pretty format

			for j in range(len(relationshipList[i])):
				print("Timestamp:%s, Content:%s " %(relationshipList[i][j]["start"],relationshipList[i][j]["content"]))
			print("\n\n\n") #Make the output less harsh on the yees
