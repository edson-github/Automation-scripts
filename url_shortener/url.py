# Title :- URL Shortener
# The URL shortener is application which takes url input from user and shorts it
import pyshorteners
import sys


# url converter function
def make_short(url):
    return pyshorteners.Shortener().tinyurl.short(url)


# this will take multiple url as input
def main():
    for cooked_url in map(make_short, sys.argv[1:]):
        print(cooked_url)


if __name__ == '__main__':
    main()
