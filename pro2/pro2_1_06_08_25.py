#ejercicios 
#calculo del area de un circulo
import datetime
import math
import random
def calculo_area_circulo(radio:float) -> str:
    """Calcula el area de un circulo, el parametro 'radio' es en cm"""
    return f"El area del circulo con radio de {radio} cm es: {math.pi*(radio**2):.2f} cm2"

print(calculo_area_circulo(5))

#cantar la loteria!
loteria = [
    ("El gallo", "El que le cantó a san Pedro no le volverá a cantar."),
    ("El diablo", "El diablo son las mujeres cuando se quieren casar."),
    ("La dama", "La chula de Severiana un tacón quería empeñar."),
    ("El catrín", "Don Ferruco en la Alameda su bastón quería empeñar."),
    ("El paraguas", "El paraguas quitasol."),
    ("La sirena", "Medio cuerpo de sirena, medio cuerpo de mujer."),
    ("La escalera", "La escalera, siete palos, la escalera del pintor."),
    ("La botella", "La botella del tequila, la botella del mezcal."),
    ("El barril", "El barril es quintaleño, el barril del mezcal."),
    ("El árbol", "El árbol de la esperanza que de venir no se cansa."),
    ("El melón", "El melón y sus olores, un pedazo me has de dar."),
    ("El valiente", "’Tate quieto, Valentín, no te vayas a pelear."),
    ("El gorrito", "El gorrito ponle al nene, no se te vaya a resfriar."),
    ("La muerte", "La muerte siriquiflaca, montada en su burra flaca."),
    ("La pera", "Me esperas donde quedamos, para poder platicar."),
    ("La bandera", "Bonito cinco de mayo, el pabellón nacional."),
    ("El bandolón", "El bandolón ya no suena, hay que llevarlo a afinar."),
    ("El violoncello", "El violoncello del maistro, que no deja de sonar."),
    ("La garza", "Llegaron los picos largos de la feria de San Juan."),
    ("El pájaro", "El pájaro churlumirlo, que no deja de cantar."),
    ("La mano", "La mano del escribano, la mano del criminal."),
    ("La bota", "La bota rechina, la bota del general."),
    ("La luna", "La luna tuerta de un ojo, que no deja de brillar."),
    ("El cotorro", "Perico, da’cá la pata y empieza a platicar los trabajos que pasabas cuando no sabías hablar."),
    ("El borracho", "Al borracho, mi compañero, ya se lo van a cargar."),
    ("El negrito", "Para negros, en La Habana; uno acaba de llegar."),
    ("El corazón", "El corazón de una ingrata yo lo voy a traspasar."),
    ("La sandía", "La sandía y su rebanada, un pedazo me has de dar."),
    ("El tambor", "No te arrugues, cuero viejo, que te quiero pa’ tambor."),
    ("El camarón", "Camarón que se duerme se lo lleva la corriente."),
    ("Las jaras", "Las jaras o no las jaras, o las dejas de jalar."),
    ("El músico", "El músico, trompa de hule."),
    ("La araña", "La araña teje su tela."),
    ("El soldado", "Centinela, ponte alerta, que te habla tu general."),
    ("La estrella", "La estrella polar del norte, que no deja de brillar."),
    ("El cazo", "El caso que te hago es poco; el caso es averiguar."),
    ("El mundo", "El mundo es una bola, y nosotros, un bolón."),
    ("El apache", "Para apaches, en Chihuahua; uno acaba de llegar."),
    ("El nopal", "El auxilio de San Luis, que le llaman el nopal."),
    ("El alacrán", "¡No levantes esa piedra, que te pica ese animal!"),
    ("La rosa", "Rosa, Rosita, Rosaura, Rosita se ha de llamar."),
    ("La calavera", "Ya te vide an ca’ la güera."),
    ("La campana", "La campana, y tú, debajo."),
    ("El cantarito", "Todo cabe en un jarrito, sabiéndolo acomodar."),
    ("El venado", "Don Venancio, a la carrera, un balazo le han de dar."),
    ("El sol", "Solito me estoy quedando, solito me he de quedar."),
    ("La corona", "Si te mueres, te la pongo, la coronita imperial."),
    ("La chalupa", "Rema y rema, Joaquinita, y no dejes de remar."),
    ("El pino", "Te empino y me voy de paso, y empinado has de quedar."),
    ("El pescado", "Me pescaron vacilando en la puerta del zaguán."),
    ("La palma", "Sube a la palma, palmero, y bájame un cocotal."),
    ("La maceta", "En la maceta me dieron, por no saber barajar."),
    ("El arpa", "El arpa vieja de mi suegra."),
    ("La rana", "¡Qué saltos pega tu hermana en la puerta del zaguán!"),
]

def cantar_la_loteria(cartas:list[tuple]) ->None:
    random.shuffle(cartas)
    for x in cartas:
        print(f"\n{x[0]}. {x[1]}")
        if random.randrange(20)<5:
            print("\nLoteriaaaaaaaaaaa!")
            return None
        
cantar_la_loteria(loteria)

#calculo de edad con datetime
def calcula_edad(dt_string:str) -> str:
    """Calcula la edad del usario con la fecha de nacimiento del mismo, es un texto y el formato para la fecha es 'dd/mm/aaaa'."""
    try:
        new_date=datetime.datetime.strptime(dt_string,"%d/%m/%Y").date()
        return f"\nTu edad a dia de hoy es: {datetime.datetime.today().year-new_date.year} años."
    except ValueError as e:
        return(f"details: el formato no coincide! {e}")

print(calcula_edad("09/07/2005"))





