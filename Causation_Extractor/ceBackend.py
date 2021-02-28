import json
import os
import datetime

class ceBackend:

	#defines the relationships based on the master json file created by ce_gui
	def relationshipDefiner(self):
		with open("demo1.json") as jsonFile:
			#jsons are loaded as a list of dicts. each dict is a json block
			data = json.load(jsonFile)
			sortTest = sorted(data, key = lambda i: i["start"])
		timeframe = datetime.timedelta(seconds=30) #Check in 15 second blocks
		startTime = datetime.datetime.strptime(sortTest[0]["start"], '%Y-%m-%dT%H:%M:%S') #Init time to check against
		endTime   = startTime+timeframe
		relationshipList = []
		tempList = []
		auditD_found = 0


		for block in sortTest: #Sort through json blocks, adding each to their relationship 
			dateTimeObj = datetime.datetime.strptime(block["start"], '%Y-%m-%dT%H:%M:%S')

			#Screenshot elements are only important after commands, and we only want 1
			if 'timed_id' in block.keys(): 
				if auditD_found:
					tempList.append(block)
					auditD_found = 0
				else: #If a screenshot is found but not before a command, we ignore it
					pass
			#Anything that isn't a screenshot gets appended (including keyclicks)
			else:
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
		#relationshipList[0][0], each index is an artifact
		#relationship[0][0]["fieldName"], each index is a key:value pair from the json.
		return relationshipList

	#Iterates through relationship list that is given and counts the number of artifacts present
	def getTotalArtifacts(self, relationshipList):
		artifactCount = 0
		for relationship in relationshipList:
			for artifact in relationship:
				artifactCount+=1
		return artifactCount


	#Formats the relationship output
	def outputRelationships(self, relationshipList):
		for i in range(len(relationshipList)):
			print("Relationship:%i----------------------------------------------------------"%(i+1))
			#print(json.dumps(relationshipList[i], sort_keys=True, indent=4)) #Debug, prints out entire json list in a pretty format

			for j in range(len(relationshipList[i])):
				print("Timestamp:%s, Content:%s " %(relationshipList[i][j]["start"],relationshipList[i][j]["content"]))
			print("\n\n\n") #Make the output less harsh on the yees
