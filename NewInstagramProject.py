from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager as CM
from selenium.common.exceptions import NoSuchElementException
import time
import keyboard
import random


MIN = 0.1
MAX = 10
Username = input("What's your Username? ")
Password = input("What's your Password? ")
webdriver_path = r'C:\Users\Neria\Downloads\chromedriver_win32\chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument("--log-level=3")
mobile_emulation = {
        "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/90.0.1025.166 Mobile Safari/535.19"}
options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(executable_path=CM().install(), options=options)
# Open a different website (e.g., "https://www.example.com")
url = "https://www.instagram.com/accounts/login/"
driver.get(url)

def login(username:str, password:str):
    try:
        element = driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[3]/div[2]/button")
        element.click()
    except NoSuchElementException:
        print("[Info] - Instagram did not require to accept cookies this time.")
    Username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[aria-label="Phone number, username, or email"]')))
    Username_input.send_keys(username)
    password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[aria-label="Password"]')))
    password_input.send_keys(password)
    login_button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    login_button.click()
    print(f"[INFO] - The Login to {username} was succesful")
    time.sleep(10)

def Unfollow():
    Set = []
    with open(f"{Username}_NotFollowingBack.txt", 'r') as file:
        for line in file:
            Set.append(line.strip())
    driver.get(f"https://www.instagram.com/{Username}/")
    time.sleep(random.randint(5,10))
    driver.get(f"https://www.instagram.com/{Username}/following")
    time.sleep(random.randint(5,10))
    print(f"Your Unfollowers are: {Set}")

    for i in range(50):
        try:
            Name_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[aria-label="Search input"]')))
            name = Set[i]
            time.sleep(random.randint(0,3))
            Name_input.send_keys(name)
            #class=" _acan _acap _acat _aj1- _ap30"
            Unfollow_button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class=' _acan _acap _acat _aj1- _ap30']")))
            Unfollow_button.click()
            #class="_a9-- _ap36 _a9-_"
            Unfollow_fully_button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[class='_a9-- _ap36 _a9-_']")))
            Unfollow_fully_button.click()
            print(f"[INFO] - Unfollowed {name}")
            time.sleep(random.randint(2,4))
            Name_input.clear()
        except IndexError as indexerror:
            print("[DONE] - Done, there is no one else to unfollow")
            break
        except Exception as ex:
            print(f"[INFO] - Couldn't find any following user called {name}")
            Name_input.clear()
            continue
    with open(f"{Username}_NotFollowingBack.txt", 'w') as file:
        for i in range(50,len(Set)): 
            try:
                file.write(str(Set[i]) + '\n')
            except IndexError as indexeror:
                file.write("")
                break


def is_at_bottom(driver, div_element):
    # Get the current scroll position
    current_scroll_position = driver.execute_script("return arguments[0].scrollTop;", div_element)
    
    # Get the maximum scroll position (scrollHeight)
    max_scroll_position = driver.execute_script("return arguments[0].scrollHeight;", div_element)
    
    # Check if at the bottom
    return current_scroll_position >= max_scroll_position

def Followers():
    url = f"https://www.instagram.com/{Username}/"
    driver.get(url)
    time.sleep(6)
    #//*[@id="mount_0_0_Bf"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/ul/li[2]/a/span

    element = driver.find_element(By.XPATH, '//*[@id="mount_0_0_Bf"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/ul/li[2]/a/span')   
    element.click()
    time.sleep(4)
    #<div class="_aano"
    div_element = driver.find_element(By.CLASS_NAME, "_aano")
    while not is_at_bottom(driver,div_element):
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", div_element)
        time.sleep(random.randint(3,7))
    #<a class="x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk x78zum5 xdl72j9 xdt5ytf x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt xnz67gz x14yjl9h xudhj91 x18nykt9 xww2gxu x9f619 x1lliihq x2lah0s x6ikm8r x10wlt62 x1n2onr6 xzfakq x7imw91 x1j8hi7x x5aw536 x194ut8o x1vzenxt xd7ygy7 xt298gk xynf4tj xdspwft x1r9ni5o x1d52zm6 xoiy6we x15xhmf9 x1qj619r x15tem40 x1xrz1ek x1s928wv x1n449xj x2q1x1w x1j6awrg x162n7g1 x1m1drc7 x1ypdohk x4gyw5p _a6hd"
    AllDives = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[class='_ap3a _aaco _aacw _aacx _aad7 _aade']")))
    Array = []
    for i in AllDives:
        Array.append(i.text)
    with open(f"{Username}_Following", "w") as file:
        for i in range(len(Array)):
            file.write(Array[i])


login(Username, Password)
Followers()