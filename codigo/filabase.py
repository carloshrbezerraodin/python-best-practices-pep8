import abc

from codigo.constantes import NUMERO_CONSTANTE


class FilaBase(metaclass=abc.ABC):
    codigo: int = 0
    fila = []
    senha_atual: str = ''

    @abc.abstractmethod
    def gerar_senha_tual(self) -> None:
        self.senha_atual = self.codigo + NUMERO_CONSTANTE