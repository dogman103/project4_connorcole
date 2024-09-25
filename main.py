import requests
from datetime import datetime
from pydantic import BaseModel, ValidationError
import json
from data_model import Agent, Bundle


agents = {}
response = requests.get("https://valorant-api.com/v1/agents")
try:
  if response.status_code == 200:
    agents = response.json()
    print("data is valid")
except ValidationError:
  print("Agent Validation error! try again idk man")  

gekko : Agent = agents['data'][0]
gekkoUuid = gekko['uuid']

agentNamesInOrder = []
for agent in agents['data']:
  agentNamesInOrder.append(agent['displayName'])

bundles = {}
bundleResponse = requests.get("https://valorant-api.com/v1/bundles")
try:
  if bundleResponse.status_code == 200:
    bundles = bundleResponse.json()
    print("valid data")
except ValidationError:
  print("Bundle validation error; try again")

agentNumber = 0

while(True):
  print("\nPress 1 to continue to agent select; press 0 to exit")
  flag = input()
  if (flag == '1'):
    print("\n Would you like to view agents or bundles?: ")
    whichOne = input("0 for Agents, 1 for Bundles: ")
    if (whichOne == '0'):
      print("\nPlease select an agent to view:")
      for agent in agentNamesInOrder:
        print(agentNumber, agent)
        agentNumber += 1
      agentSelection=int(input("\nEnter the number of the agent to select: "))
      agentName = agents['data'][agentSelection]['displayName']
      print("what would you like to view?")
      print(f"1. The description of {agentName}")
      print(f"2. The abilities of {agentName}")
      print(f"3. All the information about {agentName}")
      characterInput = input("Select one of the options above and hit enter: ")
      if (characterInput == "1"):
        print('\n')
        print(agents['data'][agentSelection].get("description"))
      elif (characterInput == "2"):
        print('\n')
        agentAbilities = agents['data'][agentSelection].get('abilities')
        for item in agentAbilities:
          print(f"{item.get('displayName')} : {item.get('description')}")
      elif (characterInput == "3"):
        for item in agents['data'][agentSelection].items():
          print(item)
      else:
        print("Input not recognized; try again!")
      agentNumber = 0
    elif (whichOne == '1'):
      bundleCount = 0
      for item in bundles['data']:
        print(f"{bundleCount} : {bundles['data'][bundleCount]['displayName']}")
        bundleCount += 1
      bundleCount = 0
  else:
    break