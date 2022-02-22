from selenium import webdriver
from colorama import Fore
import random
import time
import os


PATH = "C:\chromedriver.exe"
options = webdriver.ChromeOptions()
#options.add_argument('--headless')
options.add_argument('--log-level=3')
driver = webdriver.Chrome(PATH, options=options)
os.system('cls')
os.system('cls')
Logged = False
log = ""
text = "______ _ _ _       _           _   \n\
|  ___(_| | |     | |         | |  \n\
| |_   _| | | ___ | |__   ___ | |_ \n\
|  _| | | | |/ _ \| '_ \ / _ \| __|\n\
| |   | | | | (_) | |_) | (_) | |_ \n\
\_|   |_|_|_|\___/|_.__/ \___/ \__|\n\
                                   "

def refresh_console():
    os.system('cls')
    print(Fore.WHITE + text)
    print(Fore.CYAN + "instagram: @filippocerchi\n")

def connection_error():
    refresh_console()
    print(Fore.RED + "\n[ERROR] Unable to connect to instagram servers, please try again")
    driver.quit()
    exit()

print(Fore.WHITE + text)
print(Fore.CYAN + "instagram: @filippocerchi")
print(Fore.BLUE + "\nConnecting to Instagram servers...")
try:
    driver.get("https://www.instagram.com")
except:
    connection_error()

def login():
    global driver
    global log
    global Logged

    if Logged == True:
        log = "You are already logged."
        return None
    refresh_console()

    user = input(Fore.GREEN + 'Enter your instagram username: ')
    while True:
        passw = input(Fore.GREEN + 'Enter your instagram password: ')
        if(len(passw) < 6):
            print(Fore.RED + "[LOG] Password must be at least 6 characters long.")
        else:
            break
    print(Fore.BLUE + "\nLogging in...")

    try:
        driver.find_element_by_xpath('/html/body/div[4]/div/div/button[1]').click()
    except:
        None
    time.sleep(random.randrange(3,5))
    driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input').send_keys(user)
    driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input').send_keys(passw)
    time.sleep(random.randrange(2,3))
    try:
        driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button').click()
    except:
        connection_error()
    time.sleep(random.randrange(2,3))
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div/div/button[2]").click()
        time.sleep(random.randrange(2,3))
    except:
        None
    try:
        driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div').click()
    except:
        time.sleep(random.randrange(1,3))
        try:
            errorLoginMessage = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/p").text
        except:
            None
        if "password" in errorLoginMessage:
            log = "Incorrect username or password."
            driver.refresh()
            return None
        else:
            refresh_console()
            print(Fore.RED + "[ERROR] Unable to login, please try again.")
            time.sleep(6)
            print(Fore.WHITE)
            driver.quit()
            exit()
    time.sleep(random.randrange(2,3))
    try:
        driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
    except:
        None

    log = "Logged in successfully!"
    loginValue = 0
    Logged = True

def logout():
    global driver
    global log
    global Logged

    if Logged == False:
        log = "You must be logged in."
        return None

    refresh_console()
    print(Fore.BLUE + "Logging out...")

    driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/span/img").click()
    time.sleep(random.randrange(1,2))
    driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/div[2]").click()

    log = "Logged out successfully!"
    Logged = False
    
def like_by_tag():
    global driver
    global Logged
    global log
    if Logged == False:
        log = "You must be logged in."
        return None
    validInput = False
    while validInput != True:
        try:
            refresh_console()
            tags = int(input(Fore.GREEN + "Enter how many tags (0 to go back): "))
            if tags < 0:
                log = "Invalid input."
                return None
            if tags == 0:
                driver.get("https://www.instagram.com")
                try:
                    time.sleep(random.randrange(2,4))
                    driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
                    return None
                except:
                    return None
            validInput = True
        except:
           None
    tag = []
    index = 1
    while index <= tags:
        tag.append(input("Enter tag [" + str(index) + "]: "))
        index = index + 1
    howMuchFollow = int(input("How many posts you want to like for each tag: " ))
    index = 0
    refresh_console()
    while index < tags:
        print(Fore.YELLOW + "\n#" + tag[index] + ":")
        try:
            driver.get("https://www.instagram.com/explore/tags/" + tag[index])
        except:
            log = "Tag not valid."
            return None
        index = index + 1
        x = 0
        row = 1
        post = 0
        previusPost = 0
        while x < howMuchFollow:
            post = random.randrange(1,3)
            while post == previusPost:
                post = random.randrange(1,3)

            time.sleep(random.randrange(2,5))
            try:
                driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div/div[" + str(row) + "]/div[" + str(post) + "]").click()
            except:
                print(Fore.RED + "Posts not found.")
                break
            previusPost = post
            time.sleep(random.randrange(2,5))
            driver.find_element_by_xpath("/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button").click()
            profile = driver.find_element_by_xpath("/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/div/span/a").text
            print(Fore.BLUE + "Liked the post to: " + profile)
            time.sleep(random.randrange(2,4))
            driver.find_element_by_xpath("/html/body/div[6]/div[1]").click()
            if((x - 1) % 2 == 0):
                row = row + 1
            x = x + 1
    driver.get("https://www.instagram.com")
    try:
        time.sleep(random.randrange(2,4))
        driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
    except:
        None
    print(Fore.GREEN + "\nFinished.")
    input(Fore.MAGENTA + "Press enter to continue...")

