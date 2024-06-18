from selenium import webdriver
from selenium.webdriver.common.by import By 

tema = input('Digite o tema que deseja pesquisar: ')
url = 'https://pt.wikipedia.org/wiki/Wikip%C3%A9dia:P%C3%A1gina_principal'
driver = webdriver.Chrome()
driver.get(url)
if driver.find_element(By.XPATH,'//*[@id="p-search"]/a/span[1]'):
    driver.find_element(By.XPATH,'//*[@id="p-search"]/a/span[1]').click()
search_box = driver.find_element(By.NAME,"search")
search_box.send_keys(tema)
search_box.submit()
if driver.find_elements(By.XPATH,'//*[@id="disambig"]/table/tbody/tr/td[1]/span/a/img'):
    driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/ul/li[1]/a').click()
elif driver.find_elements(By.XPATH,'//*[@id="firstHeading"]')[0].text == "Resultados da pesquisa":
    if driver.find_elements(By.XPATH,'//*[@id="mw-content-text"]/div[3]/div[4]/ul/li[1]/div[2]/div[2]/div[1]/a'):
        driver.find_element(By.XPATH,'//*[@id="mw-content-text"]/div[3]/div[4]/ul/li[1]/div[2]/div[2]/div[1]/a').click()
print(driver.find_elements(By.ID,'footer-info-lastmod')[0].text)