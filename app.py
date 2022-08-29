from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

target_username = "username"
target_password = "password"
target_button = "/html/body/div/div[2]/div/form/div[4]/div/button"
target_buger = "/html/body/nav/div/div[1]/a[1]"

login_username = "Dewa.nich@gmail.com"
login_password = "dewa=k1d"

def main():
    # Define Variable that needed for Automation
    url = "https://tripisia.id/cms"
    url_login = "https://tripisia.id/cms/dashboard"
    url_post = "https://tripisia.id/cms/dashboard/add_poi"
    opts = webdriver.FirefoxOptions()
    opts.add_argument("--width=1024")
    opts.add_argument("--height=800")
    driver = webdriver.Firefox(options=opts)
    driver.get(url)

    # Get Username Input Field and Insert a valid Username
    WebDriverWait(driver, timeout=5).until(EC.presence_of_all_elements_located((By.NAME, target_username)))
    username_input = driver.find_element(By.NAME, target_username)
    username_input.send_keys(login_username)

    # Get Password Input Field and Insert a valid Password
    WebDriverWait(driver, timeout=5).until(EC.presence_of_all_elements_located((By.NAME, target_password)))
    password_input = driver.find_element(By.NAME, target_password)
    password_input.send_keys(login_password)

    # Get Button and Push the submit Button
    WebDriverWait(driver, timeout=5).until(EC.presence_of_all_elements_located((By.XPATH, target_button)))
    button = driver.find_element(By.XPATH, target_button)
    button.click()

    # Get Burger Toggle and Push the Burger
    WebDriverWait(driver,10).until(lambda driver : driver.current_url == url_login)
    driver.get(url_post)

   
    
if __name__ == "__main__":
    main()
