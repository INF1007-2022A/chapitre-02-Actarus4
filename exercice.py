#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    def nouveaumot=""
    # TODO completer la fonction ici
    for i in len(mot):
         if ord(mot[i])>64:
                if ord(mot[i])>91:
                    if ord(mot[i])>123
                    nouveaumot+=mot[i]
                    else:
                    nouveaumot+='ord(mot[i])-32'
               else:
                nouveaumot+='ord(mot[i])+32'
         else:
            nouveaumot+=mot[i]
    return nouveaumot


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