def follow_by_tag():
    global driver
    global Logged
    global log
    if Logged == False:
        log = "You must be logged in."
        return None
    validInput = False
    while validInput != True:
        try:
            refresh_console()
            tags = int(input(Fore.GREEN + "\nEnter how many tags (0 to go back): "))
            if tags < 0:
                log = "Invalid input."
                return None
            if tags == 0:
                driver.get("https://www.instagram.com")
                try:
                    time.sleep(random.randrange(2,4))
                    driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
                    return None
                except:
                    return None
            validInput = True
        except:
           None
    tag = []
    index = 1
    while index <= tags:
        tag.append(input("Enter tag [" + str(index) + "]: "))
        index = index + 1
    howMuchFollow = int(input("How many users you want to follow for each tag: " ))
    index = 0
    refresh_console()
    while index < tags:
        print(Fore.YELLOW + "\n#" + tag[index] + ":")
        try:
            driver.get("https://www.instagram.com/explore/tags/" + tag[index])
        except:
            log = "Tag not valid."
            return None
        index = index + 1
        x = 0
        row = 1
        post = 0
        previusPost = 0
        while x < howMuchFollow:
            post = random.randrange(1,3)
            while post == previusPost:
                post = random.randrange(1,3)

            time.sleep(random.randrange(2,5))
            try:
                driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div/div[" + str(row) + "]/div[" + str(post) + "]").click()
            except:
                print(Fore.RED + "Posts not found.")
                break
            previusPost = post
            time.sleep(random.randrange(2,5))
            driver.find_element_by_xpath("/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button").click()
            try:
                time.sleep(random.randrange(3,6))
                driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[3]/button[2]").click()
            except:
                None
            profile = driver.find_element_by_xpath("/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/div/span/a").text
            print(Fore.BLUE + "Following: " + profile)
            time.sleep(random.randrange(2,4))
            driver.find_element_by_xpath("/html/body/div[6]/div[1]").click()
            if((x - 1) % 2 == 0):
                row = row + 1
            x = x + 1
    driver.get("https://www.instagram.com")
    try:
        time.sleep(random.randrange(2,4))
        driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
    except:
        None
    print(Fore.GREEN + "\nFinished.")
    input(Fore.MAGENTA + "Press enter to continue...")

def follow_like_by_tag():
    global driver
    global Logged
    global log
    if Logged == False:
        log = "You must be logged in."
        return None
    refresh_console()
    validInput = False
    while validInput != True:
        try:
            refresh_console()
            tags = int(input(Fore.GREEN + "Enter how many tags (0 to go back): "))
            if tags < 0:
                log = "Invalid input."
                return None
            if tags == 0:
                driver.get("https://www.instagram.com")
                try:
                    time.sleep(random.randrange(2,4))
                    driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
                    return None
                except:
                    return None
            validInput = True
        except:
           None
    tag = []
    index = 1
    while index <= tags:
        tag.append(input("Enter tag [" + str(index) + "]: "))
        index = index + 1
    howMuchFollow = int(input("How many users you want to follow for each tag: " ))
    index = 0
    refresh_console()
    while index < tags:
        print(Fore.YELLOW + "\n#" + tag[index] + ":")
        try:
            driver.get("https://www.instagram.com/explore/tags/" + tag[index])
        except:
            log = "Tag not valid."
            return None
        index = index + 1
        x = 0
        row = 1
        post = 0
        previusPost = 0
        while x < howMuchFollow:
            post = random.randrange(1,3)
            while post == previusPost:
                post = random.randrange(1,3)

            time.sleep(random.randrange(2,5))
            try:
                driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div/div[" + str(row) + "]/div[" + str(post) + "]").click()
            except:
                print(Fore.RED + "Posts not found.")
                break
            previusPost = post
            time.sleep(random.randrange(2,5))
            driver.find_element_by_xpath("/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button").click()
            time.sleep(random.randrange(2,5))
            driver.find_element_by_xpath("/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]/button").click()
            try:
                time.sleep(random.randrange(3,6))
                driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[3]/button[2]").click()
            except:
                None
            profile = driver.find_element_by_xpath("/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/div/span/a").text
            print(Fore.BLUE + "Like & Following: " + profile)
            time.sleep(random.randrange(2,4))
            driver.find_element_by_xpath("/html/body/div[6]/div[1]").click()
            if((x - 1) % 2 == 0):
                row = row + 1
            x = x + 1
    driver.get("https://www.instagram.com")
    try:
        time.sleep(random.randrange(2,4))
        driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
    except:
        None
    print(Fore.GREEN + "\nFinished.")
    input(Fore.MAGENTA + "Press enter to continue...")

