from Computers import Computers

class User:
    def __init__(self, name="", email="", username="", password=""):
        self.__username = username
        self.__password = password
        self.__name = name
        self.__email = email

    #getters for the instance variables
    def getName(self):
      return self.__name
    def getEmail(self):
        return self.__email
    def getUsername(self):
      return self.__username
    def getPassword(self):
        return self.__password

    #setters for the instance variables
    def setName(self, name):
      self.__name = name
    def setUsername(self, username):
      self.__username = username
    def setEmail(self, email):
      self.__email = email
    def setPassword(self, password):
      self.__password = password

    #method that allows users to login in with their username and password
    def login(self, userList):
      password = ""
      self.__username = input("Enter your username: ")

      for i in range(1,len(userList)):
        if self.__username == userList[i].__username:
          while password != userList[i].__password:
            password = input("Enter your password: ")
            if password != userList[i].__password:
              print("Wrong password! Please enter again: ")
          print("Sucesssfully Logged In!")
          return userList[i]
      # if username is not found user is prompted to try again
      print("Username not found, please try again")
      self.login(userList)
      
    #method that creates and returns datafields for a new user
    def createAccount(self):
        self.__email = input("Email: ")
        self.__name = input("Name: ")
        self.__username = input("Create a username: ")
        self.__password = input("Create a password: ")
        return [self.__name, self.__email, self.__username, self.__password]

    #method thats adds a new computer to the database
    def addComputer(self, store):
      newCompName = input("Enter the computer's name: ")
      newModelNum = int(input("Enter the computer's model number: "))
      newManufacturer = input("Enter the computer's manufacturer: ")
      newRamSize = int(input("Enter the computer's ram size: "))
      newProcessorSpeed = float(input("Enter the computer's processor speed: "))
      newStorage = int(input("Enter the computer's storage capacity: "))
      newPrice = int(input("Enter the price of the computer: $"))
      newComputer = [newCompName, newModelNum, newManufacturer,
                        newRamSize, newProcessorSpeed, newStorage,
                        newPrice] 
      computerList = store.getComputerList()
      compFile = store.getCompFile()
      computerList.append(Computers(newComputer[0], newComputer[1], newComputer[2], newComputer[3],newComputer[4],newComputer[5],newComputer[6]))
      with open(compFile, "a") as file:
        file.write(newComputer[0] + "\n" + newComputer[1] + "\n" + newComputer[2] + "\n" + newComputer[3] + "\n" + newComputer[4] + "\n" + newComputer[5] + "\n" + newComputer[6] + "\n")
      store.updateNumComputersStat()
      store.setComputerList(computerList)

    #method that outputs the details of a user
    def toString(self):
        print(
            "\nname: " + self.__name,
            "\nusername: " + self.__username,
            "\nemail: " + self.__email,
            "\npassword: " + self.__password
        )
