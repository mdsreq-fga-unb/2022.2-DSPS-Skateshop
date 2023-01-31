#### Como rodar o ambiente de desenvolvimento

###### Terminal 1

```
# construir e rodar o docker
docker-compose up --build
```

###### Terminal 2

```
# criar um terminal na imagem docker q está rodando
docker exec -it site bash

# aplicar migrações no banco de dados
python manage.py migrate

# criar super usuário (é necessário definir um nome de usuario, um email e uma senha nesta etapa)
python manage.py createsuperuser

# se quiser, pode fechar o terminal 2 e abrir o site em http://localhost:8000/
```
