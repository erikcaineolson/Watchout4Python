# Watchout4Python

Returns a more complex version of a Watchout4Snakes random phrase (to programmatically create passphrases).

## Goals
After reading XKCD's password comic, I found [http://watchout4snakes.com/wo4snakes/](Watchout4Snakes) (W4S), and immediately loved it. I figured I'd like to automate the process for use in other applications. So, here we are!

Also, I wanted to get a feel for some basic web scraping and string manipulation with Python.

## Requirements
1. Python >= 3.6 (I honestly didn't test it on a lower version of Python)
2. Selenium
3. chromedriver

Run `pip install selenium` if you don't have this library yet.

You will need to get the appropriate `chromedriver` file for your system from [https://sites.google.com/a/chromium.org/chromedriver/](https://sites.google.com/a/chromium.org/chromedriver/).

## Use
The current script simply prints the new password, but you can call the `main()` function as you see fit.

## Optional Parameters
`main()` takes the following optional parameters (in order):

|Parameter|Description|Default Value|
|---------|-----------|------------:|
|`word_count`|The total number of words desired in the output phrase. Currently, if you provide an odd number _n_, the program retrieves _n + 1_ words (due to the way W4S returns data and my laziness in not adding a word split for odd value counts).|2|
|`use_caps`|Whether the program should allow upper/lower case switching.|False|
|`use_leet`|Whether the program should allow 1337 speak switching.|False|
|`caps_percent`|The percent chance you want the program to swap a character to uppercase. _Technically defaults to 0 because `use_caps` defaults to False_|25|
|`leet_percent`|The percent chance you want the program to swap a character to 1337. _Technically defaults to 0 because `use_leet` defaults to False_|20|