def comment_by_tag():
    global driver
    global Logged
    global log
    if Logged == False:
        log = "You must be logged in."
        return None
    refresh_console()
    validInput = False
    while validInput != True:
        try:
            os.system('cls')
            print(Fore.WHITE + text)
            print(Fore.CYAN + "instagram: @filippocerchi")
            tags = int(input(Fore.GREEN + "\nEnter how many tags (0 to go back): "))
            if tags < 0:
                log = "Invalid input."
                return None
            if tags == 0:
                driver.get("https://www.instagram.com")
                try:
                    time.sleep(random.randrange(2,4))
                    driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
                    return None
                except:
                    return None
            validInput = True
        except:
           None
    tag = []
    index = 1
    while index <= tags:
        tag.append(input("Enter tag [" + str(index) + "]: "))
        index = index + 1
    howMuchFollow = int(input("How many users you want to comment for each tag: " ))
    comment = input("Enter the comment: ")
    index = 0
    refresh_console()
    while index < tags:
        print(Fore.YELLOW + "\n#" + tag[index] + ":")
        try:
            driver.get("https://www.instagram.com/explore/tags/" + tag[index])
        except:
            log = "Tag not valid."
            return None
        index = index + 1
        x = 0
        row = 1
        post = 0
        previusPost = 0
        while x < howMuchFollow:
            post = random.randrange(1,3)
            while post == previusPost:
                post = random.randrange(1,3)

            time.sleep(random.randrange(2,5))
            try:
                driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div/div[" + str(row) + "]/div[" + str(post) + "]").click()
            except:
                print(Fore.RED + "Posts not found.")
                break
            previusPost = post
            time.sleep(random.randrange(2,5))
            driver.find_element_by_xpath("/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea").click()
            time.sleep(random.randrange(1,2))
            driver.find_element_by_xpath("/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea").send_keys(comment)
            time.sleep(random.randrange(2,4))
            driver.find_element_by_xpath("/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/button").click( )
            try:
                time.sleep(random.randrange(3,6))
                driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[3]/button[2]").click()
            except:
                None
            profile = driver.find_element_by_xpath("/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/div/span/a").text
            print(Fore.BLUE + "Commented the post to: " + profile)
            time.sleep(random.randrange(2,4))
            driver.find_element_by_xpath("/html/body/div[6]/div[1]").click()
            if((x - 1) % 2 == 0):
                row = row + 1
            x = x + 1
    driver.get("https://www.instagram.com")
    try:
        time.sleep(random.randrange(2,4))
        driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
    except:
        None
    print(Fore.GREEN + "\nFinished.")
    input(Fore.MAGENTA + "Press enter to continue...")


def unfollow():
    global log
    global Logged
    global driver
    if Logged == False:
        log = "You must be logged in."
        return None
    i = 0
    unfollowed = 0
    refresh_console()
    print(Fore.BLUE + "Loading...")
    validInput = False
    driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/span/img").click()
    time.sleep(random.randrange(1,3))
    driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[6]/div[2]/div[2]/div[2]/a[1]").click()
    time.sleep(random.randrange(1,3))
    following = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/div/span").text
    if "." in str(following):
        following = float(following)
        following = following * 1000
    following = int(following)
    halfGoal = False
    while validInput != True:
        try:
            refresh_console()
            print(Fore.BLUE + "Current following: " + str(following))
            if halfGoal == True:
                print(Fore.RED + "\n[LOG] For anti-ban reasons, you can unfollow at most half of your following.")
                unfollowedGoal = int(input(Fore.GREEN + "\nHow many users you want to unfollow (0 to go back): "))
                if(unfollowedGoal <= 0):
                    if(unfollowedGoal < 0):
                        log = "Invalid input."
                    driver.get("https://www.instagram.com")
                    try:
                        time.sleep(random.randrange(2,4))
                        driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
                    except:
                        None
                    return None
            else:
                unfollowedGoal = int(input(Fore.GREEN + "\nHow many users you want to unfollow (0 to go back): "))
                if(unfollowedGoal <= 0):
                    if(unfollowedGoal < 0):
                        log = "Invalid input."
                    driver.get("https://www.instagram.com")
                    try:
                        time.sleep(random.randrange(2,4))
                        driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
                    except:
                        None
                    return None
            if unfollowedGoal <= following / 2:
                validInput = True
            else:
                halfGoal = True
        except:
            None
    driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/div").click()

    while(True):
        x = random.randrange(1,4)
        i = i + x

        if unfollowed >= unfollowedGoal:
            log = "Unfollowed " + str(unfollowed) + " users."
            break

        time.sleep(random.randrange(2,5))
        if i >= 8:
            i = 1
            time.sleep(random.randrange(1,2))
            driver.refresh()
            time.sleep(random.randrange(2,4))
            driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/div").click()
            time.sleep(random.randrange(2,4))
        time.sleep(random.randrange(1,3))
        driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/ul/div/li[" + str(i) + "]/div/div[3]/button").click()
        time.sleep(random.randrange(2,4))
        driver.find_element_by_xpath("/html/body/div[7]/div/div/div/div[3]/button[1]").click()
        unfollowed = unfollowed + 1
    
    driver.get("https://www.instagram.com")
    try:
        time.sleep(random.randrange(2,4))
        driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
    except:
        None

