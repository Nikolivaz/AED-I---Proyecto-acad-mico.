from definiciones import *

#### Algunas funciones ya dadas

def son_posiciones_vecinas(pos1 : Posicion, pos2 : Posicion) -> bool: # pragma: no cover
    return (pos1.fila == pos2.fila and abs(pos1.columna - pos2.columna) == 1) \
        or (pos1.columna == pos2.columna and abs(pos1.fila - pos2.fila) == 1)

def direccion_desde_hasta(pos1 : Posicion, pos2 : Posicion) -> Direccion: # pragma: no cover
    assert son_posiciones_vecinas(pos1, pos2)
    if pos1.fila < pos2.fila:
       return NORTE
    elif pos1.fila > pos2.fila:
       return SUR
    elif pos1.columna < pos2.columna:
       return ESTE
    else:
       return OESTE

def pasar_turno(j : Juego) -> Juego: # pragma: no cover
    return Juego(j.tablero, oponente(j.turno), 0)

#### Ejercicio 1

def tablero_bien_formado(t : Tablero) -> bool:
    """
    Indica si el tablero *t* esta bien formado

    PRE: True

    Args:
       t (Tablero): Es el tablero del que se indicara si esta bien formado
    
    Returns:
       Devuele True si el tablero *t* esta bien formado si no False
    """
    res:bool = True 
    for fila in t:
        res = res and len(fila) == ANCHO 
    return res and len(t) == ALTO

def posicion_en_tablero(pos : Posicion) -> bool:
    """
    Indica si la posicion *pos* pertece al tablero

    PRE: True

    Args: 
       pos (Posicion): Es la posicion que chequeara su pertenencia al tablero
    
    Returns:
       True si la posicon pertenece al tablero si no False
    """
    
    return ( 0 <= pos.fila and pos.fila < ALTO) and (0 <= pos.columna and pos.columna < ANCHO)
     

def movimiento_bien_formado(m : Movimiento) -> bool:
    """
    Indica si el movimiento *m* es valido

    PRE: True

    Args:
       m (Movimiento): Es el movimiento que vamos a revisar
    
    Returns:
          True si el movimiento *m* es valido si no False
    """
    
    return posicion_en_tablero(m.origen) and  ((m.accion ==  MOVER_A_SECAS and len(m.pasos) == 1 )or( m.accion == ARRASTRAR and len(m.pasos) == 2 )or (m.accion == EMPUJAR and len(m.pasos) == 2))

def juego_bien_formado(j : Juego) -> bool:
    """
    Indica si el juego es valido

    PRE: True

    Args:
      j (Juego): Juego del que se revisara su validez
    
    Returns:
       True si el juego *j* es valdio si no False
    """
    return tablero_bien_formado(j.tablero) and (0<= j.pasos_consumidos and j.pasos_consumidos < MAX_PASOS) 
        

#### Ejercicio 2

def posicion_vecina_hacia(pos : Posicion, d : Direccion) -> Posicion:
    """
    indica la posición vecina desde una posición inicial *pos* hacia una direccion *d*
    
    PRE: True

    Args:
        pos(Posicion):Es la  posicion de la 1ue se quiere saber la vecina
        d(Direccion): Es la direccion en la que estara la posicion vecina que se pregunta

    Returns: 
        La posicion vecina dessde una posicion *pos* hacia la direccion *d* 
    """
    
    if d == NORTE:
        res:Posicion = Posicion(pos.fila+1, pos.columna) 
    if d == SUR:
            res:Posicion = Posicion(pos.fila-1, pos.columna) 
    if d == ESTE:
            res:Posicion= Posicion(pos.fila, pos.columna +1) 
    if d == OESTE:
            res:Posicion = Posicion(pos.fila, pos.columna -1)

    return res  

def casilla_en_posicion(t : Tablero, p : Posicion) -> Casilla:
    """
    Indica lo que contiene la casilla de la posicion *p* en el tablero *t*
    
    PRE: tablero_bien_formado(t) y posicion_en_tablero(p)

    Args: 
       t(Tablero): Tablero del que se quiere saber que casilla hay en la posicion *p*
       p(posicion): Ubicacion en el tablero *t* de la casilla que quiero conocer

    Returns:
       Devuelve un casillero del tablero *t* en la posicion *p*
     """
    return t[p.fila][p.columna]

