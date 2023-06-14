class Criptografia:
    def cifrar(self, texto):
        pass
    
    def decifrar(self, texto_cifrado):
        pass

class CifraCesar(Criptografia):
    def __init__(self, deslocamento):
        self.deslocamento = deslocamento
    
    def cifrar(self, texto):
        textoCifrado = ""
        for char in texto:
            if char.isalpha():
                asciiCode = ord(char)
                if char.islower():
                    base = ord('a')
                else:
                    base = ord('A')
                deslocado = (asciiCode - base + self.deslocamento) % 26 + base
                textoCifrado += chr(deslocado)
            else:
                textoCifrado += char
        return textoCifrado
    
    def decifrar(self, textoCifrado):
        textoDecifrado = ""
        for char in textoCifrado:
            if char.isalpha():
                asciiCode = ord(char)
                if char.islower():
                    base = ord('a')
                else:
                    base = ord('A')
                deslocado = (asciiCode - base - self.deslocamento) % 26 + base
                textoDecifrado += chr(deslocado)
            else:
                textoDecifrado += char
        return textoDecifrado

class CifraXor(Criptografia):
    def __init__(self, chave):
        self.chave = chave
    
    def cifrar(self, texto):
        textoCifrado = ""
        for char in texto:
            asciiCode = ord(char)
            cifrado = asciiCode ^ self.chave
            textoCifrado += chr(cifrado)
        return textoCifrado
    
    def decifrar(self, textoCifrado):
        textoDecifrado = ""
        for char in textoCifrado:
            asciiCode = ord(char)
            decifrado = asciiCode ^ self.chave
            textoDecifrado += chr(decifrado)
        return textoDecifrado


texto = "é o Grêmio"
cifraCesar = CifraCesar(3)
cifraXor = CifraXor(42)

textoCifrado = cifraCesar.cifrar(texto)
textoDecifrado = cifraXor.decifrar(textoCifrado)
print("Texto cifrado (Cifra de César):", textoCifrado)
print("Texto decifrado (Cifra de César):", textoDecifrado)

textoCifrado = cifraXor.cifrar(texto)
textoDecifrado = cifraXor.decifrar(textoCifrado)
print("Texto cifrado (Cifra XOR):", textoCifrado)
print("Texto decifrado (Cifra XOR):", textoDecifrado)