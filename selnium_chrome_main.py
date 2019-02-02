#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import output_to_file as wf
import datetime
from datetime import date, timedelta
print(webdriver)
from selenium.webdriver.support.ui import WebDriverWait
import os
import importlib
importlib.import_module(credentials)

print(os.getcwd())


def main():
  """ Main program """
  # Code goes over here.


  date_begin = "20180101"
  date_end = "20180103"
  #date_range = '%3D{}%26_u.date01%3D{}%26'.format(date_begin, date_end)
  #example url for date range 20180101 to 20180101
  "https://analytics.google.com/analytics/web/#report/conversions-goal-funnel/a89859w27785432p26521297/%3F_u.date00%3D20180101%26_u.date01%3D20180101%26funnel_goaloption_1-graphOptions.primaryConcept%3Danalytics.goalConversionRate1/"

  #clearly AU
  '''
  baseurl = 'https://analytics.google.com/analytics/web/#report/conversions-goal-funnel/a89859w27785432p26521297/%3F_u.date00%3D'\
    + date_begin\
    + '%26_u.date01%3D'\
    + date_end\
    + '%26funnel_goaloption_1-graphOptions.primaryConcept%3Danalytics.goalConversionRate1/'
  '''
  #Clearly NZ
  baseurl = 'https://analytics.google.com/analytics/web/#report/conversions-goal-funnel/a89859w27785540p26521414/%3F_u.date00%3D'\
    + date_begin\
    + '%26_u.date01%3D'\
    + date_end


  xpaths = { 'usernameTxtBox' : '//*[@id="identifierId"]',
             'passwordTxtBox' : 'whsOnd zHQkBf',
             'nextButton' : '/html/body/div[1]/div[1]/div[2]/div[2]/div/div/div[2]/div/div/div[1]/div/content/span',
             'goalFunnel': '//*[@id="ID-funnel_goaloption_1-goalFunnel"]',
             'goalFunnelbakbak': '/html/body/div[1]/div[2]/div/div[1]/div/div[4]/div[2]/div/div/div/div[2]/div/div[1]/div[3]/div/div[5]/div/table/tbody/tr[1]/td[2]',
             'viewNamebak':'//*[@id="suite-top-nav"]/suite-header/div/md-toolbar/div/suite-universal-picker/button/div[1]/div[2]/span/span',
             'viewName' : '/html/body/div[2]/div[1]/suite-header/div/md-toolbar/div/suite-universal-picker/button'

           }




  print(baseurl)


  driver = webdriver.Chrome('/Users/rhysall/PycharmProjects/Selenium_Chrome/chromedriver')  # Optional argument, if not specified will search path.
  driver.implicitly_wait(15)  # seconds
  actions = ActionChains(driver)

  #customizable stuff
  url_tokens = {
    1: 'https://analytics.google.com/analytics/web/#report/conversions-goal-funnel/a89859w27785540p26521414/%3F_u.date00%3D',
    2: '%26_u.date01%3D',
    3: ''
  }
  # create date range
  d1 = datetime.date(2017, 5, 25)  # start date
  d2 = datetime.date(2018, 5, 25)  # end date
  delta = d2 - d1  # timedelta
  dates = [(d1 + timedelta(x)).strftime('%Y%m%d') for x in range(delta.days)]
  print(dates)
  first_page = "{}{}{}{}" \
    .format(
    url_tokens[1],
    dates[0],
    url_tokens[2],
    dates[0]
  )
  print(first_page)
  driver.get(first_page)

  #Actions!
  driver.find_element_by_xpath(xpaths['usernameTxtBox']).click()  #Click Login button
  driver.find_element_by_xpath(xpaths['usernameTxtBox']).clear()  #fill in username box
  driver.find_element_by_xpath(xpaths['usernameTxtBox']).send_keys(username)  #type username
  driver.find_element_by_xpath(xpaths['nextButton']).click()  #click next
  time.sleep(3)
  actions.send_keys(password)  #type password
  actions.perform()
  driver.find_element_by_xpath(xpaths['nextButton']).click()  #click next
  time.sleep(20)

  #get stuff
  funnel_frame = driver.find_element_by_id('galaxyIframe')
  driver.switch_to.frame(funnel_frame)
  #print(funnel_frame)
  time.sleep(5)
  text = driver.switch_to.active_element.text
  print(text)
  text=""
  fullData = []
  #driver.switch_to.default_content()
  for i, date in enumerate(dates):
    wf.main(date, text)
    result = None
    while result is None:
      try:
        next_url = "{}{}{}{}" \
          .format(
          url_tokens[1],
          dates[i],
          url_tokens[2],
          dates[i]
        )
        print("next url", next_url)
        # connect
        driver.get(next_url)
        ##WebDriverWait(driver,10).until(
        #  lambda driver: driver.find_element_by_name('galaxyIframe'))
        #funnel_frame = driver.find_element_by_name('galaxyIframe')
        #driver.switch_to.frame(funnel_frame)
        #text = driver.switch_to.active_element.text
        #print(text)

        time.sleep(10)
        funnel_frame = driver.find_element_by_id('galaxyIframe')
        driver.switch_to.frame(funnel_frame)
        text = driver.switch_to.active_element.text
        time.sleep(2)
        result = 1
      except:
        pass

  time.sleep(50)




if __name__ == "__main__":
  main()