def get_profile_data():
    global log
    global Logged
    global driver
    if Logged == False:
        log = "You must be logged in."
        return None
        
    validInput = False
    inputAttempts = False
    while validInput != True:
        refresh_console()
        if(inputAttempts == True):
            print(Fore.RED + "Invalid input.\n")
        userToSearch = input(Fore.GREEN + "Insert username: ")
        if("/" in userToSearch):
            validInput = False
            inputAttempts = True
        else:
            validInput = True
            inputAttempts = False
    print(Fore.BLUE + "\nLoading...")
    driver.get("https://www.instagram.com/" + userToSearch)
    time.sleep(random.randrange(1,3))
    try:
        driver.find_element_by_xpath("/html/body/div[4]/div/div/button[1]").click()
        time.sleep(random.randrange(2,4))
    except:
        None

    try:
        profileName = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/h2")
    except:
        try:
            profileName = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/h1")
        except:
            log = "User not found."
            return None
    try:
        posts = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[1]/div/span")
    except:
        posts = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[1]/a/div/span")

    try:
        followers = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/div/span")
    except:
        followers = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/div/span")

    try:
        following = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a/div/span")
    except:
        following = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/div/span")

    refresh_console()
    print(Fore.YELLOW + "Profile name: " + Fore.WHITE + profileName.text)
    print(Fore.YELLOW + "Posts: " + Fore.WHITE + posts.text)
    print(Fore.YELLOW + "Followers: " + Fore.WHITE + followers.text)
    print(Fore.YELLOW + "Following: " + Fore.WHITE + following.text)

    driver.get("https://www.instagram.com")
    try:
        time.sleep(random.randrange(1,3))
        driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
    except:
        None

    input(Fore.MAGENTA + "\nPress enter to continue...")
    

def choose(number):
    global driver
    global log
    if number == '0':
        refresh_console()
        print(Fore.MAGENTA + "Goodbye!")
        print(Fore.WHITE)
        time.sleep(1)
        driver.quit()
        exit()

    if number == '1':
        login()
        return None

    if number == '2':
        like_by_tag()
        return None
        
    if number == '3':
        follow_by_tag()
        return None
    
    if number == '4':
        follow_like_by_tag()
        return None

    if number == '5':
        comment_by_tag()
        return None

    if number == "6":
        unfollow()
        return None

    if number == '7':
        get_profile_data()
        return None

    if number == '8':
        logout()
        return None
    
    log = "Invalid input."

while(True):
    refresh_console()
    print(Fore.WHITE + "\
        " + Fore.YELLOW +"1)" + Fore.WHITE + " Login\n\
        " + Fore.YELLOW +"2)" + Fore.WHITE + " Like by tags\n\
        " + Fore.YELLOW +"3)" + Fore.WHITE + " Follow by tags\n\
        " + Fore.YELLOW +"4)" + Fore.WHITE + " Follow & Like by tags\n\
        " + Fore.YELLOW +"5)" + Fore.WHITE + " Comment by tags\n\
        " + Fore.YELLOW +"6)" + Fore.WHITE + " Unfollow\n\
        " + Fore.YELLOW +"7)" + Fore.WHITE + " Get profile data\n\
        " + Fore.YELLOW +"8)" + Fore.WHITE + " Logout\n\
        " + Fore.YELLOW +"0)" + Fore.WHITE + " Exit\n")
    if log != "":
        print(Fore.RED + "[LOG] " + log + "\n")
    n = input(Fore.GREEN + "Choose: ")
    log = ""
    choose(n)
