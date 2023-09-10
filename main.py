from User import User
from Admin import Admin
from Store import Store

# menu for login asks if user is new, returning or an admin
def loginMenu():
  print("Welcome to Computer Central!" + "\n")
  print("Press 1 if you are a new customer or 2 if you are returning or 3 to login as the admin: ")
  newOrOld = int(input("Enter your choice: "))
  # returns user choice
  return newOrOld

#moved menus here so it would be possible to call store methods

# menu for the user, takes store object as argument
def userMenu(self):
    menuselection =  int(input( """ 
  1. View All Computers
  2. Sort Computers by Price
  3. Sort Computers by Processor Speed
  4. Sort Computers by Storage Capacity
  5. Sort Computers by Memory
  6. Filter by Manufacturer
  7. Show Suggested Computers
  8. Remove or Modify Review
  9. Add a computer
  10. Log out
  Enter Your Selection: """
     ))

    if menuselection == 1:
      # calls store method with computer list as argument
      self.showComputers(self.getComputerList())
      # returns to menu when method is completed
      userMenu(self)
    elif menuselection == 2:
      self.sortComputerByPrice()
      userMenu(self)
    elif menuselection == 3:
      self.sortComputerByProcessorSpeed()
      userMenu(self)
    elif menuselection == 4:
      self.sortComputerByStorage()
      userMenu(self)
    elif menuselection == 5:
      self.sortComputerByRamSize()
      userMenu(self)
    elif menuselection == 6:
      self.filterByManufacturer()
      userMenu(self)
    elif menuselection == 7:
      self.suggestComputers()
      userMenu(self)
    elif menuselection == 8:
      self.removeReview()
      userMenu(self)
    elif menuselection == 9:
      # calls user method add computer with store object as argument 
      user.addComputer(self)
      userMenu(self)
    elif menuselection == 10:
      # ends program and prints message
      print("Successfully logged out.")

# menu for the admin, taking admin object as argument
def adminMenu(self):
        menuselection = int(
            input(""" 
  1. View All Users
  2. View All Computers
  3. Add a Computer
  4. Remove a Computer
  5. Add a User
  6. Remove a User
  7. View Statistics
  8. Log Out
  Enter Your Selection: """))
        if menuselection == 1:
          # calls admin class method
            self.viewAllUsers()
          # calls menu when method is completed
            adminMenu(admin)
        elif menuselection == 2:
            self.viewAllComputers()
            adminMenu(admin)
        elif menuselection == 3:
          # calls inherited method with store object as argument
            self.addComputer(store)
            adminMenu(admin)
        elif menuselection == 4:
            self.removeComputer(store)
            adminMenu(admin)
        elif menuselection == 5:
          # calls admin method with inherited method and store object as argument
            self.addNewUser(self.createAccount(), store)
            adminMenu(admin)
        elif menuselection == 6:
            self.removeUser(store)
            adminMenu(admin)
        elif menuselection == 7:
            print(store.displayStatistics())
            adminMenu(admin)
        elif menuselection == 8:
          # menu isn't called again so program is ended
            print("Sucessfully Logged Out!")

# each of the file names is assigned to a variable for future use
userFile = "UserInfo.txt"
computerFile = "Computers.txt"
ratingsFile = "Ratings.txt"
storeStatsFile = "StoreStats.txt"

# admin object is constructed with its details and the user and computer files as arguments
admin = Admin("admin1", "admin123", "Administrator", "admin@gmail.com", userFile, computerFile)
# user object is created with no arguments in order for login method to be called
user = User()
# userlist is created and assigned to variable
admin.createUserList()
userList = admin.getUserList()
# computerlist is created and assigned to variable
admin.createComputerList()
computerList = admin.getComputerList()

# store object is created with files, the computer list and the user object as arguments
store = Store(computerList, ratingsFile, user, storeStatsFile, computerFile)
# trackers are created for use within store method
store.viewTracker()
store.createStoreStatsList()
store.createRatingList()

newOrOld = loginMenu()

# if the user chooses 1 in the login menu
if newOrOld == 1:
  # new user is created and added to list and file, store stats updated
  admin.addNewUser(user.createAccount(), store)
  print("Successfully Created Account!")
  store.addNumUserStat()
  # user object is assigned 
  user = user.login(userList)
  # user object is updated in store class
  store.setUser(user)
  # menu is called
  userMenu(store)

elif newOrOld == 2:
  # user object assinged from userlist
  user = user.login(userList)
  # user object updated in store
  store.setUser(user)
  # user menu called
  userMenu(store)

elif newOrOld == 3:
  # admin login method called
  admin.login(userList)
  # admin menu displayed
  adminMenu(admin)
  


