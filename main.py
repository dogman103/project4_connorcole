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

gekko = agents['data'][0]

gekkoList = gekko.items()
for item in gekkoList:
  print(item)

#example by uuid
#specificAgent = requests.get("https://valorant-api.com/v1/agents/e370fa57-4757-3604-3648-499e1f642d3f")
#gdata = specificAgent.json()
#print(gdata)
#gekko = Agent(**gdata)
#print(gekko)
