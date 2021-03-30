grille_actuelle = [["B1","B2","B3","B4","0","0","N1","N2","N3","N4"]]

def coup_valide(pion):
  for pion in grille_actuelle :
    for p in range (len(grille_actuelle)):

        if pion == "B1" or "B2" or "B3" or "B4" :
          if grille_actuelle[ p + 1] == "0" :

            return True
          
          elif grille_actuelle[ p + 2] == "0" :

            return True

          else : return False

        elif pion == "N1" or "N2" or "N3" or "N4" :
          if grille_actuelle[ p - 1] == "0" :

            return True
          
          elif grille_actuelle[ p - 2] == "0" :

            return True

          else : return False
        
        else : return False
      
      else : return False

print(coup_valide("B1"))
