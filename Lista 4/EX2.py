class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def acelerar(self):
        print("Acelerando o veículo!")
    
    def frear(self):
        print("Freando o veículo!")

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, cor):
        super().__init__(marca, modelo, ano)
        self.cor = cor
    
    def ligarRadio(self):
        print("Ligando o rádio do carro!")
    
    def abrirPorta(self):
        print("Abrindo a porta do carro!")

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindrada):
        super().__init__(marca, modelo, ano)
        self.cilindrada = cilindrada
    
    def empinar(self):
        print("Empinando a moto!")
    
    def buzinar(self):
        print("Buzinando a moto!")

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano, cargaMaxima):
        super().__init__(marca, modelo, ano)
        self.cargaMaxima = cargaMaxima
    
    def carregar(self):
        print("Carregando o caminhão!")
    
    def descarregar(self):
        print("Descarregando o caminhão!")


carro = Carro("Ford", "Fiesta", 2020, "vermelho")
moto = Moto("Honda", "CBR 1000", 2021, "1000cc")
caminhao = Caminhao("Volvo", "FH", 2019, "30 toneladas")

carro.acelerar()
carro.frear()
carro.ligarRadio()
carro.abrirPorta()

moto.acelerar()
moto.frear()
moto.empinar()
moto.buzinar()

caminhao.acelerar()
caminhao.frear()
caminhao.carregar()
caminhao.descarregar()