def hay_casilla_vacia(t : Tablero, pos : Posicion) -> bool:
    """
    Indica si la casilla hallada en el tablero *t* en la posicion *pos* esta vacia o no

    PRE: tablero_bien_formado(t) y posicion_en_tablero(pos)
    
    Args:
       t(Tablero): Es el tablero del cual revisare si la posicion *pos* es vacia o no
       pos(Posicion): Es la posicion del tablero *t* que revisare si esta vacia o no

    Returns:
       True si la posicion *pos* en el tablero *t* es VACIA si no False

    """
    return posicion_en_tablero(pos) and  t[pos.fila][pos.columna] == VACIA

def hay_pieza_de_color(t : Tablero, pos : Posicion, col : Color) -> bool:
    """
    Indica si la pieza es del color *col* en la posicion *pos* del tablero *t*

    PRE: tablero_bien_formado(t) y posicion_en_tablero(pos)

    Args:
       t (Tablero): Es el tablero del cual se indicara si el color *col* coincide con alguna pieza en la posicion *pos*
       pos (Poisicion): Es la posicion del Tablero en la que revisare si hay alguna pieza del color *col*
       col(Color): Es el color del cual quiero saber si coincide con la la pieza en la posicion (pos) del tablero *t*
    
    Returns:
       True si hay una pieza cualquiera del mismo color que *col* en la posicion *pos* del tablero *t* si no False
    """

    res: bool = False 
    for f in Figura:
        res = res or  aux_hay_figura_de_color(t,pos,f,col)
    return res

def aux_hay_figura_de_color(t:Tablero,pos : Posicion, f: Figura , col : Color)-> bool : 
    """
    Indica si en la posicion *pos* del tanblero *t* hay una figura *f* de color *col*
    
    PRE: tablero_bien_formado(t) y posicion_en_tablero(pos)
    
    Args:
       t(Tablero): Es el tablero en el que mirare el color *col* de la figura *f* de la posicion *pos*
       pos(Posicion): Es una posicion dentro del Tablero *t*
       f(Figura): Es una figura que esta en la posicion *pos* de la que quiero saber si es de color *col*
       col(Color): Es el color del que quiero saber si la figura *f * es o no

    Returns: 
       True si la figura *f* que esta en el tablero *t* en la posicion *pos* es del color *col* si no False
    """
    return posicion_en_tablero(pos) and not hay_casilla_vacia(t,pos) and t[pos.fila][pos.columna].figura == f and t[pos.fila][pos.columna].color == col
     
#### Ejercicio 3

def aux_posicion_vecina(pos : Posicion, d : Direccion) -> Posicion:
    """
    Devuelve la posicion vecina en la direccion

    PRE: True.

    Args:
        pos (Posicion): posicion que busca la vecina
        d (Direccion): direccion que se busca

    Returns:
        La posicion vecina en la direccion indicada
    """
    vecina: Posicion = posicion_vecina_hacia(pos, d)
    # El ejercicio 2 devuelve una tupla, la pasamos a Posicion.
    res: Posicion = Posicion(vecina[0], vecina[1])
    return res

def hay_casilla_vacia_hacia(t : Tablero, pos : Posicion, d : Direccion) -> bool:
    """
    Indica si hay una casilla vacia en la direccion dada

    PRE: tablero bien formado y pos dentro del tablero

    Args:
        t (Tablero): tablero del juego
        pos (Posicion): posicion de origen
        d (Direccion): direccion donde busca la casilla

    Returns:
        True si la casilla vecina esta vacia, False si no
    """
    pos_v: Posicion = aux_posicion_vecina(pos, d)
    res: bool = False
    if posicion_en_tablero(pos_v):
        res = hay_casilla_vacia(t, pos_v)
    return res

