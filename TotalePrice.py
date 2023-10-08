pht=float(input("entrer le prix de produit :)) #pht est le prix hors taxe 
ctg=str(input("entrer la catégorie")                
    match ctr :
      case "A" : 
         pttc=pht*(1+0.07)
      case "B" :
         pttc=pht*(1+0.2)
      case "C" :
         pttc=pht*(1+0.25)
print("le Prix ttc de ce produit est :",pttc)
       
