"""
Ce script génère et analyse une suite de Syracuse.
Il affiche le temps de vol, le temps de vol en altitude et l'altitude maximale de la suite.
"""

from plotly.graph_objects import Scatter, Figure

#### Fonctions secondaires
### NE PAS MODIFIER ###
def syr_plot(lsyr):
    """
    Génère et affiche un graphique de la suite de Syracuse.

    Args:
        lsyr (list): La suite de Syracuse à tracer.
    """
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({
        'layout': {
            'title': {'text': title},
            'xaxis': {'title': {'text': "x"}},
            'yaxis': {'title': {'text': "y"}},
        }
    })

    x = list(range(len(lsyr)))  # Simplification demandée par l'analyse
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color="blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')
    #return None  # Useless return conservé car demandé par le commentaire

#######################

### Fonction tertiaire
# fonction qui crée une liste de la suite de syracuse
def syracuse_l(n):
    """
    Retourne la suite de Syracuse de source n.

    Args:
        n (int): La source de la suite.

    Returns:
        list: La suite de Syracuse de source n.
    """
    l = [n]
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        l.append(n)
    return l

### Fonction secondaire
# affiche le temps de vol
def temps_de_vol(l):
    """
    Retourne le temps de vol d'une suite de Syracuse.

    Args:
        l (list): La suite de Syracuse.

    Returns:
        int: Le temps de vol.
    """
    return len(l) - 1

### Fonction secondaire
# affiche le temps de vol en altitude
def temps_de_vol_en_altitude(l):
    """
    Retourne le temps de vol en altitude d'une suite de Syracuse.

    Args:
        l (list): La suite de Syracuse.

    Returns:
        int: Le temps de vol en altitude.
    """
    for i in range(1, len(l)):
        if l[i] < l[0]:
            return i - 1
    return 0

### Fonction secondaire
# affiche l'altitude max
def altitude_maximale(l):
    """
    Retourne l'altitude maximale d'une suite de Syracuse.

    Args:
        l (list): La suite de Syracuse.

    Returns:
        int: L'altitude maximale.
    """
    return max(l)

#### Fonction principale
# fonction qui fait tourner le code
# crée un liste de syracuse, et affiche son tps de vol, tps vol en attitude et altitude max
def main():
    """
    Affiche le temps de vol, le temps de vol en altitude et l'altitude maximale
    de la suite de Syracuse.
    """
    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))


if __name__ == "__main__":
    main()
