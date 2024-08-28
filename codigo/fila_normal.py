class FilaNormal:
    codigo:int = 0
    fila = []
    clienteatendidos = []
    senhatual: str = ""

    def gerarsenhatual(self) -> None:
        self.senhatual = self.codigo

    def chamarcliente(self, caixa:str) -> str:
        return 'teste' +  caixa