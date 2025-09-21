# * Tarea 4 * #

# Verificar si na cadena es Palíndromo

def Palindromo(text, n, i):
    if i == 0:
        return print("La cadena de texto esta vacia")
        
    if text[n] != text[i - 1]:
        return False
    elif n == i or n > i:
        return True
    else: 
        return Palindromo(text, n + 1, i - 1)
    
text = ""
text = text.lower()
text = text.replace(" ", "")
tamaño = len(text)
vof = Palindromo(text, 0, tamaño)

if vof:
    print(f"El texto: {text}\nEs un palindromo.  :)")
else: 
    print(f"El texto: {text}\nNo es un palindromo.  :)")