grille_courante = ["B1", "B2", "B3", "B4", "0", "0", "N1", "N2", "N3", "N4"] #création de la grille
#B1,B2,B3,B4=pion blanc/0,0=case vide/N1,N2,N3,N4=pion noir


def avancer_pion(grille_courante, index): #appel fonction avec argument: grille et index case sélectionnée

    for i in range(1, 5): #boucle pour obtenir: B1,B2,B3,B4,N1,N2,N3,N4
      b = "B" + str(i)
      n = "N" + str(i)

      if grille_courante[index] == b: #vérifier si case = pion blanc

        if grille_courante[index + 1] == "0" :#vérifier si case suivante est vide

          t = grille_courante[index] # fonction permuter(avancer pion blanc G->D)
          grille_courante[index] = grille_courante[index + 1]
          grille_courante[index + 1] = t

          return grille_courante # retourner la grille après le mouvement
       
        for i in range(1,5): #boucle pour obtenir: B1,B2,B3,B4,N1,N2,N3,N4
          b = "B" + str(i)
          n = "N" + str(i)

          if grille_courante[index + 2] == "0" : # vérifier si la case après la case suivante le ion blanc est vide

           t = grille_courante[index] # fonction permuter(avancer pion blanc G->D)
           grille_courante[index] = grille_courante[index + 2]
           grille_courante[index + 2] = t

           return grille_courante # retourner la grille après mouvement

          else : # si la case après la case suivante le pion blanc n'est pas vide

             return "impossible" # retourner impossible
            
      elif grille_courante[index] == n: # si case sélectionnée = pion noir

         if grille_courante[index - 1] == "0" : # vérifier si case avant pion noir est vide

           t = grille_courante[index] # fonction permuter(reculer pion noir D->G)
           grille_courante[index] = grille_courante[index - 1]
           grille_courante[index - 1] = t

           return grille_courante # retourner grille après mouvement

         else : # si case avant pion noir n'est pas vide

             for i in range(1,5) : #boucle pour obtenir: B1,B2,B3,B4,N1,N2,N3,N4
               b = "B" + str(i)
               n = "N" + str(i)

               if grille_courante[index - 1] == b or n : # si pion dans case avant pion noir

                  if grille_courante[index - 2] == "0" : # si case avant case avant pion noir vide

                    t = grille_courante[index] # permuter(reculer pion noir DD->G)
                    grille_courante[index] = grille_courante[index - 2]
                    grille_courante[index - 2] = t

                    return grille_courante # retourner grille après mouvement

                  else : # si case avant case avant pion noir n'est pas vide

                     return "impossible" # retourner impossible

      if grille_courante[index] == "0": # si case sélectionnée est vide

        return "impossible" # retourner impossible


nouvelle_grille = avancer_pion(grille_courante, 0)

print(nouvelle_grille)
