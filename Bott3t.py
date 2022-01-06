import random
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'tercertiempoparana'
insta_password = 'sanmartin695'

dont_likes = ['sex', 'nude', 'naked', 'beef', 'pork',
            'sausage', 'lobster','fisch', 'schwein', 'lamm', 'rind', 'kuh', 'meeresfrüchte',
            'schaf', 'ziege', 'hummer', 'yoghurt', 'joghurt', 'dairy',
            'meal', 'food', 'eat','essen', 'mahl','dinner', 'turkey', 'truthahn', 'plate', 'bacon',
            'sushi', 'burger', 'steak','schnitzel', 'goat', 'oxtail', 'mayo', 'fur', 'leather',
            'cream', 'hunt', 'gun', 'shoot', 'slaughter', 'pussy','natgeo','animal','zoo']

friends = ['tercertiempoparana','sonderparana','sondersantafe']

like_tag_list = ['rugby','argentina','sport','actualidadscrum','sports','rugbyunion',
                'rugbyargentino','rugbylove','hockey','jaguares','leonas','lospumas',
                'scrum','seleccion','passline','fieldhockey','sports','fit',
                'pasion','hockeylife','mamihockey','hockeygame','leonas','lasleonas',
                'leones','losleones','crai','qlsr','prc','cae','paracao']

# prevent posts that contain some plantbased meat from being skipped
ignore_list = ['animal','natgeo','zoo','porn']

accounts = ['unionargentina','lasleonashockeyargentina','lospumasuar','jaguaresarg']

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
    session.set_ignore_if_contains(ignore_list)

    session.set_user_interact(amount=2, randomize=True, percentage=60)
    session.set_do_follow(enabled=True, percentage=40)
    session.set_do_like(enabled=True, percentage=80)

    # activity
    session.like_by_tags(random.sample(like_tag_list, 3),
                        amount=random.randint(50, 100), interact=True)

    # session.unfollow_users(amount=random.randint(75, 150),
    #                     InstapyFollowed=(True, "all"), style="FIFO",
    #                        unfollow_after=90 * 60 * 60, sleep_delay=501)

    """ Joining Engagement Pods...
    """
    photo_comments = ['Muy buena! @{}',
        'Genial! @{}',
        'Pasa por mi pefil y mirá nuestras prendas y accesorios! :thumbsup:',
        'Excelente! :raised_hands:',
        ':raised_hands::raised_hands::raised_hands:']

    session.set_do_comment(enabled = True, percentage = 95)
    session.set_comments(photo_comments, media = 'Photo')
    session.join_pods(topic='hockey')