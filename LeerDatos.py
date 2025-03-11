import pandas as pd
import numpy as np

#Graficos
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff

#machine learning regresion

from sklearn.model_selection import train_test_split #Separar los datos de entrenamiento y prueba
from sklearn.metrics import r2_score #
from sklearn.preprocessing import scale #Escalamiento de la informacion
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Lasso, Ridge  #Regresión lineal
from sklearn.svm import SVR  #Máquina de vectores de soporte
from sklearn.tree import DecisionTreeRegressor  #Árbol de decisiones
from sklearn.ensemble import RandomForestRegressor  #Bosques aleatorios


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Configura tus credenciales
client_id = "bb0a0e09d6c94aa7b737367978a6d801"
client_secret = "551eb9f17e9e4a9fa27458063b98e515"

# Autenticación con Client Credentials Flow
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

def encontrarID(artista):
    resultados = sp.search(q=artista, limit=1, type='artist')
    return resultados['artists']['items'][0]['id']

def obtenerData(artista_id): # 'album', 'single', 'appears_on', 'compilation'
    canciones_data = [] # Crear una lista vacía para almacenar los datos de las canciones

    albumes = sp.artist_albums(artista_id, album_type='album') # Obtener los álbumes del artista
    singles = sp.artist_albums(artista_id, album_type='single') # Obtener los singles del artista

    for album in albumes['items'] + singles['items']: # Obtener las canciones para cada álbum
        album_nombre = album['name']
        album_tipo = {'album':'Álbum', 'single':'Single'}[album['album_type']]
        album_año = album['release_date'].split('-')[0]  # Obtener el año de lanzamiento

        tracks = sp.album_tracks(album['id'])

        for track in tracks['items']: # Para cada canción, obtener los detalles y añadirlos a la lista de canciones
            cancion_nombre = track['name']
            cancion_artistas = ', '.join([t['name'] for t in track['artists']])
            cancion_duracion = '{:02d}:{:02d}'.format(*divmod(track['duration_ms'] // 1000, 60))
            cancion_popularidad = sp.track(track['id'])['popularity'] # Obtener la popularidad de la canción

            # Añadir los detalles de cadaa canción a la lista de canciones
            canciones_data.append([album_nombre, album_tipo, album_año, cancion_nombre, cancion_artistas, cancion_duracion, cancion_popularidad])

    return pd.DataFrame(canciones_data, columns=['Álbum', 'Tipo', 'Año', 'Canción', 'Artistas', 'Duración', 'Popularidad'])

tu_artista = 'Juanes'
id_artista = encontrarID(tu_artista)
print(f'ID de {tu_artista}: {id_artista}')

df = obtenerData(id_artista)
print(df)