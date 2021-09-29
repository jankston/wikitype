
'''
- selects random wikipedia article and prints the summary and has the user copy them as fast as possible, returns WPM and characters per second 
'''
import requests
import wikipedia
import time
import datetime
import string


class Wikitype:
    def __init__(self):
        self.article = self.check_restrictions()
        self.summ = wikipedia.summary(self.article)
        self.summ_word_count = len(self.summ.split())
        self.summ_word_list = []
        self.entry = ''

    def check_restrictions(self, max_word_count=50): # TODO: Add english/ASCII tests
        safe_article = wikipedia.random(pages=1)
        try:
            if len(wikipedia.summary(safe_article).split()) > max_word_count:
                print('Max word count exceeded. Finding new article...')
                return self.check_restrictions()
        except:
            print('Error, finding new article...')
            self.check_restrictions()
        else:
            print(str(len(wikipedia.summary(safe_article).split())))
            return safe_article

    def get_entry(self):
        self.entry = input()

    def countdown(self, time_left = 3, sleep_time=2):
        # counts down from time_left value to 0 at intervals of sleep_time's value
        # then prompts user to start typing
        for time_left in range(time_left,0,-1):
            print(str(time_left) + '...')
            time.sleep(sleep_time)
        print('GO!')

    def start_clock(self):
        # "starts" clock and saves current time for calculating user stats
        self.start_time = time.time()

    def stop_clock(self):
        # "stops" clock and saves current time for calculating user stats
        self.stop_time = time.time()

    def calculate_time(self):
        # calculates and returns time to took for user to type the article summary
        # should always be called after start_clock() and stop_clock(); rounds to 3rd decimal place
        self.elapsed_time = round(self.stop_time - self.start_time, 3)

    def calculate_stats(self):
        self.wpm = round(len(self.entry.split())*(60.0/self.elapsed_time), 2)
        self.cps = round(len(self.entry)/self.elapsed_time, 2)
        print('Words per minute: ' + str(self.wpm))
        print('Characters per second: ' + str(self.cps))

    # first argument is OG article summary, second argument is the user entry
    # compares the two strings and returns inconsistencies 

'''
    def error_count(self):
        # compares the results of entry and summ to find differences between the strings

        i = 0
        g = 0
        misspell_ct = 0
        error_list = []

        while g < get_article_word_ct+1:
            if get_article_word_list[i] == user_entry[i]:
                i+=1
            else:
                error_list.append(summ_split[i])
                misspell_ct+=1
                i+=1
        
        print('--------------------------------------')
        print('Characters in original summary: ' + str(len(article_summ)))
        print('Characters in user entry: ' + str(len(user_entry)))
        print('--------------------------------------')
        print('Words in original summary: ' + str(get_article_word_ct))
        print('Words in user entry: ' + str(get_entry_word_ct))
        print('--------------------------------------')
        print(str(misspell_ct) + ' misspelled word(s)')
        
        if len(article_summ) > len(user_entry):
            missing_char_ct = len(article_summ) - len(user_entry)
            print('Missing ' + str(missing_char_ct) + ' character(s)')
        elif len(article_summ) < len(user_entry):
            extra_char_ct = len(user_entry) - len(article_summ)
            print(str(extra_char_ct) + ' extra character(s)')
        else:
            print('0 missing/extra characters')
        
        print(error_list)
'''

def main():
    test = Wikitype()
    print(test.article)
    print('--------------------------------------------')
    print(test.summ)
    test.countdown()
    test.start_clock()
    test.get_entry()
    test.stop_clock()
    test.calculate_time()
    test.calculate_stats()

main()