def hay_pieza_amiga_vecina(t : Tablero, pos : Posicion) -> bool:
    """
    Indica si la pieza ubicada en la posicion dada tiene al menos una pieza amiga en alguna casilla a su lado

    PRE: tablero bien formado, pos dentro del tablero y hay una pieza en pos

    Args:
        t (Tablero): tablero del juego
        pos (Posicion): posicion de la pieza

    Returns:
        True si tiene alguna pieza amiga vecina, False si no
    """
    col_pieza: Color = t[pos.fila][pos.columna].color
    direcciones: list[Direccion] = [NORTE, SUR, ESTE, OESTE]
    tiene_amiga: bool = False

    for d in direcciones:
        pos_v: Posicion = aux_posicion_vecina(pos, d)
        if posicion_en_tablero(pos_v):
            if hay_pieza_de_color(t, pos_v, col_pieza):
                tiene_amiga = True
    return tiene_amiga

def hay_pieza_enemiga_mas_debil_hacia(t : Tablero, pos : Posicion, d : Direccion) -> bool:
    """
    Indica si hay una pieza enemiga mas debil en la direccion dada

    PRE: tablero bien formado, pos dentro del tablero y hay una pieza en pos

    Args:
        t (Tablero): tablero del juego.
        pos (Posicion): posicion de la pieza.
        d (Direccion): direccion donde busca la enemiga

    Returns:
        True si hay una pieza enemiga mas debil en esa direccion, False si no
    """
    pieza: Casilla = t[pos.fila][pos.columna]
    pos_v: Posicion = aux_posicion_vecina(pos, d)
    res: bool = False

    if posicion_en_tablero(pos_v):
        if hay_pieza_de_color(t, pos_v, oponente(pieza.color)):
            pieza_enemiga: Casilla = t[pos_v.fila][pos_v.columna]
            if fuerza(pieza.figura) > fuerza(pieza_enemiga.figura):
                res = True
    return res

def aux_hay_enemiga_mas_fuerte_hacia(t : Tablero, pos : Posicion, d : Direccion) -> bool:
    """
    Indica si hay una pieza enemiga mas fuerte en la direccion dada

    PRE: tablero bien formado, pos dentro del tablero y hay una pieza en pos

    Args:
        t (Tablero): tablero del juego.
        pos (Posicion): posicion de la pieza.
        d (Direccion): direccion donde se busca la enemiga

    Returns:
        True si hay una pieza enemiga mas fuerte en esa direccion, False si no
    """
    pieza: Casilla = t[pos.fila][pos.columna]
    pos_v: Posicion = aux_posicion_vecina(pos, d)
    res: bool = False

    if posicion_en_tablero(pos_v):
        if hay_pieza_de_color(t, pos_v, oponente(pieza.color)):
            pieza_enemiga: Casilla = t[pos_v.fila][pos_v.columna]
            if fuerza(pieza.figura) < fuerza(pieza_enemiga.figura):
                res = True
    return res

def hay_pieza_enemiga_mas_fuerte_vecina(t : Tablero, pos : Posicion) -> bool:
    """
    Indica si hay al menos una pieza enemiga mas fuerte junto a la pieza
    PRE: tablero bien formado, pos dentro del tablero
    Args:
        t (Tablero): tablero del juego
        pos (Posicion): posicion de la pieza
    Returns:
        True si tiene alguna pieza enemiga mas fuerte vecina, False si no
    """
    direcciones: list[Direccion] = [NORTE, SUR, ESTE, OESTE]
    res: bool = False
    for d in direcciones:
        if aux_hay_enemiga_mas_fuerte_hacia(t, pos, d):
            res = True
    return res

def hay_pieza_congelada(t : Tablero, pos : Posicion) -> bool:
    """
    Indica si una pieza esta congelada por una enemiga mas fuerte y sin amigas vecinas
    PRE: tablero bien formado y pos dentro del tablero
    Args:
        t (Tablero): tablero del juego.
        pos (Posicion): posicion que se quiere comprobar
    Returns:
        True si hay una pieza congelada en pos, False si no
    """
    res: bool = False
    if not hay_casilla_vacia(t, pos):
        if hay_pieza_enemiga_mas_fuerte_vecina(t, pos):
            if not hay_pieza_amiga_vecina(t, pos):
                res = True
    return res

#### Ejercicio 4

