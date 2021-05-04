var grille_courante=new Array ();
grille_courante[0]="B1";
grille_courante[1]="B2";
grille_courante[2]="B3";
grille_courante[3]="B4";
grille_courante[4]="0";
grille_courante[5]="0";
grille_courante[6]="N1";
grille_courante[7]="N2";
grille_courante[8]="N3";
grille_courante[9]="N4";

Function av(grille_courante,index) {
  for (let i = 0;i = 4;i++){
    let b = "B" + string(i)
    let n = "N" + string(i)

    if grille_courante[index] == b {

      if grille_courante[index + 1] == "0" {
        
        let t = grille_courante[index]
        let grille_courante[index] = grille_courante[index + 1]
        let grille_courante[index + 1] = t

        return grille_courante
         }

      for (let i = 0;i = 4;i++){
        let b = "B" + string(i)
        let n = "N" + string(i)

        if grille_courante[index + 2] == "0" {

        let t = grille_courante[index]
        let grille_courante[index] = grille_courante[index + 2]
        let grille_courante[index + 2] = t

        return grille_courante 
        } else {

          return "impossible"
        }
      } 
    } else if grille_courante[index] == n {

      if grille_courante[index - 1] == "0" {
        
        let t = grille_courante[index]
        let grille_courante[index] = grille_courante[index - 1]
        let grille_courante[index - 1] = t

        return grille_courante
         } else {
            for (let i = 0;i = 4;i++){
            let b = "B" + string(i)
            let n = "N" + string(i)
              if 


         }
        }


  }



}
