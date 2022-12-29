from selenium import webdriver
from time import sleep


url = 'https://ap.kh.usc.edu.tw/STU1/EASG/GB0101.aspx'
options = webdriver.EdgeOptions()
options.add_experimental_option('detach', True)  #不自动关闭浏览器
# options.add_argument('--start-maximized')#浏览器窗口最大化
driver = webdriver.Edge(options=options)
driver.get(url)
uid = "a108510336"
psw = "1106t125737907"
driver.find_element('xpath', '//*[@id="txtMyId"]').send_keys(uid)
driver.find_element('xpath', '//*[@id="txtMyPd"]').send_keys(psw)
driver.find_element('xpath', '//*[@id="btnLogin"]').click()
driver.find_element('xpath', '/html/body/form/div[3]/div/div[2]/div[2]/div[4]/div/div/table/tbody/tr[2]/td[7]/a').click()
driver.get('https://ap.kh.usc.edu.tw/STU1/EASG/GB0101.aspx')
for i in range(2,13):
    driver.find_element('xpath', '//*[@id="Preview_t2"]/tbody/tr[{}]/td[5]/input[1]').format(i).click()

# sleep(10)
# driver.quit()
# driver.find_element_by_xpath('//*[@id="content"]/div/div/ul/li[1]/a').click()
# //*[@id="Preview_t2"]/tbody/tr[2]/td[5]/input[1]
# //*[@id="Preview_t2"]/tbody/tr[3]/td[5]/input[1]
# //*[@id="Preview_t2"]/tbody/tr[13]/td[5]/input[1]