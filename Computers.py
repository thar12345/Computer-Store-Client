
class Computers:

  def __init__(self, name, modelNum, manufacturer, ramSize, storage, processorSpeed, price):
      self.__name = name
      self.__modelNum = modelNum
      self.__manufacturer = manufacturer
      self.__ramSize = ramSize
      self.__storage = storage
      self.__processorSpeed = processorSpeed
      self.__price = price

  def getName(self):
    return self.__name
  def getModelNum(self):
    return self.__modelNum
  def getManufacturer(self):
    return self.__manufacturer
  def getRamSize(self):
    return self.__ramSize
  def getStorage(self):
    return self.__storage
  def getProcessorSpeed(self):
    return self.__processorSpeed
  def getPrice(self):
    return self.__price

  def setName(self,name):
    self.__name = name
  def setModelNum(self,modelNum):
    self.__modelNum = modelNum
  def setManufacturer(self,manufacturer):
    self.__manufacturer = manufacturer
  def setRamSize(self,ramSize):
    self.__ramSize = ramSize
  def setStorage(self,storage):
    self.__storage = storage
  def setProcessorSpeed(self,processorSpeed):
    self.__processorSpeed = processorSpeed
  def setPrice(self,price):
    self.__price = price

    
  def toString(self):
    return """
    Name: {}
    Model Number: {}
    Manufacturer: {}
    RAM Size: {}gb
    Storage: {}gb
    Processor Speed: {}Ghz
    Price: ${}""".format(self.__name,self.__modelNum,self.__manufacturer,self.__ramSize,self.__storage,self.__processorSpeed,self.__price)



