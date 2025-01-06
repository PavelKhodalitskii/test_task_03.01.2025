# Документация API

* [Авторизация](#Auth-endpoints)
* [Car endpoints](#Car-endpoints)
* [Comment endpoints](#Comment-endpoints)


<h2 id="Auth-endpoints">Авторизация</h2>

Эндпоинты, связанные с авторизацией

### Логин - /api/accounts/login/

**Требуется csrf_token**

Методы: GET, POST

#### POST:
    Request:
    {
        "username": "string",
        "password": "string"
    }

### Логаут - /api/accounts/logout/

**Требуется csrf_token**

Методы: POST

#### POST:
    {}

______________________________________________________________

<h2 id="Car-endpoints">Car endpoints</h2>

### Список авто: /api/cars/
**Требуется аутентификация (POST)**

#### GET
    Request:
    {}

    Response:
    {
        "id": 3,
        "make": {
        "id": 3,
        "name": "Honda"
        },
        "owner": {
        "id": 1,
        "first_name": "Павел",
        "last_name": "Ходалицкий"
        },
        "model": "Civic",
        "year": 2024,
        "description": "Надежный и экономичный седан, идеален для городской эксплуатации.",
        "created_at": "2025-01-05T16:21:53.377703Z",
        "updated_at": "2025-01-06T04:10:39.636939Z"
    }

#### POST
    Request:
    {
        "make": 0,
        "owner": 0,
        "model": "string",
        "year": 3000,
        "description": "string"
    }

    Response:
    {
        "id": 0,
        "make": 0,
        "owner": 0,
        "model": "string",
        "year": 3000,
        "description": "string",
        "created_at": "2025-01-06T04:39:31.179Z",
        "updated_at": "2025-01-06T04:39:31.179Z"
    }

### Подробная инфомация, редактирование, удаление /api/cars/{id}:
**Требуется Id автомобиля**
**Требуется аутентификация (PUT, PATCH, DELETE)**
**Редактировать может только владелец записи (PUT, PATCH, DELETE)**

Методы: GET, PUT, PATCH, DELETE

#### GET
    Request:
    {}

    Response:    
    {
        "id": 0,
        "make": {
            "id": 0,
            "name": "string"
        },
        "owner": {
            "id": 0,
            "first_name": "string",
            "last_name": "string"
        },
        "model": "string",
        "year": 3000,
        "description": "string",
        "created_at": "2025-01-06T04:43:32.351Z",
        "updated_at": "2025-01-06T04:43:32.351Z"
    }

#### PUT
    Request:
    {
        "make": 0,
        "owner": 0,
        "model": "string",
        "year": 3000,
        "description": "string"
    }

    Response:
    {
        "id": 0,
        "make": 0,
        "owner": 0,
        "model": "string",
        "year": 3000,
        "description": "string",
        "created_at": "2025-01-06T04:44:16.113Z",
        "updated_at": "2025-01-06T04:44:16.113Z"
    }

#### PATCH
    Request:
    {
        "make": 0,
        "owner": 0,
        "model": "string",
        "year": 3000,
        "description": "string"
    }

    Response:
    {
        "id": 0,
        "make": 0,
        "owner": 0,
        "model": "string",
        "year": 3000,
        "description": "string",
        "created_at": "2025-01-06T04:44:16.113Z",
        "updated_at": "2025-01-06T04:44:16.113Z"
    }

#### DELETE
    Request:
    {}

    Response:
    {}

_____________________________________________________________

<h2 id="Comment-endpoints">Comment endpoints</h2>

### Получить комментарий по id машины /api/cars/{id}/comments/
**Требуется Id автомобиля**
**Требуется аутентификация (POST)**

Методы GET, POST

#### GET
    Request:
    {}

    Response:
    [
        {
            "id": 0,
            "content": "string",
            "created_at": "2025-01-06T04:50:28.012Z",
            "car": 0,
            "author": 0,
            "parent": 0
        }
    ]

#### POST
    Request:
    {
        "content": "string",
        "car": 0,
        "author": 0,
        parent": 0
    }

    Response {
        "id": 0,
        "content": "string",
        "created_at": "2025-01-06T04:50:28.003Z",
        "car": 0,
        "author": 0,
        "parent": 0
    }