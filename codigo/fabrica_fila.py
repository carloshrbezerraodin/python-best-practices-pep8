from typing import Union

from codigo.fila_normal import FilaNormal
from codigo.file_prioritaria import FilaPrioritaria


class FaricaFila:
    @staticmethod
    def pega_fila(self, tipo_fila)-> Union[FilaNormal, FilaPrioritaria]:
         if (tipo_fila == 'normal'):
             return FilaPrioritaria();
         elif (tipo_fila == 'prioritaria'):
             return FilaNormal()
         else:
             raise NotImplemented('tipo fila nao existe')
