import sqlite3
from decimal import Decimal
from dataclasses import dataclass


DATABASE_PATH = "investimentos.db"


@dataclass
class Ativo:
    rowid: int
    nome: str
    num_cotas: int
    preco_unitario: Decimal
    tipo: str

@dataclass
class CustoTotal:
    tipo: str
    custo: Decimal

class SqliteConn:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_path)
        return self.conn

    def __exit__(self, *_):
        self.conn.close()

def get_all_ativos():
    with SqliteConn(DATABASE_PATH) as conn:
        query = """
        SELECT a.rowid, a.nome, a.num_cotas, a.preco_unitario, ta.tipo
        FROM ativos AS a
        JOIN tipos_ativos AS ta ON a.tipo = ta.rowid;
        """.strip()

        cur = conn.execute(query)

        ativos = [Ativo(*line) for line in cur]

    return ativos

def get_custo_por_tipo_de_ativo():
    with SqliteConn(DATABASE_PATH) as conn:
        query = """
        SELECT ta.tipo, SUM(a.num_cotas * a.preco_unitario)
        FROM ativos AS a
        JOIN tipos_ativos AS ta ON a.tipo = ta.rowid
        GROUP BY ta.tipo
        """.strip()

        cur = conn.execute(query)

        registros = [CustoTotal(*line) for line in cur]

    return registros

# ORM Object-Relational Mapper
