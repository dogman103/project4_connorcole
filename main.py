import requests
from datetime import datetime
from pydantic import BaseModel, ValidationError

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
  characterTags : list[str]
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
  recruitmentData : recruitmentData
  abilities : list[abilities]
  voiceLine : voiceLine

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
  status : int
  data : agentData

class Bundle(BaseModel):

  data : bundleData

extracted_agents = {}
#response = requests.get("https://valorant-api.com/v1/agents")
#print(Agent.model_json_schema())
#if response.status_code == 200:
 # data = response.json()
  #extracted_agents = Agent(**data)
  
  #print("data is valid", data)
#if response.status_code == 400:
 # print("400")

specificAgent = requests.get("https://valorant-api.com/v1/agents/e370fa57-4757-3604-3648-499e1f642d3f")
data = specificAgent.json()
print(data)

