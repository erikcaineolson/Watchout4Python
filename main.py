from selenium import webdriver
import math
import random


def alpha_to_leet(character):
    """
    Uses some mapping from http://www.robertecker.com/hp/research/leet-converter.php to switch an alphabetical character
    to a numeric character. Utilizes some "standards" as well (like "3" for "E")

    :param string character:
    :return string:
    """
    swaps = {
        'a': 4,
        'A': 4,
        'b': 6,
        'B': 6,
        'e': 3,
        'E': '€',
        'i': '!',
        'I': '!',
        'l': 1,
        'L': '£',
        'o': 0,
        'O': 0,
        's': '$',
        'S': '$',
        't': 7,
        'T': 7,
        'x': '%',
        'X': '%'
    }

    leet = swaps.get(character)

    if leet is not None:
        return leet

    return str(character)


def get_phrase(iterations):
    """
    Retrieves a two-word phrase from the RandomPhrase page on the Watchout4Snakes website.

    :param int iterations:
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


def random_caps(any_case, upper_percent_chance=25):
    """
    Takes a string passed to it in any case, as well as an optional percentage of time you want lower-case letters, and
    returns a string with randomly capitalized letters.

    :param string any_case:
    :param int upper_percent_chance:
    :return string:
    """
    random.seed()
    string_length = len(any_case)
    random_case = ''

    for i in range(0, string_length):
        check_int = random.randrange(1, 100)

        if check_int <= upper_percent_chance:
            random_case += any_case[i].upper()
        else:
            random_case += any_case[i].lower()

    return random_case


def random_characters(alpha, numeric_percent_chance=20):
    """
    Randomly swaps characters in the string for numerals or symbols.

    :param string alpha:
    :param int numeric_percent_chance:
    :return string:
    """

    random.seed()
    string_length = len(alpha)
    alphanumeric = ''

    for i in range(0, string_length):
        check_int = random.randrange(1, 100)

        if check_int <= numeric_percent_chance:
            alphanumeric += str(alpha_to_leet(alpha[i]))
        else:
            alphanumeric += alpha[i]

    return alphanumeric


def main(word_count=2, use_caps=False, use_leet=False, caps_percent=25, leet_percent=20):
    """
    Scrape the site and get the password. Optionally specify more than four words, use caps, use leetspeak, and set the
    caps and leet percentages.

    :param int word_count:
    :param bool use_caps:
    :param bool use_leet:
    :param int caps_percent:
    :param int leet_percent:
    :return void:
    """
    iterations = int(math.ceil(word_count / 2))

    phrase = get_phrase(iterations)

    if use_caps:
        phrase = random_caps(phrase, caps_percent)

    if use_leet:
        phrase = random_characters(phrase, leet_percent)

    print(phrase)


print('Base example:')
main()

print('Advanced example (1 word, caps, leet, 50% caps percent and 90% leet percent):')
main(1, True, True, 50, 90)

print('Finally, a more likely example: 4 words, caps, no leet, default percentages:')
main(4, True)