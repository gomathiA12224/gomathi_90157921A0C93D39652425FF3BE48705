def linearSearchProduct(productlist, targetProduct):
 
   indices = []
   
 
    for index, product in enumerate(productlist):
     
   if product == targetProduct:
         
   indices.append(index)
    
  
  return indices


products = ["shoes", "boot", "Loafer", "shoes", "sandal", "shoes"]

target = "shoes"

target2= " apple"

result = linearSearchProduct(products, target)

print(result)