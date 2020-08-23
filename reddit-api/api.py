import praw

reddit = praw.Reddit(client_id = 'M0r2Lz_sW0GAig',
                    client_secret = 'P8lCAp8i6UG2SAah8FvBUElDLbg',
                    user_agent = 'image-collector',
                    username = "thsnersy" ,
                    password = "thsnreddit1001" )


subreddit = reddit.subreddit('gonewild')

hot_python = subreddit.hot(limit=5)

for submission in hot_python:
  if not submission.stickied:
    print(submission.shortlink)


  