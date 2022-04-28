-- ativos
-- tipos_ativos

CREATE TABLE IF NOT EXISTS tipos_ativos (
    tipo TEXT
);

CREATE TABLE IF NOT EXISTS ativos (
    nome TEXT,
    num_cotas INTEGER,
    preco_unitario REAL,
    tipo INTEGER,
    FOREIGN KEY(tipo) REFERENCES tipos_ativos(rowid)
);

INSERT INTO tipos_ativos VALUES
("ação"), -- id 1
("fii");  -- id 2

INSERT INTO ativos VALUES
("XPTO12", 500, 5.70, 1),
("XPTO10", 300, 5.90, 1),
("TAPA20", 100, 4.20, 2);
