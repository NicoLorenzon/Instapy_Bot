import random
from instapy import InstaPy
from instapy import smart_run

user = "joker.showroomparana@hotmail.com"
passw= "alanalva"

# Restricciones
dont_like = ['nudes', 'porn', 'ntfs']

amigos = ['nicoolorenzon', 'ciro.mzz']

ignore_list = ['cars']

# Target
objetivos= ['onefitnessargentina', 'gustavoluisrenaud']
target_bussines_cat = ['cars']

comentarios = ['Excelente! :thumbsup: @{}',
               'Buena! :thumbsup:',
               ':muscle::muscle:',
               'Que bien! @{}']

# Sesion
session = InstaPy(username=user,
                  password=passw,
                  headless_browser=False,
                  disable_image_load=False,
                  multi_logs=False)

# Ciclo Bot
with smart_run (session):
    # NO comentar una publicacion con mas de 10 mil comentarios, minimo 1
    #session.set_delimit_commenting(enabled=True, max_comments=100, min_comments=1)
    # Cfg general
    # session.set_dont_include(amigos)
    # session.set_dont_like(dont_like)
    # session.set_ignore_if_contains(ignore_list)
    # session.set_ignore_users(amigos)
    # session.set_simulation(enabled=True)

    # session.set_relationship_bounds(enabled=True,
    #                                 potency_ratio=0.65,
    #                                 delimit_by_numbers=True,
    #                                 max_followers=1500000,
    #                                 max_following=4000,
    #                                 min_followers=50,
    #                                 min_following=50,
    #                                 min_posts=3)

    #session.set_skip_users(skip_private=True,
                           #skip_no_profile_pic=True,
                          # skip_business=False)


    session.set_do_like(enabled=True, percentage=90)
    session.like_by_users(objetivos)
    # session.set_comments(comentarios)
    # session.set_do_comment(enabled=True, percentage=80)
    # session.comments_by_users(objetivos)

#############
# Actividades
    # nro = random.randint(2,3)
    # random_targets= objetivos

    # if len(objetivos) <= nro:
    #     random_targets = objetivos

    # else:
    #     random_targets= random.sample(objetivos, nro)

print("nico gay")

