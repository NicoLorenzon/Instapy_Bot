from instapy import Instapy
from instapy import smart_run

user = ""
passw= ""

comentarios= [
"Genial! :muscle:",
"Que bonito!",
"Excelente! :relaxed:",
]

#comentarios_clave = [{"required_words": ['fit' ,'fintess'], 'comments': ["Buen trabajo!"]]

sesion = Instapy(username= user,
                password= passw,
                headless_browser= False)

with smart_run(sesion):
    #Likes
    sesion.set_do_like(enabled=True, percentage=70) 
    sesion.like_by_tags(["fit", "fitness", 'protein'], amount= 20) 
    sesion.like_by_locations(["218829052/parana-entre-rios/"])

    # Comentarios
    sesion.set_do_comment(enabled=True, percentage= 35)
    sesion.set_comments(comentarios) 
    # sesion.set_comments(["Linda Foto! :grinning:""], media= "photo")
    # sesion.set_comments(['Lindo video!'], media= "video")
    sesion.join_pods(topic="", engagement_mode= "no_comments") 
    sesion.comment_by_locations(["218829052/parana-entre-rios/"])

    # Seguidos
    sesion.set_do_follow(enabled=True, percentage= 10)

    # Hashtags
    sesion.set_smart_location_hashtags(["218829052/parana-entre-rios/"], radius=15, limit=10) 
    sesion.like_by_tags(amount=15, use_smart_location_hashtags= True)

    # Resctriccion de likes
    sesion.set_dont_like(['nudes', 'naked', 'porn', 'foodporn'])
    sesion.set_ignore_if_contains(['sin gluten', 'veggie'])
    # Restricciones de usuarios
    sesion.set_dont_include(['nicoolorenzon'])

    #Omision de usuarios sin foto de perfil
    sesion.set_skip_users(skip_private = True ,
                          skip_no_profile_pic = True ,
                          no_profile_pic_percentage = 100)


    sesion.set_quota_supervisor(enabled= False,
                                sleep_after= ['likes', 'comments'],
                                sleepyhead=True,
                                stochastic_flow=True,
                                notify_me=True,
                                peak_likes_hourly=40,
                                peak_likes_daily=200,
                                peak_comments_hourly=21,
                                peak_comments_daily=182,
                                peak_follows_hourly=48,
                                peak_follows_daily=None,
                                peak_unfollows_hourly=35,
                                peak_unfollows_daily=402,
                                peak_server_calls_hourly=None,
                                peak_server_calls_daily=4700)