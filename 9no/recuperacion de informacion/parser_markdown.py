import re
import html
import requests 

def parsear_markdown(texto):
    elementos = []
    en_codigo = False
    codigo = []
    lenguaje = ""

    for linea in texto.splitlines():
        if linea.startswith("```"):
            if not en_codigo:
                en_codigo = True
                lenguaje = linea[3:].strip()
                codigo = []
            else:
                en_codigo = False
                elementos.append({"tipo": "codigo", "lenguaje": lenguaje, "contenido": "\n".join(codigo)})
            continue

        if en_codigo:
            codigo.append(linea)
            continue

        # Reconocer encabezados H1, H2, H3
        if linea.startswith("### "):
            elementos.append({"tipo": "encabezado", "nivel": 3, "contenido": linea[4:]})
        elif linea.startswith("## "):
            elementos.append({"tipo": "encabezado", "nivel": 2, "contenido": linea[3:]})
        elif linea.startswith("# "):
            elementos.append({"tipo": "encabezado", "nivel": 1, "contenido": linea[2:]})
        # Reconocer listas no ordenadas
        elif linea.startswith("- "):
            elementos.append({"tipo": "item", "contenido": linea[2:]})
        # Reconocer párrafos (descartar líneas vacías)
        elif linea.strip():
            elementos.append({"tipo": "parrafo", "contenido": linea})

    return elementos

def procesar_inline(texto):
    # Negritas y cursivas
    texto = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', texto)
    texto = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<em>\1</em>', texto)
    # Enlaces
    texto = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', texto)
    return texto

def convertir_html(elementos):
    salida = []
    lista_abierta = False
    
    for e in elementos:
        if e["tipo"] != "item" and lista_abierta:
            salida.append("</ul>")
            lista_abierta = False

        if e["tipo"] == "encabezado":
            n = e["nivel"]
            contenido = procesar_inline(html.escape(e['contenido']))
            salida.append(f"<h{n}>{contenido}</h{n}>")
        elif e["tipo"] == "parrafo":
            contenido = procesar_inline(html.escape(e['contenido']))
            salida.append(f"<p>{contenido}</p>")
        elif e["tipo"] == "item":
            if not lista_abierta:
                salida.append("<ul>")
                lista_abierta = True
            contenido = procesar_inline(html.escape(e['contenido']))
            salida.append(f"<li>{contenido}</li>")
        elif e["tipo"] == "codigo":
            salida.append("<pre><code>" + html.escape(e["contenido"]) + "</code></pre>")

    if lista_abierta:
        salida.append("</ul>")

    return "\n".join(salida)

# --- Ejecución principal ---
try:
    # Solicitar al usuario el origen del archivo
    origen = input("Introduce la URL de GitHub (raw) o la ruta del archivo local .md: ").strip()
    texto = ""

    # Determinar si es una URL o un archivo local
    if origen.startswith("http://") or origen.startswith("https://"):
        print("Descargando archivo desde la Web...")
        respuesta = requests.get(origen)
        if respuesta.status_code == 200: # Verifica que la petición fue exitosa
            texto = respuesta.text
        else:
            print(f"Error al descargar: Código de estado {respuesta.status_code}")
            exit()
    else:
        with open(origen, "r", encoding="utf-8") as archivo:
            texto = archivo.read()

    # Procesamiento del documento
    resultado = parsear_markdown(texto)
    html_resultado = convertir_html(resultado)

    # Guardar el resultado HTML
    with open("resultado.html", "w", encoding="utf-8") as archivo:
        archivo.write(html_resultado)
    print("Archivo 'resultado.html' generado exitosamente.\n")

    # Contar elementos para el resumen
    conteos = {"h1": 0, "h2": 0, "h3": 0, "parrafos": 0, "items": 0, "codigo": 0}
    
    for e in resultado:
        if e["tipo"] == "encabezado":
            conteos[f"h{e['nivel']}"] += 1
        elif e["tipo"] == "parrafo":
            conteos["parrafos"] += 1
        elif e["tipo"] == "item":
            conteos["items"] += 1
        elif e["tipo"] == "codigo":
            conteos["codigo"] += 1

    # Contar enlaces usando la expresión regular sobre el texto original
    enlaces = len(re.findall(r'\[([^\]]+)\]\(([^)]+)\)', texto))

    # Mostrar resumen
    print("RESUMEN DEL DOCUMENTO")
    print(f"Encabezados H1: {conteos['h1']}")
    print(f"Encabezados H2: {conteos['h2']}")
    print(f"Encabezados H3: {conteos['h3']}")
    print(f"Párrafos: {conteos['parrafos']}")
    print(f"Elementos de lista: {conteos['items']}")
    print(f"Enlaces: {enlaces}")
    print(f"Bloques de código: {conteos['codigo']}")

except FileNotFoundError:
    print(f"Error: No se encontró el archivo local '{origen}'.")
except requests.exceptions.RequestException as e:
    print(f"Ocurrió un error de conexión al intentar acceder a la URL: {e}")