from typing import List, Dict, Union


class EstatisticaDetalhada:
    def __init__(self, dia: str) -> None:
        self.dia = dia

    def roda_estatistica(self, clientes_atendidos: List[str]) -> dict:
        estatistica: Dict[str, Union[List[str], str, int]] = {}
        estatistica[f'{self.agencia}-{self.dia}'] = len(clientes_atendidos)

        return estatistica

