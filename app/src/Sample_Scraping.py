import time
from selenium import webdriver

# Chrome のオプションを設定する
options = webdriver.ChromeOptions()
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Remote( command_executor='http://chrome:4444/wd/hub', desired_capabilities=options.to_capabilities(), options=options)

#googleにアクセス
driver.get('https://google.com/')

#スクショ
driver.save_screenshot('/app/data/cap.png')

#スリープ
time.sleep(1)

#自動終了
driver.close()
driver.quit()
