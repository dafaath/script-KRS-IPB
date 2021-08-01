import requests
import time
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException


def main(username, password, jadwal):
    # Script Author: Dafa Athaullah KOM 56, jika mau makai harap izin dulu
    print("Script Author: Dafa Athaullah KOM 56, jika mau makai harap izin dulu")
    urllogin = "https://krs.simak.ipb.ac.id/login"

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(urllogin)
    driver.maximize_window()
    userInput = driver.find_element_by_id("input-username")
    userInput.send_keys(username)
    passwordInput = driver.find_element_by_id("input-password")
    passwordInput.send_keys(password)
    passwordInput.send_keys(Keys.RETURN)
    time.sleep(2)
    continue_link = driver.find_element_by_partial_link_text('Isi')
    continue_link.click()

    # Kode Matkul, Pararel Kuliah, Pararel Praktikum

    for j in jadwal:
        searchmatkul = driver.find_element_by_id("__BVID__52")
        searchmatkul.clear()
        searchmatkul.send_keys(j['matkul'])
        time.sleep(1)
        ambil = driver.find_element_by_xpath(
            "//button[contains(text(),'Ambil')]")
        ambil.click()
        time.sleep(0.5)
        kuliahselector = Select(driver.find_element_by_xpath(
            "//label[contains(text(),'Kuliah')]//parent::*//following-sibling::*//child::*"))
        kuliahselector.select_by_value(j['kuliah'])
        isPraktikumExist = checkElementExistByXpath(driver,
                                                    "//label[contains(text(),'Praktikum')]//parent::*//following-sibling::*//child::*")
        isResponsiExist = checkElementExistByXpath(driver,
                                                   "//label[contains(text(),'Responsi')]//parent::*//following-sibling::*//child::*")
        if isPraktikumExist:
            praktikumselector = Select(driver.find_element_by_xpath(
                "//label[contains(text(),'Praktikum')]//parent::*//following-sibling::*//child::*"))
            praktikumselector.select_by_value(j['praktikum'])
        elif isResponsiExist:
            responsiselector = Select(driver.find_element_by_xpath(
                "//label[contains(text(),'Responsi')]//parent::*//following-sibling::*//child::*"))
            responsiselector.select_by_value(j['praktikum'])
        simpanbutton = driver.find_element_by_xpath(
            "//span[contains(text(),'Simpan')]//parent::button")
        time.sleep(0.5)
        simpanbutton.click()
    quit()

    # isolated = [j for j in jadwal if j["matkul"] == 'KOM335']

    # for j in isolated:


def checkElementExistByXpath(driver, xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True


if __name__ == "__main__":
    with open("config.json") as f:
        data = json.load(f)
        main(data['username'], data['password'], data['jadwal'])
