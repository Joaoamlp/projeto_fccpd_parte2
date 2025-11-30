# projeto_fccpd_parte2

## Desafio 3

### Objetivo

Nesse desafio o objetivo é utilizar docker compose para construir multiplos serviços de uma vez

### Ferramentas utilizadas

- Docker
- flask
- posterqSQL
- redis

### Como rodar

Lembre-se de estar no diretorio do desafio 3 seu cmd deve estar desse jeito

```
..\desafio3
```

1. Como rodar 

Esse comando ira construir as imagens referenciadas no docker compose e a network que conecta ambos utilizando o build, e ja que possui um up ele tambem ira executar os conteiners desse docker compose.

```
docker compose up --build
```

2. Funcionamento via local host

Utilize o comando do curl para utilizar o localhost.
```
curl http://localhost:8000
```

Caso queira ver os logs utilize o comando

```
docker compose logs -f app_desafio3
```


---

## Desafio 4

### Objetivo

Nesse desafio o objetivo é conectar dois microservisos via um docker compose

### Ferramentas utilizadas 

-Docker
-flask


### Como Rodar

Lembre-se de estar no diretorio do desafio 3 seu cmd deve estar desse jeito

```
..\desafio3
```

1. Buildar o compose

Esse comando ira construir as imagens referenciadas no docker compose e executar os conteiners em uma linha

``` bash

docker compose up --build

```

2. Observe se subiu corretamente e os logs

Utilize o comando para ver quais estão em execução 

``` bash
docker ps 
```

Utilize ambos os comandos tanto para micro_serviceA quando o B

``` bash
docker compose logs -f microservice_a
docker compose logs -f microservice_b

```

3. Visualização web

Utilize o esses comando para observar via um local host 

```
curl http://localhost:8000/   # chama microservice B
curl http://localhost:8001/   # chama microservice A (que por sua vez chama B internamente)

```

---

## desafio5

### Objetivo

Utilizar um api gateway para controlar as requisições de dois microservisos. 

### Ferramentas

- Docker
- flask
- nginx

### Como Rodar 

Lembre-se de estar no diretorio do desafio 5 seu cmd deve estar desse jeito

```
..\desafio5
```
1.Buildar o compose e executar os conteiners

Utilize esse comando para buildar as imagens e subir os conteiners 

``` bash
docker compose up --build
```

## Testando o Gateway

Utilize o esses comandos para testar o gateway

```
curl http://localhost:8080/users
curl http://localhost:8080/orders
```

Se observarmos as portas dos serviços não estão expostas o que conclui que o gateway esta funcionando como deveria







