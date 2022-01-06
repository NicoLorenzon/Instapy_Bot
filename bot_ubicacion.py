from instapy import InstaPy
from instapy import smart_run

user = "joker.showroomparana@hotmail.com"
passw= "alanalva"


session = InstaPy(username= user,
                password= passw,
                headless_browser= False)

coments = [':muscle: :muscle:',
            'Los mejores! :thumbsup:',
            'Excelente!']

# def megusta ():
#     like = sesion.like_by_tags(['fit', 'fitness'])
#     ubicacion= sesion.like_by_locations(['218829052'],amount = 5 , skip_top_posts = True , randomize = True)

#     while like == ubicacion:
#         sesion.set_do_like(enabled=True, percentage=100)



with smart_run(session):

    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=None,
                                    delimit_by_numbers=True,
                                    max_followers=3000,
                                    max_following=900,
                                    min_followers=50,
                                    min_following=50)

    session.set_simulation(enabled=False)
    # session.like_by_locations(['801529605'],amount = 10 , skip_top_posts = True , randomize = True) # Casa Ditalia
    # session.set_do_like(enabled=True, percentage=70)
    session.set_ignore_users(['nicoolorenzon'])
    session.set_do_comment(enabled=True, percentage=35)
    session.comment_by_locations(['801529605'])
    session.set_comments(coments)
    
    session.set_action_delays(enabled=True, like=40)
 




    session.end()    
  
    

   

