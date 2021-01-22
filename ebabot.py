from selenium import webdriver
import time
from random import choice


tc = input("Tc Kimlik Numaranız: ") 
ebasifre = input("Eba Şifreniz: ")

browser = webdriver.Chrome()
browser.get("https://giris.eba.gov.tr/EBA_GIRIS/giris.jsp")

def ebagirisi():
    tckimlik = browser.find_element_by_name("tckn")
    sifre = browser.find_element_by_name("password")
    tckimlik.send_keys(tc)
    sifre.send_keys(ebasifre)
    time.sleep(1)
    giris_yap = browser.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[2]/form/div[5]/button")
    giris_yap.click()
    time.sleep(5)
# Eba'da gelen bazı çalışmalar hatalı olduğu için anasayfadaki 3 çalışmadan birine random gidiyor.
def birincibuton():
    time.sleep(1)
    birincibuton = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div[1]/div/div[4]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div[3]/div/div[2]/div[3]/div[2]/div[1]")
    birincibuton.click()
    print("Ebada 10 Puan Kazandın ! |1| ")


def ikincibuton():
    ikincibuton = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div[1]/div/div[4]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div[3]/div/div[2]/div[2]/div[2]/div[1]")
    ikincibuton.click()
    print("Ebada 10 Puan Kazandın ! |2|")


def ucuncubuton():
    ucuncubuton = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div[1]/div/div[4]/div/div/div[2]/div/div/div/div[2]/div/div[1]/div[3]/div/div[2]/div[1]/div[2]/div[1]")
    ucuncubuton.click()
    print("Ebada 10 Puan Kazandın ! |3|")

def puankazan():
    randombuton = [birincibuton, ucuncubuton, ikincibuton]
    choice(randombuton)()
    time.sleep(7)
    videodancik = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div[1]/div/div[4]/div/div/div[1]/div/div/a/i")
    videodancik.click()

ebagirisi()
# Giriş yaptıktan sonra sürekli olarak puan kazanması için döngüye aldım
while True:
    try:
        puankazan()
        time.sleep(2)
    except:
        #Çalışma hatalı çıktığı zaman çalışmadan çıkarak 'countine' ile işlemi tekrarlıyor
        istisna = browser.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/a[2]")
        istisna.click()
        continue


