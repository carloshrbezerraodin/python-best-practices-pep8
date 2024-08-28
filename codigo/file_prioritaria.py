from codigo.filabase import FilaBase


class FilaPrioritaria(FilaBase):

    def gerar_senha_tual(self) -> None:
        self.senha_atual = self.codigo

    def gerar_dicionario(self) -> dict:
        return {'chave': 1}

