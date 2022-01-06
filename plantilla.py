from instapy import InstaPy
from instapy import smart_run

user= "joker.showroomparana@hotmail.com"
pas = "alanalva"


comentarios = ["Lindo auto! @{}",
               "Lindo perfil!",
               ":open_mouth: :open_mouth:",
               ":muscle: :muscle:",
               "Que maquina! @{}" ] 

sesion = InstaPy(username= user,
                 password= pas,
                 headless_browser=False) # Ejecutar en segundo plano = True

with smart_run(sesion):
    """Actividad del bot"""
    # Carac generales
    sesion.set_dont_include(["alan_alva_", "nicoolorenzon", "revivalautomotores"]) #Usuarios para no interactuar

    # Actividad
    sesion.set_do_like(enabled=True, percentage=65) # Porcentaje de likes en publicaciones vistas
    sesion.like_by_tags(["cars", "car"], amount= 20) # Hastaghs objetivos
    sesion.like_by_locations(["218829052/parana-entre-rios/"]) # Ubicacion

    #Entradas a comentarios
    sesion.set_do_comment(enabled=True, percentage= 35) # Porcentaje de comentarios
    sesion.set_comments(comentarios) 
    sesion.join_pods(topic="", engagement_mode= "no_comments") # Comentarios desactivados
    sesion.comment_by_locations(["218829052/parana-entre-rios/"]) # Ubicacion para los comentarios A PROBAR

    sesion.set_do_follow(enabled= True, percentage= 15, times=1) # Sigue el 15 porciento de las cuentas 1 vez
    sesion.set_smart_hashtags(["", ""], limit=3, sort='top', log_tags=True) #Seleccion de hastags inteligente, por mas popular o aleatorio, log_tags muestra el hasgtag visto
    sesion.like_by_tags(amount=10, use_smart_hashtags= True) # Usa la linea de arriba
    sesion.set_smart_location_hashtags([""], radius=20, limit=10) # Generar Hashtags inteligentes por la ubicacion, radus = distancia a la redonde en millas


# LOCALIZACIONES
#  Gim Vertigo 1026882572/gimnasio-vertigo/
#  Costanera 226724549/parque-urquiza-costanera-parana/
#  Echague 289490085/atletico-echague-club-oficial/
#  Casa Ditalia 801529605/gim-casa-d-italia/
#  Atlethic gym 1013859680/athletic-gimnasio-deportivo/
#  centro fitness 128608701022840/cf-628-centro-de-fitness/
#  PRC 55252289/parana-rowing-club/
#  CCP 295017276/club-ciclista-parana/
#  Bonafide 214856181988338/bonafide-parana/
#  Gym cep 798170816/gimnasio-cep/
#  One Finess center 1002999060/one-fitness-center/
#  Arenasports 887993377/arenasports-gimnasio/
# Suplementos gym 1467257293573449/suplementos-gym/
# Zeus gym 1030444545/zeus-gym/
# Parana fitness 614558312316896/parana-fitness-place/
# Play fit 371837166536506/play-fit-training-center/
# Pro gym 338923740281904/pro-gym-parana/
# gymcenter 606740392796799/megaforce-gymcenter/
sss


