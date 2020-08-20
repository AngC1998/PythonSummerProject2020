import praw
import pdb
import re
import os
from botKeys import *
import random

#Create the Reddit instance
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     username=username,
                     password=password,
                     user_agent=user_agent)

if not os.path.isfile('posts_replied_to.txt'):
    posts_replied_to = []
else:
    with open('posts_replied_to.txt', 'r') as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split('\n')
        posts_replied_to = list(filter(None, posts_replied_to))

#Have the bot say different things
#Add flexibility for subreddits
'''
subreddit = reddit.subreddit('UTAustin')
for submission in subreddit.hot():
    if submission.id not in posts_replied_to:
        if "CS" in submission.title:
            submission.reply("I am a bot, and I love UTCS. Hook em Horns")
            print('Bot replying to: ', submission.title)
            posts_replied_to.append(submission.id)
        elif "UT" in submission.title:
            submission.reply("Hook 'em horns!")
            print('Bot replying to: ', submission.title)
            posts_replied_to.append(submission.id)

subreddit_two = reddit.subreddit('kpop')
for submission in subreddit_two.hot():
    if submission.id not in posts_replied_to:
        if "ONEUS" in submission.title:
            submission.reply("The recent ONEUS comeback was great. Their choreography was awesome and their voices sound nice.")
            print('Bot replying to: ', submission.title)
            posts_replied_to.append(submission.id)
'''

def reply_bot(page, keywords, responses):
    subreddit_page = reddit.subreddit(page)
    for submission in subreddit_page.hot():
        if submission.id not in posts_replied_to:
            for keyword in keywords:
                if keyword in submission.title:
                    index = random.randint(0, len(responses)-1)
                    reply = responses[index]
                    submission.reply(reply)
                    print('Bot replying to: ', submission.title)
                    posts_replied_to.append(submission.id)

page = 'hello'
keywords = []
responses = []

while page != '-1':
    page = input('Enter in subreddit: ')
    keyword = 'hello'
    reply = 'hello'
    while keyword != '-1':
        keyword = input('Enter in keyword in title you want to find: ')
        if keyword != '-1':
            keywords.append(keyword)
    while reply != '-1':
        reply = input('Enter what response you want to generate:')
        if reply != '-1':
            responses.append(reply)
    if page == '-1':
        print('Reply bot will terminate.')
    else:
        reply_bot(page, keywords, responses)


with open('posts_replied_to.txt', 'w') as f:
    for post_id in posts_replied_to:
        f.write(post_id + '\n')
