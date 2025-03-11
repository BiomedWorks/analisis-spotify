from LeerDatos import df_canciones

#Graficos
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff

# Seleccionamos las canciones más populares (Top 15)
canciones_populares = df_canciones.sort_values(by=['Popularidad'], ascending=False).head(15)

# Creamos una columna 'Canción_única' con la combinación de nombre de la canción y el álbum
canciones_populares['Canción_única'] = canciones_populares['Canción'] + '<br>' + canciones_populares['Álbum']

# Definimos los colores para las categorías 'Álbum' y 'Single'
color_dict = {'Álbum': '#1ED660', 'Single': 'white'}

# Creamos el gráfico de barras
fig = px.bar(canciones_populares,
             x='Canción_única',
             y='Popularidad',
             text='Popularidad',
             color='Tipo',
             color_discrete_map=color_dict,
             hover_data={'Álbum':True, 'Año':True, 'Artistas':True},
             title='Canciones más populares',
             template='plotly_dark')

# Ordenamos las categorías del eje X de acuerdo a la popularidad
fig.update_layout(title={'text': '<i>Canciones más populares</i>',
                         'y':0.9, 'x':0.5, 'xanchor': 'center', 'yanchor': 'top',
                         'font':dict(size=25, color='white')},
                  xaxis={'categoryorder': 'total descending', 'tickangle': 45},  # Rotamos las etiquetas del eje X para que se muestren mejor
                  yaxis={'categoryorder': 'total descending'})

# Establecemos el rango del eje Y, si es necesario
fig.update_yaxes(range=[0, canciones_populares['Popularidad'].max() + 3], showgrid=False, showticklabels=True)

# Ajustamos la posición y formato del texto en el gráfico
fig.update_traces(textposition='outside')

# Añadimos la imagen de Spotify al gráfico
fig.add_layout_image(dict(source="Resources/Logo_Spotify.png",
                          xref="paper", yref="paper", x=0.94, y=1.12,
                          sizex=0.17, sizey=0.17,
                          xanchor="center", yanchor="middle",
                          layer="above"))

# Mostrar el gráfico
fig.show()