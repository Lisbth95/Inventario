from pymongo import MongoClient
import certifi

uri = "mongodb+srv://castrocatalan5991:Cacl953101@cluster0.4vlhs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
ca = certifi.where()

def dbConnection():
    try:
        client = MongoClient(uri, tlsCAFile=ca)
        db = client["dbb_products_app"]
    except ConnectionError:
        print('Error en la conexion bd')
    return db 