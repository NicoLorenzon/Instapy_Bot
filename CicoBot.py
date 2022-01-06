import random
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'cicodata'
insta_password = 'Python2021'

dont_likes = ['sex', 'nude', 'naked', 'beef', 'pork', 'seafood',
              'egg', 'chicken', 'cheese', 'sausage', 'lobster',
              'fisch', 'schwein', 'lamm', 'rind', 'kuh', 'meeresfrüchte',
              'schaf', 'ziege', 'hummer', 'yoghurt', 'joghurt', 'dairy',
              'meal', 'food', 'eat', 'pancake', 'cake', 'dessert',
              'protein', 'essen', 'mahl', 'breakfast', 'lunch',
              'dinner', 'turkey', 'truthahn', 'plate', 'bacon',
              'sushi', 'burger', 'salmon', 'shrimp', 'steak',
              'schnitzel', 'goat', 'oxtail', 'mayo', 'fur', 'leather',
              'cream', 'hunt', 'gun', 'shoot', 'slaughter', 'pussy',
              'breakfast', 'dinner', 'lunch']

friends = ['nicoolorenzon','ciromzz']

like_tag_list = ['bigdata', 'datascience', 'dataanalytics', 'data',
                'datascientist', 'python', 'artificialintelligence',
                'machinelearning ','python', 'ai', 'deeplearning',
                'programming', 'technology', 'coding','datavisualization',
                'computerscience', 'pythonprogramming','analytics',
                'tech', 'dataanalysis','iot','programmer','statistics',
                'developer','ml','business','java','innovation',
                'coder','dataanalyst','bhfyp']

# prevent posts that contain some plantbased meat from being skipped
#ignore_list = ['vegan', 'veggie', 'plantbased']

accounts = ['argentinaendatos']

# get a session!
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    # settings
    session.set_relationship_bounds(enabled=True,
                                    max_followers=15000)

    session.set_dont_include(friends)
    session.set_dont_like(dont_likes)
    # session.set_ignore_if_contains(ignore_list)

    session.set_user_interact(amount=2, randomize=True, percentage=60)
    session.set_do_follow(enabled=True, percentage=40)
    session.set_do_like(enabled=True, percentage=80)

    # activity
    session.like_by_tags(like_tag_list, amount=random.randint(50, 100), interact=True)

#    session.unfollow_users(amount=random.randint(75, 150),
                        #    InstapyFollowed=(True, "all"), style="FIFO",
                        #    unfollow_after=90 * 60 * 60, sleep_delay=100)

    """ Joining Engagement Pods...
    """
    photo_comments = ['Nice! @{}',
        'Good! @{}',
        'Wonderful :thumbsup:',
        'Just incredible :open_mouth:',
        ':raised_hands: Yes!']

    session.set_do_comment(enabled = True, percentage = 95)
    session.set_comments(photo_comments, media = 'Photo')
    session.join_pods(topic='DataScience')