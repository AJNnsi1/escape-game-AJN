grille_départ = [["B1","B2","B3","B4","0","0","N1","N2","N3","N4"]]

grille = [["B1","B2","B3","B4","0","0","N1","N2","N3","N4"]]

def coup_valide(grille,index):
    for p in range (len(grille)):
        for i in range (1,5) :
            b = "B" + str(i)
            n = "N" + str(i)
            
            if grille[index] == b :
                  
                if grille[ index + 1] == "0" :
        
                    return True
                  
                elif grille[ index + 2] == "0" :
        
                    return True
        
                else : return False
        
            if grille[index] == n :
                    
                if grille[ index - 1] == "0" :
        
                    return True
                  
                elif grille[ index - 2] == "0" :
        
                    return True
        
                else : return False
                
            else : return False



print(coup_valide("B1",0))
