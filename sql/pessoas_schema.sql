CREATE TABLE cidades (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    cidade TEXT UNIQUE,
    uf VARCHAR(2)
);

CREATE TABLE pessoas (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    sobrenome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    idcidade INTEGER,
    dtcriacao DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (idcidade) REFERENCES cidades(id)
    
);