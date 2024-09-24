import requests
from datetime import datetime
from pydantic import BaseModel, ValidationError
import json

class role(BaseModel):
  uuid : str
  displayName  :str 
  description : str 
  displayIcon : str
  assetPath : str

class recruitmentData(BaseModel):
  recruitmentData : object 
  counterId : str
  milestoneId : str
  milestoneThreshold : int
  useLevelVpCostOverride : bool
  levelVpCostOverride : int
  startDate : datetime
  endDate : datetime

class abilities(BaseModel):
  slot : str
  displayName : str
  description : str 
  displayIcon : str

class mediaList(BaseModel):
  id : int
  wwise :str
  wave : str

class voiceLine(BaseModel):
  minDuration : float
  maxDuration : float
  mediaList : list[mediaList]

class agentData(BaseModel):
  uuid : str
  displayName : str
  description : str 
  developerName: str
  characterTags : list[str] | None
  displayIcon:  str
  displayIconSmall : str
  bustPortrait : str
  fullPortrait : str
  fullPortraitV2: str
  killfeedPortrait: str
  background: str
  backgroundGradientColors: list[str]
  assetPath : str
  isFullPortraitRightFacing : bool
  isPlayableCharacter : bool
  isAvailableForTest : bool
  isBaseContent : bool
  role : role
  recruitmentData : recruitmentData | None
  abilities : list[abilities]
  voiceLine : voiceLine | None

class bundleData(BaseModel):
  uuid : str
  displayName : str
  displayNameSubtext : str
  description : str
  extraDescription : str
  promoDescription : str 
  useAdditionalContext : bool
  displayIcon : str
  displayIcon2 : str
  logoIcon : str
  verticalPromoImage : str
  assetPath : str

class Agent(BaseModel):
  data : agentData

class Bundle(BaseModel):

  data : bundleData

agents = {}
response = requests.get("https://valorant-api.com/v1/agents")
try:
  if response.status_code == 200:
    agents = response.json()
    print("data is valid")
except ValidationError:
  print("Validation error! try again idk man")  

gekko : Agent = agents['data'][0]
gekkoUuid = gekko['uuid']

agentNamesInOrder = []
for agent in agents['data']:
  agentNamesInOrder.append(agent['displayName'])



#example by uuid
#specificAgent = requests.get("https://valorant-api.com/v1/agents/e370fa57-4757-3604-3648-499e1f642d3f")
#gdata = specificAgent.json()
#print(gdata)
#gekko = Agent(**gdata)
#print(gekko)

agentNumber = 0

while(True):
  print("\nPress 1 to continue to agent select; press 0 to exit")
  flag = input()
  if (flag == '1'):
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
  else:
    break