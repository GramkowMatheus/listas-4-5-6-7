class Assinatura:
    def calcularPreco(self):
        pass
    
    def exibirDetalhes(self):
        pass

class AssinaturaSimples(Assinatura):
    def calcularPreco(self):
        return 29.99
    
    def exibirDetalhes(self):
        print("Assinatura Simples - Acesso a filmes e séries em qualidade padrão.")

class AssinaturaPremium(Assinatura):
    def calcularPreco(self):
        return 49.99
    
    def exibirDetalhes(self):
        print("Assinatura Premium - Acesso a filmes e séries em qualidade HD e Ultra HD.")

assinaturaSimples = AssinaturaSimples()
assinaturaPremium = AssinaturaPremium()

assinaturas = [assinaturaSimples, assinaturaPremium]

for assinatura in assinaturas:
    print("Tipo de Assinatura:", type(assinatura).__name__)
    print("Preço:", assinatura.calcularPreco())
    assinatura.exibirDetalhes()
    print()
