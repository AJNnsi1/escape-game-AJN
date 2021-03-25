index=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
pions_noirs=["N1", "N2", "N3", "N4"]
pions_blancs=["B1", "B2", "B3", "B4"]

def victoire(index, pions_blancs, pions_noirs):
  if index[0,1,2,3]==pions_noirs[0,1,2,3] and index[6,7,8,9]==pions_blancs[0,1,2,3]:
    print("Félicitations! Vous avez réussi cette énigme! On passe à la suivante? ☺")
  else:
      print("Réessayez encore! Courage, vous allez y arriver! ☺")
  return victoire
