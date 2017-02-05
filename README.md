# Watchout4Python

Returns a more complex version of a Watchout4Snakes random phrase.

## Goals
After reading XKCD's password comic, I found [http://watchout4snakes.com/wo4snakes/](Watchout4Snakes), and immediately loved it. I figured I'd like to automate the process for use in other applications. So, here we are!

Also, I wanted to get a feel for some basic web scraping with Python.

## Requirements
1. Python 3._x_
2. Selenium
3. chromedriver

Run `pip install selenium` if you don't have this library yet.

You will need to get the appropriate `chromedriver` file for your system from [https://sites.google.com/a/chromium.org/chromedriver/](https://sites.google.com/a/chromium.org/chromedriver/).

## Use
The current script simply prints the new password, but you can call the `get_phrase()` function as you see fit.
