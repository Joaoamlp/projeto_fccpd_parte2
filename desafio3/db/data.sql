CREATE TABLE pokemons (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    tipo VARCHAR(50)
);

INSERT INTO pokemons (nome, tipo) VALUES ('Bulbasaur', 'Planta/Venenoso');
INSERT INTO pokemons (nome, tipo) VALUES ('Charmander', 'Fogo');
INSERT INTO pokemons (nome, tipo) VALUES ('Squirtle', 'Água');
INSERT INTO pokemons (nome, tipo) VALUES ('Pikachu', 'Elétrico');
INSERT INTO pokemons (nome, tipo) VALUES ('Jigglypuff', 'Normal/Fada');
INSERT INTO pokemons (nome, tipo) VALUES ('Meowth', 'Normal');
INSERT INTO pokemons (nome, tipo) VALUES ('Psyduck', 'Água');
