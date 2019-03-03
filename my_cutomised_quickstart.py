# import required libraries
import random
from instapy import InstaPy
from instapy import smart_run

# Login Details
insta_username = ''
insta_password = ''

# set target whose followers will be targetted
target_followers_of_user = ['tinn','ankita_bhattacharya_sharma']

# get a session!
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False,
                  multi_logs=True)


#Comment Data
comments = ['This is a dope picture. good one',
            'thats an Awesome picture, very well captured!!',
            'nice one',
            'You have great feed content in your gallery, loved it',
            'your captures are really nice!.','Your pictures are amazing ! ']

#Start Bot
with smart_run(session):

    session.set_relationship_bounds(enabled=True,
        potency_ratio=-.90, #following and follower ratio is equal or greater than this will be entertained.
        delimit_by_numbers=True,
        max_followers=12000,
        max_following=15000,
        min_followers=30,
        min_following=50,
        min_posts=5)

    session.set_skip_users(skip_business=False,skip_private=False)

    session.set_user_interact(amount=6,randomize=True,percentage=100,media='photo')

    session.set_comments(comments, media='photo')
    session.set_do_comment(enabled=True, percentage=100)
    session.set_do_like(enabled=True, percentage=100)
    session.set_do_follow(enabled=True,percentage=100,times=1)

    session.follow_user_followers(target_followers_of_user,amount=60,randomize=True,sleep_delay=60,interact=True) #Select randomized 20 followers from each target, Interact with them and sleep for 500 Sec and move to next target




