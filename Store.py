from Computers import Computers

class Store:
  def __init__(self, computerList, ratingsFile, user,storeStatsFile, computerFile):
    self.__computerList = computerList
    self.__ratingsFile = ratingsFile
    self.__ratingsList = []
    self.__user = user
    self.__viewList = []
    self.__storeStatsFile = storeStatsFile
    self.__storeStatsList = []
    self.__computerFile = computerFile

  # getters
  def getStoreStatsList(self):
    return self.__storeStatsList
  def getComputerList(self):
    return self.__computerList
  def getCompFile(self):
    return self.__computerFile
  def getRatingsFile(self):
    return self.__ratingsFile
  def getRatingsList(self):
    return self.__ratingsList
  def getUserObject(self):
    return self.__user
  def getViewList(self):
    return self.__viewList
  def getStatsFile(self):
    return self.__storeStatsFile

  # setters
  def setComputerList(self, compList):
    self.__computerList = compList
  def setRatingsFile(self, ratingsFile):
    self.__ratingsFile = ratingsFile
  def setRatingsList(self, ratingsList):
    self.__ratingsList = ratingsList
  def setUser(self, user):
    self.__user = user
  def setViewList(self, viewList):
    self.__viewList = viewList
  def setStoreStatsFile(self, statsFile):
    self.__storeStatsFile = statsFile
  def setStoreStatsList(self, statsList):
    self.__storeStatsList = statsList
  def setComputerFile(self, computerFile):
    self.__computerFile = computerFile
    
  def mergeSorting(self, arr):
  # soring algorithm
      def mergeSort(arr):
          # the algo should only do something if the length of the array is greater than 1:

          if len(arr) > 1:
              # defining the two parts of the array.
              # left arr is the start to middle
              # right arr goes from middle to end.
              leftArr = arr[:len(arr) // 2]
              rightArr = arr[len(arr) // 2:]

              # calling merge sort recursively
              mergeSort(leftArr)
              mergeSort(rightArr)

              # implementing the merge step:

              # using i to keep track of the left most element of the left array
              # using j to keep track of the left most element in the right array.
              # using k to keep track of the index in the merged array.
              i = 0
              j = 0
              k = 0
              while i < len(leftArr) and j < len(rightArr):

                  if leftArr[i] < rightArr[j]:
                      # whenever the value of left arr at index i is less than the right arr, the value will be saved in
                      # the regular arr at index k.
                      arr[k] = leftArr[i]
                      i += 1

                  else:
                      # if right arr is smaller than the current arr.
                      arr[k] = rightArr[j]
                      j += 1
                  # incrementing k by one.
                  k += 1

              # transferring every element from the left arr without considering right arr.
              while i < len(leftArr):
                  arr[k] = leftArr[i]
                  i += 1
                  k += 1

              # transferring every element from the right arr without considering left arr.
              while j < len(rightArr):
                  arr[k] = rightArr[j]
                  j += 1
                  k += 1


      mergeSort(arr)

      return arr

  # searches for desired value and adds all matches to add to list
  def linearSearch(self, list, desiredValue):
    matchingList = []
    for i in range(0, len(list)):
        if (list[i].getManufacturer() == desiredValue):
            matchingList.append(list[i])
    return matchingList

  
  def filterByManufacturer(self):
    manufacturerList = []
    # creates list of available manufacturers to display in a menu
    for x in self.__computerList:
      if x.getManufacturer() not in manufacturerList:
        manufacturerList.append(x.getManufacturer())
    for i in range(len(manufacturerList)):
      print("\n" + str(i+1) + " " + manufacturerList[i])
    selection = int(input("\nChoose the manufacturer you'd like to see computers from: "))
    # uses input to find manufacturer in the manufacturer list and search through the computer list for computer matches using linear search
    manufacturer = self.__computerList[selection-1].getManufacturer()
    listWithComputers = self.linearSearch(self.__computerList, manufacturer)
    # displays the computers
    self.showComputers(listWithComputers)
    

  # sorts by price from low to high
  def sortComputerByPrice(self):
    price = []
    sortedComputerByPriceList = []
    # creates a list of all available prices
    for computer in self.__computerList:
      if (float(computer.getPrice())) not in price:
        price.append(float(computer.getPrice()))
        
    # uses merge sort to make a list of the prices from low to high
    sortedPrice = self.mergeSorting(price)

    # price finds matching computer and computer object is appanded to the list
    for price in sortedPrice:
      for computer in self.__computerList:
          if float(price) == float(computer.getPrice()):
            # appends computer object and its price to list of computers to be shown
            sortedComputerByPriceList.append([computer, "$" + str(price)])
          else:
            continue
    
    self.showComputers(sortedComputerByPriceList)

  # sorts by processor speed from low to high
  def sortComputerByProcessorSpeed(self):
    processorSpeed = []
    sortedComputerByProcessorSpeedList = []
    for computer in self.__computerList:
      if float(computer.getProcessorSpeed()) not in processorSpeed:
        processorSpeed.append(float(computer.getProcessorSpeed()))

      sortedProcessorSpeed = self.mergeSorting(processorSpeed)
    
    for processorSpeed in sortedProcessorSpeed:
      for computer in self.__computerList:
        if str(processorSpeed) == computer.getProcessorSpeed():
          sortedComputerByProcessorSpeedList.append([computer, str(processorSpeed) + "GHz"])
        else:
          continue

    self.showComputers(sortedComputerByProcessorSpeedList)

  # sorts by storage from high to low
  def sortComputerByStorage(self):
    storage = []
    sortedComputerByStorageList = []
    for computer in self.__computerList:
      if int(computer.getStorage()) not in storage:
        storage.append(int(computer.getStorage()))

      sortedStorage = self.mergeSorting(storage)

    for storage in sortedStorage:
      for computer in self.__computerList:
        if str(storage) == computer.getStorage():
          sortedComputerByStorageList.append([computer, str(storage) + "GB"])
        else:
          continue
          
    self.showComputers(sortedComputerByStorageList)

  # sorts by ram size from high to low
  def sortComputerByRamSize(self):
    ramSize = []
    sortedComputerByRamSizeList = []
    for computer in self.__computerList:
      if int(computer.getRamSize()) not in ramSize:
        ramSize.append(int(computer.getRamSize()))

    sortedRamSize = self.mergeSorting(ramSize)

    for ramSize in sortedRamSize:
      for computer in self.__computerList:
        if str(ramSize) == computer.getRamSize():
          sortedComputerByRamSizeList.append([computer, str(ramSize) + "GB"])
        else:
          continue
          
    self.showComputers(sortedComputerByRamSizeList)
  
  # display list of computer names with ability to expand on one
  def showComputers(self, computerList):
    newList = []
    attributeList = []

    # for computers which were sorted, each computer also contains its attribute (RAM, Storage) in the list
    # these are split into two lists for smooth operation
    if str(type(computerList[0])) == "<class 'list'>":
      for list in computerList:
        newList.append(list[0])
        attributeList.append(list[1])
      computerList = newList

    print("\n")
    # if there is an attribute list, the property is printed with the computer name
    if len(attributeList) > 0:
      for i in range(1, len(computerList)+1):
        print(str(i) + ": " + computerList[i-1].getName() + " - " + (attributeList[i-1]))
    # otherwise just the computer index and name are printed
    else:
      for i in range(1, len(computerList)+1):
        print(str(i) + ": " + computerList[i-1].getName())
      
    # allows user to select a computer from the printed list    
    select = int(input("\nPlese select a computer or enter 0 to return to the menu: "))
    if select == 0:
      pass
    else:
      # increases total number of views stat
      self.updateNumViewsStat()
      modelNum = computerList[select-1].getModelNum()
      # adds view for current computer for suggestion algorithm
      for x in self.__viewList:
        if x[0] == computerList[select-1]:
          x[1] = x[1] + 1
      # prints all of the computer's details 
      print(computerList[select-1].toString())
      # uses computer ID to find matching reviews
      compReviewList = self.displayReviews(modelNum)
      if compReviewList != None:  
        print("\nReviews:")
        # prints all reviews for the computer
        for review in compReviewList:
          print(self.ratingsToString(review))
      
      compmenu = int(input("""\nWould you like to:
          
          1. Purchase the computer
          2. Leave a review
          3. Return to computer list
          Enter your choice: """))

      # calls purchase method and uses object reference as argument
      if compmenu == 1:
        self.purchaseComputer(computerList[select-1])

      # calls review adding method and uses computer model number as argument
      if compmenu == 2:
        self.createReview(computerList[select-1].getModelNum())

      # calls current method with current computer list as argument so user can computers with previous configuration(sorted, filtered)
      elif compmenu == 3:
        self.showComputers(computerList)
    
  # initiates rating list from file
  def createRatingList(self):
    ratingsFile = open(self.__ratingsFile, "r")
    # one list for each property (username, rating, etc)
    lists = [[],[],[],[]]
    length = 0
    # lines 1-4 append to lists 1-4
    for line in ratingsFile:
        lists[length].append(line.strip())
        length+=1
      # when the list index reaches 4, it is set to 0 so the next set of attributes can be appended
        if length == 4:
            length = 0

    # appends one item from each list at a time
    for i in range((len(lists[1]))):
      self.__ratingsList.append([lists[0][i], lists[1][i], lists[2][i], lists[3][i]])

  # allows the user to add a review
  def createReview(self, productID):
    duplicate = False
    # username referenced using user object getter
    username = self.__user.getUsername()
    for i in range(len(self.__ratingsList)):
      # ensures user does not already have a review for selected product
      if self.__ratingsList[i][0] == username and self.__ratingsList[i][1] == productID:
        print("You have already reviewed this!")
        duplicate = True
    if not duplicate:
      # ensures rating is between 1 and 10
      while True:
        numRating = int(input("Enter a rating between 1 and 10: "))
        if 0 <= numRating <= 10:
          break
        else:
          print("Enter a value between 1 and 10! \n")
      # allows user to add comments
      comments = input("Write any comments about the product: ")
      # appends review to rating list
      self.__ratingsList.append([username, productID, numRating, comments])
      # appends review to file
      with open(self.__ratingsFile, "a") as file:
        file.write(str(username) + "\n" + str(productID) + "\n" + str(numRating) + "\n" + str(comments) + "\n")
      print("Thanks for leaving a review!")

  # allows user to remove or change previously added review
  def removeReview(self):
    track = 0
    # checks for reviews with usernames matching current user
    for i in range(len(self.__ratingsList)):
      if self.__ratingsList[i][0] == self.__user.getUsername():
        # checks if any reviews were found
        track = 1 
        # prints reviews with their ID and asks user to select a review based on number printed beside it
        print("\n" + str(i+1) + " " +  self.ratingsToString(self.__ratingsList[i]))
    if track != 1:
      print("No reviews found!")
    else:
      remove = int(input("\nWhich review would you like to edit or remove?: "))
      print("""
          Would you like to:
          1. Edit Review
          2. Delete Review
          """)
      selection = int(input("Enter your selection: "))
      productID = self.__ratingsList[remove-1][1]
      removeObject = self.__ratingsList[remove-1]
      # uses list remove method to remove review from list
      self.__ratingsList.remove(removeObject)
      # rewrites the ratings file so old review is not present
      with open(self.__ratingsFile, "w") as file:
        for x in self.__ratingsList:
          file.write(str(x[0]) + "\n" + str(x[1]) + "\n" + str(x[2]) + "\n" + str(x[3]) + "\n")
      # if user chooses to change the review the create review method is called and product id is passed
      if selection == 1:
        self.createReview(productID)

  # creates list of reviews matching a product
  def displayReviews(self, productID):
    productReviewList = []
    for i in range(len(self.__ratingsList)):
      # checks if product id in review matches requested product id
      if int(self.__ratingsList[i][1]) == int(productID):
        productReviewList.append(self.__ratingsList[i])
    return productReviewList

  # display the username, rating and comments of a review
  def ratingsToString(self, review):
    # gets product name using model id
    productNum = int(review[1])
    for x in self.__computerList:
      if int(x.getModelNum()) == productNum:
        productName = x.getName()
    return """
    Username: {}
    Product Name: {}
    Rating (out of 10): {}
    Comments: {}""".format(review[0], productName, review[2], review[3])

  # creates a list for counting the number of times a user viewed an object
  def viewTracker(self):
    for x in self.__computerList:
      # appends a list consisting of the object and the starting number of views
      self.__viewList.append([x, 0])

  # method for displaying the user computers which have similar processor speeds to those viewed previously
  def suggestComputers(self):
    suggestedList = []
    # selection sort algorithm finds highest viewed computer
    for i in range(len(self.__viewList)):
      n = i
      for x in range(i+1, len(self.__viewList)):
        # views of computers are compared to each other
        if self.__viewList[x][1] > self.__viewList[n][1]:
          # assigns larger value as computer with most views
          n = x
      # swaps current computer with one with highest views
      self.__viewList[i], self.__viewList[n] = self.__viewList[n], self.__viewList[i]
    # creates a lower speed and higher speed to find computers from
    desiredSpeed =self.__viewList[0][0].getProcessorSpeed()
    lowerDesired = float(desiredSpeed) - 0.3
    higherDesired = float(desiredSpeed) + 0.3
    # creates a suggested list
    for x in self.__computerList:
      if higherDesired >= float(x.getProcessorSpeed()) >= lowerDesired:
        suggestedList.append(x)
    print("\nShowing computers with processor speeds close to " + str(desiredSpeed) + "GHz")
    # displays computers with a similar processor speed
    self.showComputers(suggestedList)
    

  # creates list of store stats from file
  def createStoreStatsList(self):
    infoFile = open(self.__storeStatsFile, "r")
    lists = []
    for line in infoFile:
        lists.append(line.strip())

    for i in range((len(lists))):
      self.__storeStatsList.append(lists[i])

  # increments the number of users stat when called
  def addNumUserStat(self):
    self.__storeStatsList[0] = int(self.__storeStatsList[0]) + 1
    self.saveStats()

  #Reduces the number of users stat when called
  def removeNumUserStat(self):
    self.__storeStatsList[0] = int(self.__storeStatsList[0]) - 1
    self.saveStats()

  #Updates the total number of computers stat
  def updateNumComputersStat(self):
    self.__storeStatsList[1] = len(self.__computerList)
    self.saveStats()
    
  # increments the number of sales stat when called  
  def addNumSalesStat(self):
    self.__storeStatsList[2] = int(self.__storeStatsList[2]) + 1
    self.saveStats()

  # increments the number of total views stat when called
  def updateNumViewsStat(self):
    self.__storeStatsList[3] = int(self.__storeStatsList[3]) + 1
    self.saveStats()

  # method to write stats to file
  # called whenever stat is changed
  def saveStats(self):
     with open(self.__storeStatsFile, "w") as file:
      for stat in self.__storeStatsList:
        file.write(str(stat) + "\n")

  # method for user to buy a computer
  def purchaseComputer(self,computerChoice):
    # compares all computer objects to desired object
    for computer in self.__computerList:
      if computerChoice == computer:
        # removes purchased product from inventory
        self.__computerList.remove(computer)

        #updates the computer file to incorporate removal of computer
        with open(self.__computerFile, "w") as file:
          for computer in self.__computerList:
            file.write(computer.getName() + "\n" + computer.getModelNum() + "\n" + computer.getManufacturer() + "\n" + computer.getRamSize()+"\n" + computer.getStorage() + "\n" + computer.getProcessorSpeed() + "\n" + computer.getPrice() + "\n") 

    # increments store stat
    self.addNumSalesStat()
    print("Thank you for Shopping at Computer Central!")

  # displays store statistics for admin
  def displayStatistics(self):
    return """
    Total Users: {}
    Total Computers: {}
    Total Sales:{}
    Total Product Views:{}""".format(self.__storeStatsList[0],self.__storeStatsList[1],self.__storeStatsList[2], self.__storeStatsList[3])   
    
    