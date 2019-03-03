""" Quickstart script for InstaPy usage """
# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'clockingmiles'
insta_password = 'Vikas@1729'

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    """ Activity flow """
    # general settings
    session.set_dont_include(["friend1", "friend2", "friend3"])

    # activity
    session.like_by_tags(["sunset"], amount=10, interact=True)

    # don't like if a post already has more than 150 likes
    session.set_delimit_liking(enabled=True, max=150, min=0)

    # don't comment if a post already has more than 4 comments
    session.set_delimit_commenting(enabled=True, max=4, min=0)

    """I used to have potency_ratio=-0.85 and max_followers=1200 for set_relationship_bounds()
       Having a stricter relationship bound to target only low profiles users was not very useful,
      as interactions/sever calls ratio was very low. I would reach the server call threshold for
      the day before even crossing half of the presumed safe limits for likes, follow and comments (yes,
      looks like quiet a lot of big(bot) managed accounts out there!!).So I relaxed it a bit to -0.50 and 2000 respectively.
    """
    session.set_relationship_bounds(enabled=True, potency_ratio=-1.2,
                                    delimit_by_numbers=True,
                                    max_followers=5000,
                                    max_following=6500,
                                    min_followers=25,
                                    min_following=25)
    session.set_do_comment(True, percentage=20)
    session.set_do_follow(enabled=True, percentage=20, times=2)
    session.set_comments(['This is a dope picture', 'Awesome dope picture!!',
                          'Really good one'])
    session.set_sleep_reduce(200)

    """ Get the list of non-followers
        I duplicated unfollow_users() to see a list of non-followers which I 
        run once in a while when I time
        to review the list
    """
