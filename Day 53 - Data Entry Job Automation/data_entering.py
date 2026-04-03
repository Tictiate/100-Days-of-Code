from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FormFiller:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")

        self.driver = webdriver.Chrome(options=chrome_options)

    def fill_form(self, links, addresses, prices):
        self.driver.get("https://forms.gle/AqGMDyfu5AYTXJWh8")

        wait = WebDriverWait(self.driver, 10)

        for i in range(len(addresses)):
            inputs = wait.until(EC.visibility_of_all_elements_located(
                (By.CSS_SELECTOR, 'input[type="text"]')
            ))

            inputs[0].send_keys(addresses[i])
            inputs[1].send_keys(prices[i])
            inputs[2].send_keys(links[i])

            submit_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//span[text()="Submit"]')
            ))
            submit_button.click()

            another_response = wait.until(EC.element_to_be_clickable(
                (By.LINK_TEXT, "Submit another response")
            ))
            another_response.click()