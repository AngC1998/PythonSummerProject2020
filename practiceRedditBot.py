# the following code is from sentdex about video on Reddit bots
# code is modified to suit practice and current bot testing
# https://www.youtube.com/watch?v=NRgfgtzIhBQ&t=218s

# import praw to use Reddit API
import praw

# Reddit object
reddit = praw.Reddit(client_id='WmmS1FTYJemKkA',
                     client_secret='MeorsyYJUlOZpaF_lOo5Ce59NbQ',
                     username='testtw132',
                     password='evillion',
                     user_agent='practice')

# subreddit for practice
subreddit = reddit.subreddit('Python')

# searching submissions with hot and printing their contents
hot_python = subreddit.hot(limit=3)


# function to showcase naive approach to reddit commenting
def naive_comment_chain():
    for submission in hot_python:
        # prints submission ID
        # print(submission)
        if not submission.stickied:
            # first two ignored because stickied, so limit would be n - 2
            print(submission.title)
            print('ups: {}, downs: {}, have visited: {}'.format(submission.ups, submission.downs, submission.visited))
            # now check out the comments and practice with them
            # so far only checks the topmost layer of comments (direct comments, not replies)
            comments = submission.comments
            for comment in comments:
                print(20 * '-')
                print(comment.body)
                # now check for comments in the main comment If reply string is above 0, is a reply.
                if len(comment.replies) > 0:
                    for reply in comment.replies:
                        # be sure to use reply.body, otherwise it uses the comment ID instead
                        print('REPLY: ', reply.body)
            # Now, the issue with the above code is that you don't know how large the reply chain a given
            # comment may contain, so we must use either an iterative loop or recursion to get the comment chain
            # So, we use a list command (part of the PRAW package) for list of comments


def better_comment_chain():
    # Better approach to longer reddit comment chains
    for submission in hot_python:
        # prints submission ID
        # print(submission)
        if not submission.stickied:
            # first two ignored because stickied, so limit would be n - 2
            print(submission.title)
            print('Submission ID: ', submission.id)
            print('ups: {}, downs: {}, have visited: {}'.format(submission.ups, submission.downs, submission.visited))
            # now check out the comments and practice with them
            # bit more wonky solution, but it works somehow
            submission.comments.replace_more(limit=0)
            comments = submission.comments.list()
            for comment in comments:
                print(20 * '-')
                print('Parent ID: ', comment.parent())
                print('Comment ID: ', comment.id)
                # Note: comment.body works for purely textual comments. Comments with emojis will
                # be an issue. To fight this, use: print(comment.body.encode("utf-8", errors='ignore'))
                print(comment.body)


# NEVER use these commands (because bots are not supposed to use them):
# .upvote()
# .downvote()


# streaming comments and submissions practice in r/politics
def stream_reddit():
    # stream comments
    sub = reddit.subreddit('politics')
    hot_pol = subreddit.hot(limit=1)
    for comment in sub.stream.comments():
        try:
            print(20 * '-')
            print(comment.body)
        except Exception as e:
            pass
    # stream submissions
    # for submission in sub.stream.submissions():
    #     try:
    #         print(20 * '-')
    #         print(submission.title)
    #     except Exception as e:
    #         print(str(e))


# functions to call for stuff:
# better_comment_chain()
# subreddit.subscribe()
stream_reddit()