def aux_direccion_habilitada(t : Tablero, pos : Posicion, d : Direccion) -> bool:
    """
    Indica si la direccion esta habilitada para la pieza
    PRE: tablero bien formado, pos dentro del tablero y hay una pieza en pos
    Args:
        t (Tablero): tablero del juego
        pos (Posicion): posicion de la pieza
        d (Direccion): direccion del movimiento
    Returns:
        True si la pieza puede moverse en esa direccion, False si no
    """
    pieza: Casilla = casilla_en_posicion(t, pos)
    res: bool = True
    if pieza.figura == CONEJO:
        if pieza.color == DORADO and d == SUR:
            res = False
        if pieza.color == PLATEADO and d == NORTE:
            res = False
    return res
    # pieza: Casilla = casilla_en_posicion(t, pos)
    #     return  pieza.figura == CONEJO and ((not (pieza.color == DORADO and d == SUR) )or (not (pieza.color == PLATEADO and d == NORTE)) )
def aux_puede_realizar_accion(t : Tablero, m : Movimiento) -> bool:
    """
    Indica si el tablero permite la accion del movimiento
    PRE: tablero bien formado, movimiento bien formado y una pieza en el origen
    Args:
        t (Tablero): tablero del juego
        m (Movimiento): movimiento que se quiere realizar
    Returns:
        True si el tablero permite realizar la accion, False si no
    """
    pos: Posicion = m.origen
    d: Direccion = m.pasos[0]
    res: bool = False

    if m.accion == MOVER_A_SECAS:
        res = hay_casilla_vacia_hacia(t, pos, d)
    elif m.accion == ARRASTRAR:
        res = hay_casilla_vacia_hacia(t, pos, d) and hay_pieza_enemiga_mas_debil_hacia(t, pos, opuesta(m.pasos[1]))
    else: #Empujar
        pos_enemiga: Posicion = aux_posicion_vecina(pos, d)
        if hay_pieza_enemiga_mas_debil_hacia(t, pos, d):
            res = hay_casilla_vacia_hacia(t, pos_enemiga, m.pasos[1])
    return res

def puede_realizar_movimiento(j : Juego, m : Movimiento) -> bool:
    """
    Indica si se puede realizar el movimiento en el turno actual.
    PRE: el juego y el movimiento estan bien formados.
    Args:
        j (Juego): estado actual del juego
        m (Movimiento): movimiento que se quiere realizar
    Returns:
        True si el movimiento se puede realizar, False si no
    """
    t: Tablero = j.tablero
    pos: Posicion = m.origen
    pasos: int = j.pasos_consumidos + len(m.pasos)
    
    return (hay_pieza_de_color(t, pos, j.turno) and (not hay_pieza_congelada(t, pos)) and (aux_direccion_habilitada(t, pos, m.pasos[0]) 
                and pasos <= MAX_PASOS) and aux_puede_realizar_accion(t, m))

#### Ejercicio 5

def activar_trampas(t : Tablero) -> Tablero:
    """
    Verifica que el tablero este bien formado y retira las piezas en casillas trampa sin piezas amigas vecinas
    
    PRE: tablero_bien_formado(t)

    Args:
        t (Tablero): Es el tablero sobre el que se activan las trampas

    Returns:
        Un tablero bien formado igual a *t*, salvo que las casillas trampa ocupadas por una pieza sin amigas vecinas quedan VACIA.

    """
    tablero_nuevo: Tablero = []
    for fila in range(len(t)):
        tablero_nuevo.append([])
        for columna in range(len(t)):
            tablero_nuevo[fila].append(t[fila][columna])

    if tablero_bien_formado(t):
        for pos_trampa in POSICIONES_TRAMPA:
            f: int = pos_trampa.fila
            c: int = pos_trampa.columna

            if (not hay_casilla_vacia(t, pos_trampa)) and (not hay_pieza_amiga_vecina(t, pos_trampa)):
                    tablero_nuevo[f][c] = VACIA
    return tablero_nuevo

#### Ejercicio 6

def aux_trasladar_pieza(t : Tablero, origen : Posicion, destino : Posicion) -> Tablero:
    """
    Mueve una pieza de una casilla a otra del tablero
    PRE: origen y destino estan dentro del tablero, hay una pieza en origen y destino esta vacio
    Args:
        t (Tablero): tablero donde se mueve la pieza
        origen (Posicion): posicion de la pieza
        destino (Posicion): posicion a la que se mueve
    Returns:
        El tablero con la pieza trasladada
    """
    pieza: Casilla = t[origen.fila][origen.columna]
    t[destino.fila][destino.columna] = pieza
    t[origen.fila][origen.columna] = VACIA
    return t


