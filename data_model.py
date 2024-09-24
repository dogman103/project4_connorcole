import requests
import datetime
from pydantic import BaseModel, ValidationError
from enum import Enum

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
  mediaList : mediaList

class data(BaseModel):
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
  data : data

class Bundle(BaseModel):
  status : int
  data : bundleData

        
