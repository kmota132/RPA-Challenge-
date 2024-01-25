import os
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import json

J = {}

class BotNoticias():

    def __init__(self):
        self.setup_browser()

    def setup_browser(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")

        chrome_service = ChromeService(ChromeDriverManager().install())
        self.navegador = webdriver.Chrome(service=chrome_service, options=chrome_options)
        self.navegador.maximize_window()

    def scrap(self):

        n = 0
        while n == 0:
            try:
                self.navegador.get('https://www.nytimes.com/')     
                n = 1              
            except Exception as error:
                time.sleep(2)

        n = 0
        while n == 0:
            try:
                self.navegador.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[2]/header/section[1]/div[1]/div[2]/button').click()
                n = 1              
            except Exception as error:
                time.sleep(2)
        
        n = 0
        while n == 0:
            try:
                self.navegador.find_element(By.XPATH,'//*[@id="search-input"]/form/div/input').send_keys('Today')
                n = 1              
            except Exception as error:
                time.sleep(2)

        n = 0
        while n == 0:
            try:
                self.navegador.find_element(By.XPATH,'//*[@id="search-input"]/form/button').click()
                n = 1              
            except Exception as error:
                time.sleep(2)


        n = 0
        while n == 0:
            try:
                self.navegador.find_element(By.XPATH,'//*[@id="site-content"]/div/div[1]/div[2]/div/div/div[1]/div/div/button').click()
                n = 1              
            except Exception as error:
                time.sleep(2)

        n = 0
        while n == 0:
            try:
                self.navegador.find_element(By.XPATH,'//*[@id="site-content"]/div/div[1]/div[2]/div/div/div[2]/div/div/button').click()
                n = 1              
            except Exception as error:
                time.sleep(2)

        n = 0
        while n == 0:
            try:
                self.navegador.find_element(By.XPATH,'//*[@id="site-content"]/div/div[1]/div[2]/div/div/div[2]/div/div/div/ul/li[5]/label').click()
                n = 1              
            except Exception as error:
                print(f"Erro ao selecionar topico: {e}")
                time.sleep(2)  
                
        n = 0
        while n == 0:
            try:
                self.navegador.find_element(By.XPATH,'//*[@id="site-content"]/div/div[1]/div[2]/div/div/div[3]/div/div/button').click()
                n = 1              
            except Exception as error:
                print(f"Erro ao selecionar  type : {e}")
                time.sleep(2)   

        n = 0
        while n == 0:
            try:
                self.navegador.find_element(By.XPATH,'//*[@id="site-content"]/div/div[1]/div[2]/div/div/div[3]/div/div/div/ul/li[2]/label').click()
                n = 1              
            except Exception as error:
                print(f"Erro ao selecionar  article: {e}")
                time.sleep(2)     

        n = 0
        while n == 0:
            try:
                noticias  = self.navegador.execute_script("""
                        var schedule = document.querySelector('[class="css-8xl60i"]');
                        var rows = schedule.querySelectorAll('.css-1l4w6pd');
                        var authors = schedule.querySelectorAll('.css-15w69y9');
                        var descriptions = schedule.querySelectorAll('.css-16nhkrn');
                        var noticias = [];

                        rows.forEach(function(row, index) {
                            var dataElement = row.querySelector('.css-17ubb9w');
                            var titleElement = row.querySelector('.css-2fgx4k');
                            var authorElement = authors[index];
                            var descriptionElement = descriptions[index];

                            if (dataElement && titleElement && authorElement && descriptionElement) {
                                noticias.push({
                                    data: dataElement.innerText,
                                    title: titleElement.innerText,
                                    author: authorElement.innerText.replace(/By/g, ""), 
                                    description: descriptionElement.innerText
                                });
                            }
                        });
                        var jsonDataCombined = { noticias: noticias };
                        var jsonStringCombined = JSON.stringify(jsonDataCombined, null, 2);

                        return jsonStringCombined;
                     """)
                n = 1              
            except Exception as error:
                print(f"Erro ao buscar as notias: {e}")
                time.sleep(2) 
            
            print(noticias)


            J['noticias'] = noticias
            n = 0
            while n == 0:   
                try:
                    jsonString = json.dumps(J)
                    json_file = open('super_json.json', 'w')
                    json_file.write(jsonString)
                    json_file.close()
                    super_json = str(J).replace('"', '').replace("'", '"').replace("\\", "").replace('"None"', '"Null"').replace("None", '"Null"').replace("\n", '')
                    n = 1

                except Exception as e:
                        print(f"Erro: {e}")

        
        input('1')

if __name__ == "__main__":
    try:
        bot_noticias = BotNoticias()
        bot_noticias.scrap()
    except Exception as e:
        print(f"Erro: {e}")


    finally:
        bot_noticias.navegador.quit()
