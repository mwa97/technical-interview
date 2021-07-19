from selenium import webdriver

drive = webdriver.Chrome(
    executable_path='/Users/waleed/PycharmProjects/selenium_python/venv/bin/chromedriver ')

url = 'https://www.ulta.com/hair-treatment-masks?N=27fu'

drive.get(url)


hair = drive.find_elements_by_class_name('productQvContainer')


for hair in hair:
    elements = hair.find_element_by_xpath(
        '//*[@id="canada"]/div[6]/div/div[2]').text

    print(elements)
