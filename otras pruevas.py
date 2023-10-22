data = [{'Noche alucinante'}, {'720p\n480p\n360p\n240p\n144p'},
        {'Noche de Rock'}, {'720p\n480p\n360p\n240p\n144p'},
        {'TROTSKY VENGARÁN – No me digas que no [ Videoclip Oficial ] @trotskyvengaran'}, {'720p\n480p\n360p\n240p\n144p\n2160p\n1440p\n1080p'}]

# Crear una lista para almacenar el resultado formateado
formatted_data = []

# Recorrer la lista original de diccionarios
for i in range(0, len(data), 2):
    title = list(data[i])[0]
    resolutions = list(data[i + 1])[0].split('\n')
    
    formatted_data.append(f'Título: {title}')
    formatted_data.append('Resoluciones:')
    
    # Agregar cada resolución
    for resolution in resolutions:
        formatted_data.append(f'- {resolution}')

# Imprimir el resultado formateado
for item in formatted_data:
    print(item)
