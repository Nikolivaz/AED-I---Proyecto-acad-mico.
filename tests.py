import unittest
from arimaa import *

# Las piezas se representan con las siguientes letras:
#   E : elefante
#   M : camello
#   H : caballo
#   D : perro
#   C : gato
#   R : ratón
# donde
#   mayúscula : dorado
#   minúscula : plateado

def tablero_8x8_vacio():
    return leer_tablero([
              '--------', #7
              '--------', #6
              '--------', #5
              '--------', #4
              '--------', #3
              '--------', #2
              '--------', #1
              '--------', #0
              #01234567
            ])

def tablero_8x8_inicial_ejemplo():
    return leer_tablero([
              'hcdmedch', #7
              'rrrrrrrr', #6
              '--------', #5
              '--------', #4
              '--------', #3
              '--------', #2
              'RRRRRRRR', #1
              'HCDMEDCH', #0
              #01234567
            ])

#### Ejercicio 1

class test_tablero_bien_formado(unittest.TestCase):

    def test_8x8_lleno(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertTrue(tablero_bien_formado(t))

class test_posicion_en_tablero(unittest.TestCase):

    def test_posicion_ok(self):
        self.assertTrue(posicion_en_tablero(Posicion(5, 3)))

class test_movimiento_bien_formado(unittest.TestCase):

    def test_movimiento_ok(self):
        self.assertTrue(movimiento_bien_formado(Movimiento(MOVER_A_SECAS, Posicion(0, 1), [NORTE])))

class test_juego_bien_formado(unittest.TestCase):

    def test_juego_ok(self):
        j = Juego(tablero_8x8_vacio(), DORADO, 0)
        self.assertTrue(juego_bien_formado(j))

#### Ejercicio 2

class test_posicion_vecina_hacia(unittest.TestCase):

    def test_vecina_al_norte(self):
        self.assertEqual(posicion_vecina_hacia(Posicion(0, 0), NORTE), Posicion(1, 0))

class test_son_posiciones_vecinas(unittest.TestCase):

    def test_vecinas(self):
        self.assertTrue(son_posiciones_vecinas(Posicion(0, 0), Posicion(1, 0)))

class test_casilla_en_posicion(unittest.TestCase):

    def test_casilla_en_posicion(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertEqual(casilla_en_posicion(t, Posicion(0, 0)), Pieza(CABALLO, DORADO))

class test_hay_casilla_vacia(unittest.TestCase):

    def test_casilla_vacia(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertTrue(hay_casilla_vacia(t, Posicion(2, 1)))

class test_hay_pieza_de_color(unittest.TestCase):

    def test_hay_pieza_de_color_ok(self):
        t = tablero_8x8_inicial_ejemplo()
        self.assertTrue(hay_pieza_de_color(t, Posicion(1, 4), DORADO))

#### Ejercicio 3

class test_hay_casilla_vacia_hacia(unittest.TestCase):

    def test_hay_casilla_vacia_hacia(self):
        t = leer_tablero([
              '-r----rr', #7
              '-mrh----', #6
              '-r---r--', #5
              'd-EH---c', #4
              '-M--hD-d', #3
              '-R-e----', #2
              '---H-R-C', #1
              'R-R---RR', #0
              #01234567
            ])
        self.assertTrue(hay_casilla_vacia_hacia(t, Posicion(0, 0), NORTE))

class test_hay_pieza_amiga_vecina(unittest.TestCase):

    def test_hay_pieza_amiga_vecina(self):
        t = leer_tablero([
              'R-hRD-Rr', #7
              'M----d--', #6
              '-h-rrCR-', #5
              'R-rcE---', #4
              '--drRR--', #3
              '-HD-H--m', #2
              '--r-RCc-', #1
              're---r--', #0
              #01234567
            ])
        self.assertTrue(hay_pieza_amiga_vecina(t, Posicion(4, 3)))

class test_hay_pieza_enemiga_mas_debil_hacia(unittest.TestCase):

    def test_hay_pieza_enemiga_mas_debil_hacia(self):
        t = leer_tablero([
              '--Hdm---', #7
              'r--HhC--', #6
              'e---R-C-', #5
              'ME--d---', #4
              'h--RDcRr', #3
              'R-R-r--r', #2
              '-RRcrRD-', #1
              '--r---rr', #0
              #01234567
            ])
        self.assertTrue(hay_pieza_enemiga_mas_debil_hacia(t, Posicion(1, 3), OESTE))

class test_hay_pieza_enemiga_mas_fuerte_vecina(unittest.TestCase):

    def test_hay_pieza_enemiga_mas_fuerte_vecina(self):
        t = leer_tablero([
              'R-e--mRr', #7
              '------dE', #6
              'h--Rr-RR', #5
              'c--R-C--', #4
              '-rCHDrr-', #3
              '----rc--', #2
              'h-R-M-R-', #1
              'rr-D-dH-', #0
              #01234567
            ])
        self.assertTrue(hay_pieza_enemiga_mas_fuerte_vecina(t, Posicion(3, 1)))

class test_hay_pieza_congelada(unittest.TestCase):

    def test_hay_pieza_congelada(self):
        t = leer_tablero([
              '--d--H-D', #7
              '-hMc--r-', #6
              '--r--C-H', #5
              '--------', #4
              '-CeD----', #3
              '---R----', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        self.assertTrue(hay_pieza_congelada(t, Posicion(6, 1)))

#### Ejercicio 4

class test_puede_realizar_movimiento(unittest.TestCase):

    def test_mover_a_secas_ok(self):
        t = leer_tablero([
              '--eMr---', #7
              '--------', #6
              '-R----r-', #5
              '--------', #4
              '--mMd---', #3
              '---D----', #2
              '--------', #1
              '-mD--mDR', #0
              #01234567
            ])
        j = Juego(t, PLATEADO, 0)
        m = Movimiento(MOVER_A_SECAS, Posicion(0, 1), [NORTE])
        self.assertTrue(puede_realizar_movimiento(j, m))

#### Ejercicio 5

class test_activar_trampas(unittest.TestCase):

    def test_activar_trampas_ok(self):
        t0 = leer_tablero([
               '-eRD--rd', #7
               '--------', #6
               'H-r--E--', #5
               '-H--r-Cr', #4
               'R-------', #3
               'R-H--m--', #2
               'R-------', #1
               'c-D---R-', #0
               #01234567
             ])
        t1 = leer_tablero([
               '-eRD--rd', #7
               '--------', #6
               'H-------', #5
               '-H--r-Cr', #4
               'R-------', #3
               'R-------', #2
               'R-------', #1
               'c-D---R-', #0
               #01234567
             ])
        t2 = activar_trampas(t0)
        self.assertNotEqual(t0, t1)
        self.assertEqual(t2, t1)

#### Ejercicio 6

class test_realizar_movimiento(unittest.TestCase):
 
    def test_mover_a_secas(self):
        t0 = leer_tablero([
               'rrrrrrrr', #7
               'ccddhh-e', #6
               '--------', #5
               '---m----', #4
               '--------', #3
               '--------', #2
               'EMHHDDCC', #1
               'RRRRRRRR', #0
               #01234567
             ])
        tN = leer_tablero([
               'rrrrrrrr', #7
               'ccddhh-e', #6
               '---m----', #5
               '--------', #4
               '--------', #3
               '--------', #2
               'EMHHDDCC', #1
               'RRRRRRRR', #0
               #01234567
             ])
        j0 = Juego(t0, PLATEADO, 0) 
        jN = Juego(tN, PLATEADO, 1) 
        mN = Movimiento(MOVER_A_SECAS, Posicion(4, 3), [NORTE])
        self.assertTrue(puede_realizar_movimiento(j0, mN))
        self.assertEqual(realizar_movimiento(j0, mN), jN)

#### Ejercicio 7

class test_ganador_del_juego(unittest.TestCase):

    def test_promueve_conejo_dorado_turno_del_oponente(self):
        t = leer_tablero([
              'rr----Rr', #7
              'c-----me', #6
              '---Ed-R-', #5
              '-M---R--', #4
              '---R----', #3
              '-rrrr---', #2
              '-H---DCC', #1
              'R-----RR', #0
              #01234567
            ])
        j = Juego(t, PLATEADO, 0)
        self.assertTrue(hay_ganador_determinado(j))
        self.assertEqual(ganador_del_juego(j), DORADO)

class test_ejercicio_1_2_para_cubrimiento(unittest.TestCase):

    def test_juego_mal_formado(self):
        t: Tablero = tablero_8x8_vacio()
        self.assertTrue(juego_bien_formado(Juego(t, DORADO, 3)))
        self.assertFalse(juego_bien_formado(Juego(t, DORADO, 4)))
        self.assertFalse(juego_bien_formado(Juego(t, DORADO, -1)))
        self.assertFalse(juego_bien_formado(Juego([], DORADO, 0)))

    def test_posicion_vecina_en_las_cuatro_direcciones(self):
        pos: Posicion = Posicion(3, 3)
        self.assertEqual(posicion_vecina_hacia(pos, NORTE), Posicion(4, 3))
        self.assertEqual(posicion_vecina_hacia(pos, SUR), Posicion(2, 3))
        self.assertEqual(posicion_vecina_hacia(pos, ESTE), Posicion(3, 4))
        self.assertEqual(posicion_vecina_hacia(pos, OESTE), Posicion(3, 2))

    def test_hay_pieza_de_color_casos_negativos(self):
        t: Tablero = tablero_8x8_inicial_ejemplo()
        self.assertFalse(hay_pieza_de_color(t, Posicion(0, 0), PLATEADO))
        self.assertFalse(hay_pieza_de_color(t, Posicion(4, 4), DORADO))

#### Para devolver líneas: ejercicio 6

class test_ejercicio_6_para_cubrimiento(unittest.TestCase):

    def test_arrastrar_enemiga_a_una_trampa_la_retira(self):
        t0: Tablero = leer_tablero([
              '--------', #7
              '--------', #6
              '--------', #5
              '--------', #4
              '--------', #3
              '-RE-----', #2
              '--r-----', #1
              '--------', #0
              #01234567
            ])
        tN: Tablero = leer_tablero([
              '--------', #7
              '--------', #6
              '--------', #5
              '--------', #4
              '--E-----', #3
              '-R------', #2
              '--------', #1
              '--------', #0
              #01234567
            ])
        m: Movimiento = Movimiento(ARRASTRAR, Posicion(2, 2), [NORTE, NORTE])
        self.assertEqual(realizar_movimiento(Juego(t0, DORADO, 0), m), Juego(tN, DORADO, 2))

#### Para devolver líneas: ejercicio 7

class test_ejercicio_7_para_cubrimiento(unittest.TestCase):

    def test_gana_dorado_porque_plateado_no_tiene_conejos(self):
        t: Tablero = tablero_8x8_vacio()
        t[6][3] = Pieza(ELEFANTE, PLATEADO)
        t[2][2] = Pieza(CONEJO, DORADO)
        j: Juego = Juego(t, PLATEADO, 0)
        self.assertTrue(hay_ganador_determinado(j))
        self.assertEqual(ganador_del_juego(j), DORADO)

    def test_sin_ganador_en_tablero_inicial_y_a_mitad_de_turno(self):
        self.assertFalse(hay_ganador_determinado(Juego(tablero_8x8_inicial_ejemplo(), DORADO, 0)))
        t: Tablero = tablero_8x8_vacio()
        t[0][1] = Pieza(CONEJO, PLATEADO)
        t[2][2] = Pieza(CONEJO, DORADO)
        self.assertFalse(hay_ganador_determinado(Juego(t, DORADO, 2)))

    def test_ambos_reunen_condiciones_gana_quien_acaba_de_jugar(self):
        t: Tablero = tablero_8x8_vacio()
        t[7][0] = Pieza(CONEJO, DORADO)
        t[0][1] = Pieza(CONEJO, PLATEADO)
        self.assertEqual(ganador_del_juego(Juego(t, DORADO, 0)), PLATEADO)
        self.assertEqual(ganador_del_juego(Juego(t, PLATEADO, 0)), DORADO)
# Casos adicionales de los ejercicios 3 y 4.
class test_ejercicio_3_casos_adicionales(unittest.TestCase):

    def test_casilla_vacia_direcciones_y_bordes(self):
        t: Tablero = tablero_8x8_vacio()
        pos: Posicion = Posicion(3, 3)
        for d in [NORTE, SUR, ESTE, OESTE]:
            self.assertTrue(hay_casilla_vacia_hacia(t, pos, d))
        self.assertFalse(hay_casilla_vacia_hacia(t, Posicion(0, 0), SUR))
        self.assertFalse(hay_casilla_vacia_hacia(t, Posicion(0, 0), OESTE))
        self.assertFalse(hay_casilla_vacia_hacia(t, Posicion(7, 7), NORTE))
        self.assertFalse(hay_casilla_vacia_hacia(t, Posicion(7, 7), ESTE))
        t[4][3] = Pieza(GATO, PLATEADO)
        self.assertFalse(hay_casilla_vacia_hacia(t, pos, NORTE))

    def test_pieza_amiga_y_enemiga_en_los_bordes(self):
        t: Tablero = tablero_8x8_vacio()
        pos: Posicion = Posicion(0, 0)
        t[0][0] = Pieza(GATO, DORADO)
        self.assertFalse(hay_pieza_amiga_vecina(t, pos))
        t[1][0] = Pieza(PERRO, PLATEADO)
        self.assertFalse(hay_pieza_amiga_vecina(t, pos))
        t[0][1] = Pieza(CONEJO, DORADO)
        self.assertTrue(hay_pieza_amiga_vecina(t, pos))
        t[0][1] = VACIA
        t[1][0] = Pieza(CONEJO, DORADO)
        self.assertTrue(hay_pieza_amiga_vecina(t, pos))

    def test_enemiga_debil_igual_fuerte_y_fuera_del_tablero(self):
        t: Tablero = tablero_8x8_vacio()
        pos: Posicion = Posicion(0, 0)
        t[0][0] = Pieza(CABALLO, DORADO)
        self.assertFalse(hay_pieza_enemiga_mas_debil_hacia(t, pos, OESTE))
        self.assertFalse(hay_pieza_enemiga_mas_debil_hacia(t, pos, NORTE))
        t[1][0] = Pieza(CONEJO, DORADO)
        self.assertFalse(hay_pieza_enemiga_mas_debil_hacia(t, pos, NORTE))
        t[1][0] = Pieza(CABALLO, PLATEADO)
        self.assertFalse(hay_pieza_enemiga_mas_debil_hacia(t, pos, NORTE))
        t[1][0] = Pieza(ELEFANTE, PLATEADO)
        self.assertFalse(hay_pieza_enemiga_mas_debil_hacia(t, pos, NORTE))
        t[1][0] = Pieza(CONEJO, PLATEADO)
        self.assertTrue(hay_pieza_enemiga_mas_debil_hacia(t, pos, NORTE))

    def test_enemiga_fuerte_en_cualquier_lado(self):
        t: Tablero = tablero_8x8_vacio()
        pos: Posicion = Posicion(4, 4)
        t[4][4] = Pieza(PERRO, PLATEADO)
        self.assertFalse(hay_pieza_enemiga_mas_fuerte_vecina(t, pos))
        t[4][5] = Pieza(GATO, DORADO)
        self.assertFalse(hay_pieza_enemiga_mas_fuerte_vecina(t, pos))
        t[4][5] = Pieza(PERRO, DORADO)
        self.assertFalse(hay_pieza_enemiga_mas_fuerte_vecina(t, pos))
        t[4][5] = Pieza(CAMELLO, PLATEADO)
        self.assertFalse(hay_pieza_enemiga_mas_fuerte_vecina(t, pos))
        t[4][5] = Pieza(CAMELLO, DORADO)
        self.assertTrue(hay_pieza_enemiga_mas_fuerte_vecina(t, pos))
        t[4][5] = VACIA
        t[4][3] = Pieza(ELEFANTE, DORADO)
        self.assertTrue(hay_pieza_enemiga_mas_fuerte_vecina(t, pos))
        t[4][3] = VACIA
        t[3][4] = Pieza(CABALLO, DORADO)
        self.assertTrue(hay_pieza_enemiga_mas_fuerte_vecina(t, pos))
        t[3][4] = VACIA
        t[5][4] = Pieza(CABALLO, DORADO)
        self.assertTrue(hay_pieza_enemiga_mas_fuerte_vecina(t, pos))
        t[5][4] = VACIA
        self.assertFalse(hay_pieza_enemiga_mas_fuerte_vecina(t, pos))

    def test_congelada_sin_pieza_fuerte_o_con_amiga(self):
        t: Tablero = tablero_8x8_vacio()
        pos: Posicion = Posicion(3, 3)
        self.assertFalse(hay_pieza_congelada(t, pos))
        t[3][3] = Pieza(CONEJO, DORADO)
        self.assertFalse(hay_pieza_congelada(t, pos))
        t[4][3] = Pieza(ELEFANTE, PLATEADO)
        self.assertTrue(hay_pieza_congelada(t, pos))
        t[3][4] = Pieza(CONEJO, DORADO)
        self.assertFalse(hay_pieza_congelada(t, pos))
        t[3][4] = VACIA
        t[4][3] = Pieza(CONEJO, PLATEADO)
        self.assertFalse(hay_pieza_congelada(t, pos))

class test_ejercicio_4_casos_adicionales(unittest.TestCase):

    def test_mover_a_secas_turno_ocupada_y_limites(self):
        t: Tablero = tablero_8x8_vacio()
        t[3][3] = Pieza(PERRO, DORADO)
        j: Juego = Juego(t, DORADO, 0)
        m: Movimiento = Movimiento(MOVER_A_SECAS, Posicion(3, 3), [ESTE])
        self.assertTrue(puede_realizar_movimiento(j, m))
        self.assertFalse(puede_realizar_movimiento(Juego(t, PLATEADO, 0), m))
        self.assertFalse(puede_realizar_movimiento(j, Movimiento(MOVER_A_SECAS, Posicion(3, 2), [ESTE])))
        self.assertTrue(puede_realizar_movimiento(Juego(t, DORADO, 3), m))
        t[3][4] = Pieza(CONEJO, PLATEADO)
        self.assertFalse(puede_realizar_movimiento(j, m))
        self.assertEqual(t[3][3], Pieza(PERRO, DORADO))
        self.assertEqual(t[3][4], Pieza(CONEJO, PLATEADO))
        self.assertFalse(puede_realizar_movimiento(j, Movimiento(MOVER_A_SECAS, Posicion(3, 3), [ESTE])))
        t[3][4] = VACIA
        t[7][7] = Pieza(GATO, DORADO)
        self.assertFalse(puede_realizar_movimiento(j, Movimiento(MOVER_A_SECAS, Posicion(7, 7), [ESTE])))

    def test_conejo_dorado_y_plateado_no_retroceden(self):
        t: Tablero = tablero_8x8_vacio()
        t[3][3] = Pieza(CONEJO, DORADO)
        t[5][5] = Pieza(CONEJO, PLATEADO)
        j_dorado: Juego = Juego(t, DORADO, 0)
        j_plateado: Juego = Juego(t, PLATEADO, 0)
        self.assertFalse(puede_realizar_movimiento(j_dorado, Movimiento(MOVER_A_SECAS, Posicion(3, 3), [SUR])))
        self.assertTrue(puede_realizar_movimiento(j_dorado, Movimiento(MOVER_A_SECAS, Posicion(3, 3), [NORTE])))
        self.assertTrue(puede_realizar_movimiento(j_dorado, Movimiento(MOVER_A_SECAS, Posicion(3, 3), [OESTE])))
        self.assertFalse(puede_realizar_movimiento(j_plateado, Movimiento(MOVER_A_SECAS, Posicion(5, 5), [NORTE])))
        self.assertTrue(puede_realizar_movimiento(j_plateado, Movimiento(MOVER_A_SECAS, Posicion(5, 5), [SUR])))
        self.assertTrue(puede_realizar_movimiento(j_plateado, Movimiento(MOVER_A_SECAS, Posicion(5, 5), [ESTE])))

    def test_pieza_congelada_no_se_mueve(self):
        t: Tablero = tablero_8x8_vacio()
        t[3][3] = Pieza(PERRO, DORADO)
        t[4][3] = Pieza(ELEFANTE, PLATEADO)
        m: Movimiento = Movimiento(MOVER_A_SECAS, Posicion(3, 3), [ESTE])
        self.assertFalse(puede_realizar_movimiento(Juego(t, DORADO, 0), m))
        t[3][2] = Pieza(GATO, DORADO)
        self.assertTrue(puede_realizar_movimiento(Juego(t, DORADO, 0), m))

    def test_arrastrar_valido_y_casos_invalidos(self):
        t: Tablero = tablero_8x8_vacio()
        t[3][3] = Pieza(CABALLO, DORADO)
        t[3][2] = Pieza(CONEJO, PLATEADO)
        j: Juego = Juego(t, DORADO, 0)
        m: Movimiento = Movimiento(ARRASTRAR, Posicion(3, 3), [NORTE, ESTE])
        self.assertTrue(puede_realizar_movimiento(j, m))
        self.assertTrue(puede_realizar_movimiento(Juego(t, DORADO, 2), m))
        self.assertFalse(puede_realizar_movimiento(Juego(t, DORADO, 3), m))
        self.assertFalse(puede_realizar_movimiento(j, Movimiento(ARRASTRAR, Posicion(3, 3), [NORTE, SUR])))
        t[4][3] = Pieza(GATO, DORADO)
        self.assertFalse(puede_realizar_movimiento(j, m))
        t[4][3] = VACIA
        t[3][2] = Pieza(ELEFANTE, PLATEADO)
        self.assertFalse(puede_realizar_movimiento(j, m))
        t[3][2] = Pieza(CABALLO, PLATEADO)
        self.assertFalse(puede_realizar_movimiento(j, m))
        t[3][2] = Pieza(CONEJO, DORADO)
        self.assertFalse(puede_realizar_movimiento(j, m))
        t[3][2] = VACIA
        self.assertFalse(puede_realizar_movimiento(j, m))

    def test_empujar_valido_y_casos_invalidos(self):
        t: Tablero = tablero_8x8_vacio()
        t[3][3] = Pieza(ELEFANTE, DORADO)
        t[3][4] = Pieza(CONEJO, PLATEADO)
        j: Juego = Juego(t, DORADO, 0)
        m: Movimiento = Movimiento(EMPUJAR, Posicion(3, 3), [ESTE, NORTE])
        self.assertTrue(puede_realizar_movimiento(j, m))
        self.assertTrue(puede_realizar_movimiento(Juego(t, DORADO, 2), m))
        self.assertFalse(puede_realizar_movimiento(Juego(t, DORADO, 3), m))
        self.assertFalse(puede_realizar_movimiento(j, Movimiento(EMPUJAR, Posicion(3, 3), [ESTE, OESTE])))
        t[4][4] = Pieza(GATO, PLATEADO)
        self.assertFalse(puede_realizar_movimiento(j, m))
        t[4][4] = VACIA
        t[3][4] = Pieza(ELEFANTE, PLATEADO)
        self.assertFalse(puede_realizar_movimiento(j, m))
        t[3][4] = Pieza(CONEJO, DORADO)
        self.assertFalse(puede_realizar_movimiento(j, m))
        t[3][4] = VACIA
        self.assertFalse(puede_realizar_movimiento(j, m))
        t[7][6] = Pieza(ELEFANTE, DORADO)
        t[7][7] = Pieza(CONEJO, PLATEADO)
        self.assertFalse(puede_realizar_movimiento(j, Movimiento(EMPUJAR, Posicion(7, 6), [ESTE, NORTE])))


#Test de ejercicios extra 


class test_ejercicio_extra_cn_contar_figura_de_color(unittest.TestCase):
    def test_colores(self):
        t = leer_tablero([
                      'rr----Rr', #7
                      'c-----me', #6
                      '---Ed-R-', #5
                      '-M---R--', #4
                      '---R----', #3
                      '-rrrr---', #2
                      '-H---DCC', #1
                      'R-----RR', #0
                      #01234567
                    ])
        j = Juego(t, DORADO, 0)
        self.assertEqual(contar_figura_de_color(j,DORADO),{ELEFANTE:1, GATO:2,CAMELLO:1,CABALLO:1,CONEJO:7,PERRO:1  })
        self.assertEqual(contar_figura_de_color(j,PLATEADO),{ELEFANTE:1, GATO:1,CAMELLO:1,CONEJO:7})

class test_puede_promover(unittest.TestCase):
    def test_puede_promover(self):
        t1 = leer_tablero([
                              'rr------', #7
                              'c---R-me', #6
                              '---Ed-R-', #5
                              '-M---R--', #4
                              '---R----', #3
                              '-rrrr---', #2
                              '-H---DCC', #1
                              'R-----RR', #0
                              #01234567
                            ])
        t2 = leer_tablero([
                                      'rr------', #7
                                      'c---R-me', #6
                                      '---E--R-', #5
                                      '-M---R--', #4
                                      '---R----', #3
                                      '-rrrr---', #2
                                      '-H---DCC', #1
                                      'R-----RR', #0
                                      #01234567
                                    ])
        j1 = Juego(t2, DORADO, 0)
        j2=Juego(t1,PLATEADO,0)
        self.assertTrue(puede_promover(j1))
        self.assertFalse(puede_promover(j2))




if __name__ == '__main__':
    unittest.main(verbosity=2)
