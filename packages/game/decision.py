from operator import itemgetter

from config import *


def score_candidates(board, candidates_coo):
    """
    Calcule le score de chaque candidat.

    :param board: matrix le plateau
    :param candidates_coo: list la liste des coordonnées des candidats
    :return: la liste des candidats contenant également leur type et leur score
    """

    candidates = []
    for c in candidates_coo:

        # récupération des caractéristiques
        x = c[0]
        y = c[1]
        type = board[y][x][0]
        weight = board[y][x][1]
        value = 0

        # on attribue la valeur en fonction du type
        if isinstance(type, int):
            value = MOY_VAL_MOULE  # MOULE
        elif type == BIERE:
            value = MOY_VAL_MOULE + BONUS_BIERE
        elif type == FRITE:
            value = MOY_VAL_MOULE + BONUS_FRITE

        # calcul du score
        score = value / weight

        candidates.append((score, (x, y), type, weight))
    return candidates


def choose_objective(in_candidates):
    """
    Élit un candidat en tant qu'objectif.

    :param candidates: list la liste scorée des candidats
    :return: (y,x) le tuple coordonnée de l'objectif choisi
    """

    # valeur de retour
    objective_coo = ()

    # filtrage basique des candidats via le score
    max_score = max([c[0] for c in in_candidates])
    candidates = [e for e in in_candidates if e[0] == max_score]

    # filtrage avancé si égalité(s)
    if len(candidates) == 1:
        # on le tiens !
        objective_coo = candidates[0][1]

    else:
        # au plus proche
        candidates.sort(key=itemgetter(3))
        min_weight = min([c[3] for c in candidates])
        candidates = [e for e in candidates if e[3] == min_weight]

        if len(candidates) == 1:
            # on le tiens !
            objective_coo = candidates[0][1]

        else:
            # en fonction du type maintenant BIERE>MOULE>FRITE
            for c in candidates:
                if c[2] == FRITE:
                    # on le tiens !
                    objective_coo = c[1]
                    break
            for c in candidates:
                if c[2] == isinstance(type, int):
                    # on le tiens !
                    objective_coo = c[1]
                    break
            for c in candidates:
                if c[2] == BIERE:
                    # on le tiens !
                    objective_coo = c[1]
                    break

    return objective_coo


def ask_for_objective(board, candidates_coo):
    """Choisit l'élu."""
    return choose_objective(score_candidates(board, candidates_coo))
