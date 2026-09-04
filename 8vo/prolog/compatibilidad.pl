    :- use_module(library(lists)).

    puntos_distancia(cerca, 25).
    puntos_distancia(media, 15).
    puntos_distancia(lejos, 8).
    puntos_distancia(muy_lejos, 0). 

    puntos_por_edad_en_rango(30).
    puntos_por_interes_comun(5).

    categoria_distancia(Distancia, cerca) :- Distancia =< 10.
    categoria_distancia(Distancia, media) :- Distancia > 10, Distancia =< 20.
    categoria_distancia(Distancia, lejos) :- Distancia > 20, Distancia =< 50.
    categoria_distancia(Distancia, muy_lejos) :- Distancia > 50.

    puntaje_distancia(Distancia, Puntaje) :-
        categoria_distancia(Distancia, Categoria),
        puntos_distancia(Categoria, Puntaje).

    puntaje_edad(EdadCandidato, EdadMinima, EdadMaxima, Puntaje) :-
        EdadCandidato >= EdadMinima,
        EdadCandidato =< EdadMaxima, !,
        puntos_por_edad_en_rango(Puntaje).

    puntaje_edad(EdadCandidato, EdadMinima, EdadMaxima, 0) :-
        EdadCandidato < EdadMinima ; EdadCandidato > EdadMaxima.

    intereses_en_comun([], _, 0).

    intereses_en_comun([Interes|Resto], InteresesCandidato, Cantidad) :-
        member(Interes, InteresesCandidato), !,
        intereses_en_comun(Resto, InteresesCandidato, CantidadRestante),
        Cantidad is CantidadRestante + 1.

    intereses_en_comun([_|Resto], InteresesCandidato, Cantidad) :-
        intereses_en_comun(Resto, InteresesCandidato, Cantidad).

    puntaje_intereses(Intereses1, Intereses2, Puntaje) :-
        intereses_en_comun(Intereses1, Intereses2, Cantidad),
        puntos_por_interes_comun(PuntosBase),
        Puntaje is Cantidad * PuntosBase.

    calcular_compatibilidad(EdadCandidato, EdadMinima, EdadMaxima, Intereses1, Intereses2, Distancia, PuntajeTotal) :-
        puntaje_edad(EdadCandidato, EdadMinima, EdadMaxima, PuntosEdad),
        puntaje_distancia(Distancia, PuntosDistancia),
        puntaje_intereses(Intereses1, Intereses2, PuntosIntereses),
        PuntajeTotal is PuntosEdad + PuntosDistancia + PuntosIntereses.