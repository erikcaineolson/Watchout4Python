from selenium import webdriver
import random


def get_phrase(iterations):
    """
    Retrieves a two-word phrase from the RandomPhrase page on the Watchout4Snakes website.

    :param iterations:
    :return string:
    """
    phrase = ''

    for i in range(iterations):
        driver = webdriver.Chrome()
        driver.get('http://watchout4snakes.com/wo4snakes/Random/RandomPhrase')
        two_words = driver.find_element_by_id('result').text
        phrase = phrase + two_words
        driver.close()

    return phrase.replace(" ", "")


def random_caps(any_case, lower_percent=75):
    """
    Takes a string passed to it in any case, as well as an optional percentage of time you want lower-case letters, and
    returns a string with randomly capitalized letters.

    :param any_case:
    :param lower_percent:
    :return string:
    """
    random.seed()
    string_length = len(any_case)
    random_case = ''

    for c in range(0, string_length):
        check_int = random.randrange(1, 100)

        if check_int <= lower_percent:
            random_case = random_case + any_case[c].lower()
        else:
            random_case = random_case + any_case[c].upper()

    return random_case


print(random_caps(get_phrase(1)))
#print(get_phrase(2))
