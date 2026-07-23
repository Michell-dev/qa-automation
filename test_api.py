import requests

def test_obtener_usuario():
    respuesta = requests.get("https://jsonplaceholder.typicode.com/users/1")

    assert respuesta.status_code == 200

    datos = respuesta.json()
    assert datos ["id"] == 1
    assert datos ["name"] == "Leanne Graham"

def test_usuario_no_existe():
    respuesta = requests.get ("https://jsonplaceholder.typicode.com/users/999")

    assert respuesta.status_code == 404

def test_crear_post():
    nuevo_post = {
        "title": "Mi primer post",
        "body": "Contenido del psot",
        "userId": 1
    }

    respuesta = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=nuevo_post
    )

    assert respuesta.status_code == 201

    datos = respuesta.json()
    assert datos["title"] == "Mi primer post"
    assert datos["userId"] == 1
    assert "id" in datos


def test_crear_post_sin_titulo():
    nuevo_post = {
        "body": "Post sin titulo",
        "userId": 1
    
    }

    respuesta = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json=nuevo_post
    )

    assert respuesta.status_code == 201 