def realizar_movimiento(j : Juego, m : Movimiento) -> Juego:
    """
    Realiza un movimiento y actualiza el tablero y el turno
    PRE: el juego y el movimiento estan bien formados y el movimiento es valido
    Args:
        j (Juego): estado actual del juego
        m (Movimiento): movimiento que se va a realizar
    Returns:
        El juego despues de realizar el movimiento
    """
    t_nuevo: Tablero = []
    for fila in j.tablero:
        fila_nueva: list[Casilla] = fila.copy()
        t_nuevo.append(fila_nueva)

    pos: Posicion = m.origen
    d: Direccion = m.pasos[0]
    pos_v: Posicion = aux_posicion_vecina(pos, d)

    if m.accion == MOVER_A_SECAS:
        t_nuevo = aux_trasladar_pieza(t_nuevo, pos, pos_v)

    elif m.accion == ARRASTRAR:
        pos_enemiga: Posicion = aux_posicion_vecina(pos, opuesta(m.pasos[1]))
        t_nuevo = aux_trasladar_pieza(t_nuevo, pos, pos_v)
        t_nuevo = aux_trasladar_pieza(t_nuevo, pos_enemiga, pos)

    elif m.accion == EMPUJAR:
        pos_destino: Posicion = aux_posicion_vecina(pos_v, m.pasos[1])
        t_nuevo = aux_trasladar_pieza(t_nuevo, pos_v, pos_destino)
        t_nuevo = aux_trasladar_pieza(t_nuevo, pos, pos_v)

    t_nuevo = activar_trampas(t_nuevo)

    pasos: int = j.pasos_consumidos + len(m.pasos)
    turno: Color = j.turno

    if pasos == MAX_PASOS:
        pasos = 0
        turno = oponente(j.turno)

    res: Juego = Juego(t_nuevo, turno, pasos)
    return res

#### Ejercicio 7

## Primero defino las funciones auxiliares que me ayudaran a determinar al ganador.
def auxEsInicioDeTurno(j: Juego, col: Color) -> bool:
    """
    Indica si actualmente es el inicio del turno del jugador.
        
    PRE: True

    Args:
        j (Juego): Es el juego que se revisa
        col (Color): Es el color del jugador del que se quiere saber si empieza su turno

    Returns:
        True si es el turno de *col* y todavia no consumio ningun paso, si no False

    """
    res: bool = (j.turno == col) and (j.pasos_consumidos == 0)
    return res

def auxHayConejoEnTablero(j: Juego, col: Color) -> bool:
    """
    Verifica si el jugador tiene por lo menos un conejo en cualquier casilla.
        
    PRE: juego_bien_formado(j)

    Args:
        j (Juego): Es el juego cuyo tablero se revisa
        col (Color): Es el color del jugador del que se buscan los conejos

    Returns:
        True si hay al menos un conejo de color *col* en el tablero de *j*, si no False

    """
    hay_conejo: bool = False
    for f in range(ALTO):
        for c in range(ANCHO):
            pos: Posicion = Posicion(f, c)
            hay_conejo= hay_conejo or aux_hay_figura_de_color(j.tablero, pos, CONEJO, col)
    return hay_conejo

def auxHayConejoEnFilaInicialOponente(j: Juego, col: Color) -> bool:
    """
    Verifica si el jugador tiene al menos un conejo en la fila inicial del oponente.
        
    PRE: juego_bien_formado(j)

    Args:
        j (Juego): Es el juego cuyo tablero se revisa
        col (Color): Es el color del jugador que busca llegar a la fila inicial del oponente

    Returns:
        True si hay al menos un conejo de color *col* en la fila inicial del oponente, si no False

    """
    fila_meta: int = 7 if col == DORADO else 0
    hay_conejo_meta: bool = False

    for c in range(ANCHO):
        pos: Posicion = Posicion(fila_meta, c)
        hay_conejo_meta= hay_conejo_meta or aux_hay_figura_de_color(j.tablero, pos, CONEJO, col)
    return hay_conejo_meta

