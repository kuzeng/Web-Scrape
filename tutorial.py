from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "./chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://www.linkedin.com/")
# Log in to linkedin
username = input("Please enter your Linkedln username: ")
password = input("Please enter your Linkedln password: ")
usernameInput = driver.find_element_by_id("session_key")
usernameInput.send_keys(username)
passwordInput = driver.find_element_by_id("session_password")
passwordInput.send_keys(password)

signinBtn = driver.find_element_by_class_name("sign-in-form__submit-button")
signinBtn.click()

# navigate to message page
try:
    messagingLink = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "ember29"))
    )
    messagingLink.click()
except:
    driver.quit()

# scrape the message content 
try:
    messagesPanel = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "msg-conversations-container"))
    )

    messages = messagesPanel.find_elements_by_class_name("msg-conversations-container__pillar")
    for message in messages:
        messengerName = message.find_element_by_class_name("msg-conversation-card__participant-names")
        messageTime = message.find_element_by_class_name("msg-conversation-card__time-stamp")
        messageText = message.find_element_by_class_name("msg-conversation-card__message-snippet")
        print("Messenger name: " + messengerName.text,
              "Message time: " + messageTime.text,
              "Message content: " + messageText.text, sep='\n')
        print("--------------------------\n")
except:
    driver.quit()

time.sleep(20)

driver.quit()
