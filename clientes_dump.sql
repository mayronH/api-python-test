BEGIN TRANSACTION;
CREATE TABLE clientes (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    cpf VARCHAR(11) NOT NULL,
    email TEXT NOT NULL,
    fone TEXT,
    cidade TEXT,
    uf VARCHAR(2) NOT NULL,
    dtcriacao DATE NOT NULL
, ativo BOOLEAN);
INSERT INTO "clientes" VALUES(1,'Carlos',23,'00123456789','teste@teste.com.br','31998980101','Timóteo','MG','2020-05-31',NULL);
INSERT INTO "clientes" VALUES(2,'Teste2',18,'98765432100','teste2@teste.com.br','31998980101','Coronel Fabriciano','MG','2020-06-01',NULL);
INSERT INTO "clientes" VALUES(3,'Teste3',17,'12345678900','teste3@teste.com.br','31998980101','Ipatinga','MG','2020-06-02',NULL);
INSERT INTO "clientes" VALUES(4,'Teste4',25,'11122233344','teste4@teste.com.br','31998980101','Timóteo','MG','2020-06-03',NULL);
INSERT INTO "clientes" VALUES(5,'Mateus',20,'11122233389','mateus@teste.com.br','31955554444','Timóteo','MG','2020-05-30',NULL);
INSERT INTO "clientes" VALUES(6,'Ana',18,'15155544478','ana@teste.com.br','31955554489','Coronel Fabriciano','MG','2020-05-29',NULL);
INSERT INTO "clientes" VALUES(7,'Luiza',25,'22233355566','luiza@teste.com.br','31944554489','Ipatinga','MG','2020-06-02',NULL);
INSERT INTO "clientes" VALUES(8,'Pedro',30,'11188899900','pedro@teste.com.br','31944558889','São Paulo','SP','2020-06-02',NULL);
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('clientes',8);
COMMIT;