def auxReuneCondicionesDeGanar(j: Juego, col: Color) -> bool:
    """
    Evalua si un jugador cumple alguna de las dos condiciones de victoria.
        
    PRE: juego_bien_formado(j)

    Args:
        j (Juego): Es el juego que se evalua
        col (Color): Es el color del jugador del que se evalua si reune las condiciones

    Returns:
        True si *col* cumple al menos una de las dos condiciones de victoria, si no False

    """
    res: bool = auxHayConejoEnFilaInicialOponente(j, col) or not auxHayConejoEnTablero(j, oponente(col))
    return res

def auxReuneCondicionesDeGanarExclusivas(j: Juego, col: Color) -> bool:
    """
    Evalua si un jugador reune las condiciones de ganar si su oponente no las cumple.
        
    PRE: juego_bien_formado(j)

    Args:
        j (Juego): Es el juego que se evalua
        col (Color): Es el color del jugador del que se evalua si reune las condiciones

    Returns:
        True si *col* cumple al menos una de las dos condiciones de victoria, si no False

    """
    res: bool = auxReuneCondicionesDeGanar(j, col) and not auxReuneCondicionesDeGanar(j, oponente(col))
    return res

def auxEsJugadorGanador(j: Juego, col: Color) -> bool:
    """
    Determina si un jugador resulta ganador.
        
    PRE: juego_bien_formado(j)

    Args:
        j (Juego): Es el juego que se evalua
        col (Color): Es el color del jugador del que se evalua si es el unico que reune las condiciones

    Returns:
        True si *col* reune las condiciones de victoria y su oponente no, si no False

    """
    op: Color = oponente(col)
    
    primerCondicion: bool = auxEsInicioDeTurno(j, op) and auxReuneCondicionesDeGanar(j, col)
    segundaCondicion: bool = auxEsInicioDeTurno(j, col) and auxReuneCondicionesDeGanarExclusivas(j, col)
    
    res: bool = primerCondicion or segundaCondicion
    return res


## Uso las funciones auxiliares y determino el jugador ganador.
def hay_ganador_determinado(j : Juego) -> bool:
    """
    Indica si existe un ganador determinado.
    
     PRE: juego_bien_formado(j)

    Args:
        j (Juego): Es el juego del que se quiere saber si hay ganador

    Returns:
        True si alguno de los dos jugadores es ganador de *j*, si no False

    """
    res: bool = juego_bien_formado(j) and (auxEsJugadorGanador(j, DORADO) or auxEsJugadorGanador(j, PLATEADO))
    return res

def ganador_del_juego(j : Juego) -> Color:
    """
    Devuelve el color del jugador ganador.
        
    PRE: juego_bien_formado(j) y hay_ganador_determinado(j)

    Args:
        j (Juego): Es el juego del que se quiere conocer al ganador

    Returns:
        El color del jugador que es ganador de *j*

    """
    res: Color = PLATEADO
    if juego_bien_formado(j) and hay_ganador_determinado(j) and auxEsJugadorGanador(j, DORADO):
        res = DORADO
    return res

#Ejercicios de Evaluacion 

def contar_figura_de_color(j: Juego, col: Color) -> dict:
    res: dict = {}
    figura: int = 0
    for fila in range(ALTO):
        stop = False
        for columna in range(ANCHO):
            pos = Posicion(fila,columna)
            if hay_pieza_de_color(j.tablero, pos, col):
                if Pieza.figura not in res:
                    res[Pieza.figura] = 0

                res[Pieza.figura] += 1
   
    return (res, figura)  
          

def puede_promover(j: Juego) -> bool:
    res: bool = False
    paccion = MOVER_A_SECAS
    for columna in range(ANCHO):
        if hay_pieza_de_color(j.tablero, Posicion(6,columna), DORADO):
            m: Movimiento = Movimiento(paccion, Posicion(6, columna), [NORTE])
            if movimiento_bien_formado(m) and puede_realizar_movimiento(j,m) and not auxHayConejoEnFilaInicialOponente(j, oponente(j.turno)):
                res = True      
        elif hay_pieza_de_color(j.tablero, Posicion(1,columna), PLATEADO):
            ppos = Posicion(1, columna)
            m: Movimiento = Movimiento(paccion, Posicion(1, columna), [SUR])
            if movimiento_bien_formado(m) and puede_realizar_movimiento(j,m) and not auxHayConejoEnFilaInicialOponente(j, oponente(j.turno)):
                res = True
    return res




