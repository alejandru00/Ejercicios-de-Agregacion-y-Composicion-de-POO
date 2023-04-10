

class Yin: pass 
class Yang: 
    def __del__(self): 
        print("Yang destruido") 
 
yin = Yin() 
yang = Yang() 
yin.yang = yang 
 
print(yang) 
print(yang is yin.yang) 

del(yang)
del(yin.yang)           # Linea añadida

print("?") 

"""

El mensaje de "Yang destruido" no se muestra porque el objeto Yang solo se destruye de yang, 
y no de yin.yang.

Para corregirlo serviria con escribir: del(yin.yang)

"""