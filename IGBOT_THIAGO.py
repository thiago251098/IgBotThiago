from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        #self.driver = webdriver.Firefox(executable_path="C:\\Users\\Thiag\\OneDrive\\Documents\\geckodriver-v0.24.0-win64\\geckodriver.exe")
    
    def login(self):
        count_comments = 0
        count_pages = 0
        #while True:
        count_pages += 1
        print(count_pages, " paginas abertas")
        time.sleep(5)
        page = False
        driver = webdriver.Firefox(executable_path="C:\\Users\\Thiag\\OneDrive\\Documents\\geckodriver-v0.24.0-win64\\geckodriver.exe")
        url_photo = "https://www.instagram.com/p/CLBBxN2BXS-/"
        while page == False:
            try:
                driver.get(url_photo)
                page = True
            except:
                page=False
                print("Connection recusada..")
                print("espere 3 seg")
                print("ZZzzzz...")
                time.sleep(3)
                continue
        field_entrar = driver.find_element_by_xpath("//button[contains(text(), 'Entrar')]").click()
        time.sleep(10)
        field_user = driver.find_element_by_xpath("//input[@name='username']")
        field_user.click()
        field_user.clear()
        field_user.send_keys(self.username)
        field_password = driver.find_element_by_xpath("//input[@name='password']")
        field_password.clear()
        field_password.click()
        field_password.send_keys(self.password)
        field_password.send_keys(Keys.RETURN)
        time.sleep(10)
        end_while = False
        while end_while == False:
            time.sleep(5)
            ret = self.comment(url_photo, driver)
            count_comments += 1
            print(count_comments, " comentarios feitos")
            if ret["ok"] is False:
                end_while = True
            #    driver.close()


    @staticmethod
    def comment_like_person(field, phrase):
        for letra in phrase:
            field.send_keys(letra)
            time.sleep(random.randint(1,5)/30)

    def comment(self, link, driver):
        try:
            comments = ["vamo que vamo", "esse ja é meu", "se deus quiser", "eu quero", "vou ganhar", "quero muito", "vamooo", "sorte :)", "tomara :D", "vemmm", "pode vimm"]
            driver.find_element_by_class_name('Ypffh').click()
            field_comment = driver.find_element_by_class_name('Ypffh')
            time.sleep(2)
            self.comment_like_person(field_comment, random.choice(comments))
            time.sleep(2)
            driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()
            return {"ok": True}
        except: #Exception as e:
            time.sleep(60)
            print("aguardando 60seg para dar refresh na pagina")
            try:
                #driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()
                driver.refresh()
                return {"ok": True}
            except:
                print("driver.refresh deu pau")
                return {"ok": False}
            
thiagoBot = InstagramBot("", "")
thiagoBot.login()