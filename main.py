from selenium import webdriver


def get_phrase(iterations, url):

    phrase = ''

    for i in range(iterations):
        driver = webdriver.Chrome()
        driver.get(url)
        two_words = driver.find_element_by_id('result').text
        phrase = phrase + two_words
        driver.close()

    return phrase.replace(" ", "")


print(get_phrase(2, 'http://watchout4snakes.com/wo4snakes/Random/RandomPhrase'))
