from pymongo import MongoClient
import certifi

uri = "mongodb+srv://"
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(uri, tlsCAFile=ca)
        db = client["dbb_products_app"]
    except ConnectionError:
        print('Error en la conexion bd')
    return db 
