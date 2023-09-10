from User import User
from Computers import Computers


class Admin(User):
    def __init__(self, username, password, name, email, userInfo,
                 computerInfo):
        User.__init__(self, username, password, name, email)
        self.__username = username
        self.__password = password
        self.__name = name
        self.__email = email
        self.__userInfo = userInfo
        self.__userList = []
        self.__computerInfo = computerInfo
        self.__computerList = []

    def getUserList(self):
        return self.__userList
    def getComputerList(self):
        return self.__computerList
    def getUserInfo(self):
        return self.__userList
    def getComputerInfo(self):
        return self.__computerInfo

    def setUserList(self, userList):
        self.__userList = userList
    def setComputerList(self, computerList):
        self.__computerList = computerList
    def setUserInfo(self, userInfo):
        self.__userInfo = userInfo
    def setComputerInfo(self, computerInfo):
        self.__computerInfo = computerInfo

    
    # prints information of all users in userlist
    def viewAllUsers(self):
        for user in self.__userList:
            user.toString()

    # prints information of all computers in computerlist
    def viewAllComputers(self):
        for computer in self.__computerList:
            print(computer.toString())


    # creates users from file and appends object references to a list
    def createUserList(self):
        infoFile = open(self.__userInfo, "r")
      # list created for each property (username, password, etc)
        lists = [[], [], [], []]
        length = 0
      # appends each line of file to associated property list
        for line in infoFile:
            lists[length].append(line.strip())
            length += 1
          # if the list number is 4, the counter is reset so next value is added to first list
            if length == 4:
                length = 0
          
        for i in range((len(lists[1]))):
            self.__userList.append(
                User(lists[0][i], lists[1][i], lists[2][i], lists[3][i]))

    # method for creating a user and storing it
    def addNewUser(self, newUser, Store):
        # creates user object and appends it to list
        self.__userList.append(
            User(newUser[0], newUser[1], newUser[2], newUser[3]))
      # appends user properties to file
        with open(self.__userInfo, "a") as file:
            file.write(newUser[0] + "\n" + newUser[1] + "\n" + newUser[2] +
                       "\n" + newUser[3] + "\n")
        # calls store method to update the number of users
        Store.addNumUserStat()
        # returns the added user object to assign it to current user
        return self.__userList[-1]

    # method so the admin can remove a user
    def removeUser(self, Store):
      # asks admin for username of user to rempove
        username = input(
            "Enter the username of the user you would like to remove: ")
      # checks for username in the userlist
        for user in self.__userList:
            if username == user.getUsername():
              # removes user from userlist
                self.__userList.remove(user)
              # rewrites user info file excluding the removed user
                with open(self.__userInfo, "w") as file:
                    for user in self.__userList:
                        file.write(user.getName() + "\n" + user.getEmail() +
                                   "\n" + user.getUsername() + "\n" +
                                   user.getPassword() + "\n")
                # updates the number of users by calling store method
                Store.removeNumUserStat()

    # login method for admin
    def login(self, userList):
        password = ""
        username = input("Enter Admin username: ")
        # checks if inputted username matches admin username
        if username == self.__userList[0].getUsername():
          # if the password is incorrect, the admin is asked to retry until it is right
            while password != self.__userList[0].getPassword():
                password = input("Enter Admin password: ")
                if password != self.__userList[0].getPassword():
                    print("Wrong Admin password! Please enter again: ")
            print("Admin Sucesssfully Logged In!")
            return self

    # method for creating the computer list from file
    def createComputerList(self):
        compInfoFile = open(self.__computerInfo, "r")
      # list created for each property (name, id, etc)
        lists = [[], [], [], [], [], [], []]
        length = 0
        for line in compInfoFile:
          # appends each line of file to associated property list
            lists[length].append(line.strip())
            length += 1
          # if the list number is 7, the counter is reset so next value is added to first list
            if length == 7:
                length = 0
        # creates computer object and appends it to the computer list
        for i in range((len(lists[1]))):
            self.__computerList.append(
                Computers(lists[0][i], lists[1][i], lists[2][i], lists[3][i],
                          lists[4][i], lists[5][i], lists[6][i]))

    # method for removing a computer from the database
    def removeComputer(self, Store):
        compName = input(
            "Enter the name of the computer you would like to remove: ")
      # checks what computer object the inputted name is associated with
        for computer in self.__computerList:
            if compName == computer.getName():
              # if name matches, the object containing it is removed from the computer list
                self.__computerList.remove(computer)
              # computer file is rewritten based on updated computer list
                with open(self.__computerInfo, "w") as file:
                    for computer in self.__computerList:
                        file.write(computer.getName() + "\n" +
                                   computer.getModelNum() + "\n" +
                                   computer.getManufacturer() + "\n" +
                                   computer.getRamSize() + "\n" +
                                   computer.getStorage() + "\n" +
                                   computer.getProcessorSpeed() + "\n" +
                                   computer.getPrice() + "\n")
                # store method is called to update the number of computers
                Store.updateNumComputersStat()
