# projeto_fccpd_parte2

## Deaafio 4

### Objetivo

Nesse desafio o objetivo é conectar dois microservisos via um docker compose


### Como Rodar

utilize esses comandos na raiz projeto desafio4, ou seja, seu termina deve estar assim 

```
pasta\desafio4
```

1. Buildar o compose
Esse comando ira construir as imagens referencias no docker compose e a network que conecta ambos utilizando o build, e ja que possui um up ele tambem ira subir os conteiners desse docker compose

```bash

docker compose up --build

```

2. Observe se subiu corretamente e os logs

Utilize o comando para ver quais estão em execução 

```bash
docker ps 
```

Utilize ambos os comandos tanto para micro_serviceA quando o B

```bash
docker compose logs -f microservice_a
docker compose logs -f microservice_b

```

3. Visualização web

Utilize o esses comando para observar via um local host 

```
curl http://localhost:8000/   # chama microservice B
curl http://localhost:8001/   # chama microservice A (que por sua vez chama B internamente)

```



