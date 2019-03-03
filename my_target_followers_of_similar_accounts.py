"""
This template is written by @Nuzzo235

What does this quickstart script aim to do?
- This script is targeting followers of similar accounts and influencers.
- This is my starting point for a conservative approach: Interact with the
audience of influencers in your niche with the help of 'Target-Lists' and
'randomization'.

NOTES:
- For the ease of use most of the relevant data is retrieved in the upper part.
"""

import random
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = ''
insta_password = ''

# restriction data
dont_likes = ['sad', 'cry', 'depression']
ignore_users = ['vishal.verma.773', 'sunita8059', 'neel.mitra1','muidul_islam','bhungavia_','_mythai__','loladoestravel','thelogbook_','seba_bnw']

""" Prevent commenting on and unfollowing your good friends (the images will 
still be liked)...
"""
friends = ['friend1', 'friend2', 'friend3']

""" Prevent posts that contain...
"""
ignore_list = []

# TARGET data
""" Set similar accounts and influencers from your niche to target...
"""
'''targets = ['erin.nicole.l',travelwithkaja,'ztsago',
'abhishekchoudhary4806','doon_foodfascination','anshuman_mallick',
'leemuthapa','alankwang8888','bhungavia_',
'komangbudiyani','khushi_sharma90',
'khushi_sharma07','the_midnightwriter',
'faryda_lindeman','bw_phototrip','dehradun_official_page','thecanonfanboy',
'leemuthapa','alankwang8888','bhungavia_','travellingwithgiannis','thilomellies','world_pic_nab','demas']
'''
targets = ['jonooiphotography','hungrynyc','aaronlin_monroe','dehradun_official_page','khushi_sharma90','travelawesome','travelandleisure','travel','travellingthroughtheworld','travel.escape','travelbloggeres']

""" Skip all business accounts, except from list given...
"""
target_business_categories = ['category1', 'category2', 'category3']

# COMMENT data

comments = [u'dis is a dope capture :heart_eyes: good one',
            u'thats an Awesome pic, very well captured!! :thumbsup:',
            u'nice one, Awesome!!:raising_hands:',
            u'Great capture!! :smiley: If you have time, check out my gallery too.',
            u'I really liked the way you have captured this.',
            u'Your gallery got good feed content, loved it :raising_hands:',
            u'Really nice captures in your gallery!.','Your pics are pretty amazing!!',
            u'great shot, keep up the great work like in your gallery']


# get a session!
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False,
                  multi_logs=True)

# let's go! :>
with smart_run(session):
    # HEY HO LETS GO
    # general settings
    session.set_dont_include(friends)
    session.set_dont_like(dont_likes)
    session.set_ignore_if_contains(ignore_list)
    session.set_ignore_users(ignore_users)
    session.set_simulation(enabled=True)
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=7500,
                                    max_following=3000,
                                    min_followers=25,
                                    min_following=25,
                                    min_posts=6)

    session.set_skip_users(skip_private=True,
                           skip_no_profile_pic=True,
                           skip_business=False,
                           dont_skip_business_categories=[
                               target_business_categories])

    session.set_user_interact(amount=5, randomize=True, percentage=100,
                              media='Photo')
    session.set_comments(comments, media='Photo')
    session.set_do_like(enabled=True, percentage=100)
    session.set_do_comment(enabled=True, percentage=40)
    session.set_do_follow(enabled=True, percentage=100, times=1)

    # activities

    # FOLLOW+INTERACTION on TARGETED accounts
    """ Select users form a list of a predefined targets...
    """
    number = random.randint(4, 7)
    random_targets = targets

    if len(targets) <= number:
        random_targets = targets

    else:
        random_targets = random.sample(targets, number)

    """ Interact with the chosen targets...
    """
    session.follow_likers(targets, photos_grab_amount = 1, follow_likers_per_photo = 500, randomize=True, sleep_delay=600, interact=True)
    
    #UNCOMMENT to follow followers
    #session.follow_user_followers(random_targets, amount=500, randomize=True, sleep_delay=900, interact=True)

    # UNFOLLOW activity
    """ Unfollow nonfollowers after 3 day...
    """
    session.unfollow_users(amount=random.randint(75, 100),
                           InstapyFollowed=(True, "nonfollowers"),
                           style="FIFO",
                           unfollow_after=72 * 60 * 60, sleep_delay=100)

    """ Unfollow all users followed by InstaPy after 10 days to keep the 
    following-level clean...
    """
    session.unfollow_users(amount=random.randint(75, 100),
                           InstapyFollowed=(True, "all"), style="FIFO",
                           unfollow_after=240 * 60 * 60, sleep_delay=300)

"""
Have fun while optimizing for your purposes, Nuzzo
"""
