var grille_courante=new Array (); /// création grillel

grille_courante[0]="B1"; /// pion blanc
grille_courante[1]="B2"; /// pion blanc
grille_courante[2]="B3"; /// pion blanc
grille_courante[3]="B4"; /// pion blanc
grille_courante[4]="0";  /// case vide
grille_courante[5]="0";  /// case vide
grille_courante[6]="N1"; /// pion noir
grille_courante[7]="N2"; /// pion noir
grille_courante[8]="N3"; /// pion noir
grille_courante[9]="N4"; /// pion noir


function avancer_pion(grille_courante,index) { /// donner la grille avec l'index de case sélectionnée

  for (let i = 0; i < 5; i++) {   /// boucle pour obtenir B1,B2,B3,B4,N1,N2,N3,N4
    console.log(i);
    var b = "B" + String(i);
    var n = "N" + String(i);

    if (grille_courante[index] == b) {/// vérifier si case sélectionnée = pion blanc
  
      var test = 1
      console.log(test);

      if (grille_courante[index + 1] == "0") { /// vérifier si case suivante est vide

        t = grille_courante[index] ;/// fonction permuter(avancer pion blanc G->D)
        grille_courante[index] = grille_courante[index + 1] ;
        grille_courante[index + 1] = t ;

        return grille_courante /// retourner la grille après mouvement
         }

        if (grille_courante[index + 2] == "0") { /// vérifier si case après case suivante est vide
        var test = test +1
        console.log(test);

        t = grille_courante[index]  /// fonction permuter(avancer pion blanc G->D)
        grille_courante[index] = grille_courante[index + 2]
        grille_courante[index + 2] = t

        return grille_courante   /// retourner grille après mouvement
        } else { /// si case après case suivante=pas vide alors retourner impossible

          return "impossible"
        }
       
    } else if (grille_courante[index] == n) { /// si pion noir

      if (grille_courante[index - 1] == "0") { /// si case avant le pion noir est vide
        
        t = grille_courante[index] /// fonction permuter(reculer le pion noir D->G)
        grille_courante[index] = grille_courante[index - 1]
        grille_courante[index - 1] = t

        return grille_courante  /// retourner la grille après mouvement

         } else {   /// si case avant pion noir n'est pas vide
            for (let i = 1;i = 4;i++){   /// boucle pour obtenir B1,B2,B3,B4,N1,N2,N3,N4
            let b = "B" + string(i)
            let n = "N" + string(i)

              if (grille_courante[index - 1] = b / n) {   /// si case avant pion = pion
                if (grille_courante[index - 2] = "0"){   /// si case avant la case avant le pion est vide

                  t = grille_courante[index] /// fonction permuter(reculer pion noir D->G)
                  grille_courante[index]= grille_courante[index - 2]
                  grille_courante[index - 2] = t

                  return grille_courante /// retourner la grille après mouvement
                  } else { /// si case avant la case avant le pion noir n'est pas vide
                    
                    return "impossible" /// retourner impossible
                     }
                }
               }
             }
            }
          if (grille_courante[index] = "0"){  /// si case sélectionnée est vide
          return "impossible" }   /// retourner impossible
        }
}


var nouvelle_grille = avancer_pion(grille_courante,2)

//var grille_courante = ["B1","B2","B3","B4","0","0","N1","N2","N3","N4"]
console.log(nouvelle_grille);
