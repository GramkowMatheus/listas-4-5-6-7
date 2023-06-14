class UnidadeMilitar:
    def mover(self):
        print("A unidade está se movendo.")

    def atacar(self):
        print("A unidade está atacando.")


class Soldado(UnidadeMilitar):
    def mover(self):
        print("O soldado está marchando para frente.")

    def atacar(self):
        print("O soldado está atacando com sua espada.")


class Arqueiro(UnidadeMilitar):
    def mover(self):
        print("O arqueiro está se deslocando furtivamente.")

    def atacar(self):
        print("O arqueiro está atirando flechas.")


class Cavaleiro(UnidadeMilitar):
    def mover(self):
        print("O cavaleiro está galopando em seu cavalo.")

    def atacar(self):
        print("O cavaleiro está investindo com sua lança.")


unidades = [Soldado(), Arqueiro(), Cavaleiro()]

for unidade in unidades:
    unidade.mover()
    unidade.atacar()
    print()
