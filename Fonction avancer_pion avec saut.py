grille_courante = ["B1", "B2", "B3", "B4", "0", "0", "N1", "N2", "N3", "N4"]
#grille_courante=grille_depart

def avancer_pion(grille_courante, index):

    for i in range(1, 5):
      b = "B" + str(i)
      n = "N" + str(i)

      if grille_courante[index] == b:

        if grille_courante[index + 1] == "0" :

          t = grille_courante[index]
          grille_courante[index] = grille_courante[index + 1]
          grille_courante[index + 1] = t

          return grille_courante
       
        for i in range(1,5):
          b = "B" + str(i)
          n = "N" + str(i)

          if grille_courante[index + 2] == "0" :

           t = grille_courante[index]
           grille_courante[index] = grille_courante[index + 2]
           grille_courante[index + 2] = t

           return grille_courante

           else :

             return "impossible"
            
        elif grille_courante[index] == n:

         if grille_courante[index - 1] == "0" :

            t = grille_courante[index]
           grille_courante[index] = grille_courante[index - 1]
           grille_courante[index - 1] = t

           return grille_courante

           else :

             for i in range(1,5) :
               b = "B" + str(i)
                n = "N" + str(i)

               if grille_courante[index - 1] == b or n :

                  if grille_courante[index - 2] == "0" :

                    t = grille_courante[index]
                    grille_courante[index] = grille_courante[index - 2]
                    grille_courante[index - 2] = t

                   return grille_courante

                   else :

                     return "impossible"

     if grille_courante[index] == "0":

        return "impossible"


nouvelle_grille = avancer_pion(grille_courante, 6)

print(nouvelle_grille)
#print(Est_victoire(grille_courante))
