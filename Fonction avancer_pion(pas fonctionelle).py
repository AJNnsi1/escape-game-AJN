grille = ["B1", "B2", "B3", "B4", "0", "0", "N1", "N2", "N3", "N4"]


def avancer_pion(grille, index):

    for i in range(1, 5):
      b = "B" + str(i)
      n = "N" + str(i)

      if grille[index] == b:

        if grille[index + 1] == "0" :

          t = grille[index]
          grille[index] = grille[index + 1]
          grille[index + 1] = t

          return grille
       
        for i in range(1,5):
          b = "B" + str(i)
          n = "N" + str(i)

          if grille[index + 2] == "0" :

           t = grille[index]
           grille[index] = grille[index + 2]
           grille[index + 2] = t

           return grille

          else :

             return "impossible"
            
      elif grille[index] == n:

         if grille[index - 1] == "0" :

           t = grille[index]
           grille[index] = grille[index - 1]
           grille[index - 1] = t

           return grille

         else :

             for i in range(1,5) :
               b = "B" + str(i)
               n = "N" + str(i)

               if grille[index - 1] == b or n :

                  if grille[index - 2] == "0" :

                    t = grille[index]
                    grille[index] = grille[index - 2]
                    grille[index - 2] = t

                    return grille

                  else :

                     return "impossible"

      if grille[index] == "0":

        return "impossible"


nouvelle_grille = avancer_pion(grille, 9)

print(nouvelle_grille)
