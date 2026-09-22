# Prompt para Mejorar el Codigo Base

Copia y pega el siguiente contenido completo en un asistente de IA (Claude, ChatGPT, etc.)
para obtener un ZIP con el proyecto arrancable. Si el adjunto es una carcasa (docs/placeholders),
el asistente debe materializar la estructura del stack del briefing, sin resolver las fases del reto.

---

```
## Briefing del reto (autoridad)
Este bloque manda sobre los archivos adjuntos. El stack y el rol salen de AQUÍ, no de un topic genérico ni de markdown placeholder.

### Perfil
Chapter Cloud Ops, Especialidad Analista, Tecnología infraestructura en nube, Senior

### Brecha de conocimiento
Realiza actividades de administración de los servicios en nube entendiendo el ecosistema de funcionamiento y puede desarrollar scripts básicos para creación de la infraestructura y las actividades operativas requeridas.

### Misión / candidato
Candidato con experiencia en rol analista de infraestructura en nube

### Reto
- Tema: Administración básica de infraestructura
- Seniority: senior-l1
- Tipo: practical
- Título: Administración de Infraestructura en Nube
- Tiempo estimado: 4-6 horas

### Fases (trabajo del HUMANO — PROHIBIDO completarlas)
No implementes estos entregables. Dejalos como hueco pedagógico. El asistente solo materializa el proyecto arrancable para que el participante pueda trabajar.
- Fase 1: Exploración del Ecosistema de Nube — objetivo: Comprender el funcionamiento del ecosistema de nube y sus componentes. — entregable (NO resolver): Documento de investigación con los principales servicios y mejores prácticas.
- Fase 2: Creación de Infraestructura Básica — objetivo: Desarrollar scripts para la creación de infraestructura en nube. — entregable (NO resolver): Scripts para la creación de instancia de servidor y servicio de almacenamiento.
- Fase 3: Actividades Operativas Requeridas — objetivo: Desarrollar scripts para realizar actividades operativas comunes en la infraestructura en nube. — entregable (NO resolver): Scripts para actividades operativas y documentación del proceso.

Eres un asistente experto en análisis, corrección y generación de archivos de cualquier tipo:
código fuente, documentación, hojas de cálculo, documentos Word, configuraciones, entre otros.
Voy a enviarte una cadena de texto que contiene uno o más archivos. Cada archivo está delimitado por un marcador con el siguiente formato:
// === ARCHIVO: ruta/del/archivo.extension ===
o también puede aparecer como:
## === ARCHIVO: ruta/del/archivo.extension ===
Lo que sigue al marcador puede ser:

El contenido real del archivo (código, texto, YAML, etc.)
Una descripción en lenguaje natural de lo que debe contener el archivo


TU TAREA
PASO 1 — Detección y extracción
Identifica todos los archivos presentes en la cadena. Para cada archivo extrae:

Su ruta completa (ej: src/main/java/com/pragma/Service.java)
Su contenido o descripción

PASO 2 — Clasificación por tipo
Clasifica cada archivo en una de estas categorías:
A) Código fuente (Java, Python, TypeScript, JavaScript, Kotlin, etc.)
B) Configuración / documentación (YAML, properties, Markdown, JSON, txt, etc.)
C) Excel (.xlsx, .xls, .csv)
D) Word (.docx, .doc)
E) Otro tipo de archivo binario o especial
PASO 3 — Clasificación de errores en código fuente

Objetivo prioritario: que el proyecto compile. No corrijas flujo de negocio ni lógica funcional.

Antes de modificar cualquier archivo de código fuente, clasifica cada problema encontrado en una de estas dos categorías:
🔴 ERROR DE COMPILACIÓN — corregir siempre
Son errores que impiden que el proyecto arranque, sin valor pedagógico:

Import faltante o incorrecto
Clase, método o variable referenciada que no existe en ningún archivo del proyecto
Error de sintaxis
Anotación con atributos inválidos
Dependencia ausente en pom.xml, package.json, etc.
Archivo referenciado que no existe y debe ser creado con implementación mínima

→ CORREGIR estos errores.
🟡 PROBLEMA FUNCIONAL O DE CALIDAD — preservar siempre
Son problemas que no impiden compilar. Pueden ser intencionales para el aprendizaje:

Clave secreta hardcodeada ("secret", "password123")
API deprecada que funciona pero tiene reemplazo moderno
Lógica de negocio incorrecta o incompleta
Código redundante o de baja legibilidad
Falta de validaciones en flujo de negocio
Patrones de diseño incorrectos pero funcionales
Concurrencia no segura
Configuración funcional pero no óptima

→ PRESERVAR tal cual. No corregir, no mejorar, no comentar.
PASO 4 — Procesamiento según tipo de archivo
Tipo A — Código fuente
Aplica únicamente las correcciones clasificadas como 🔴 ERROR DE COMPILACIÓN.
No alteres ningún elemento clasificado como 🟡 PROBLEMA FUNCIONAL O DE CALIDAD.
Si falta un archivo referenciado, créalo con la implementación mínima necesaria para compilar.
Tipo B — Configuración / documentación
Extrae el contenido tal cual, sin modificaciones salvo errores evidentes de sintaxis
(ej: YAML mal indentado).
Tipo C — Excel (.xlsx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un archivo Excel funcional con:

Fila de encabezados en negrita con color de fondo distintivo
Columnas con ancho ajustado al contenido
Tipos de dato correctos por columna
Validaciones si la descripción lo indica
Hojas nombradas descriptivamente si hay más de una
Filas de ejemplo si no hay datos reales

Tipo D — Word (.docx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un documento Word funcional con:

Estilos de título (Título 1, Título 2) para jerarquía de secciones
Fuente legible (Calibri o equivalente), tamaño 11-12pt para cuerpo
Márgenes estándar
Tabla de contenido si tiene múltiples secciones
Tablas con encabezados en negrita si aplica

Tipo E — Otro
Genera el archivo con el contenido o estructura más apropiada según la descripción.
PASO 5 — Exportación en ZIP
Empaqueta todos los archivos en un único archivo ZIP descargable respetando exactamente
la estructura de rutas indicada por los marcadores.
El ZIP debe incluir:

Archivos de código con únicamente los errores de compilación corregidos
Archivos de configuración y documentación sin cambios
Archivos nuevos creados para resolver dependencias de compilación faltantes
Archivos Excel y Word generados desde descripción

IMPORTANTE: El ZIP debe estar listo para descargar al finalizar. No preguntes si el usuario
quiere generarlo. Simplemente genera el archivo y proporciona el enlace de descarga; No debes desplegar en el chat el resumen de lo que arreglaste al Zip, solo entregalo.

REGLAS IMPORTANTES

No omitas ningún archivo aunque no tenga errores ni modificaciones
Respeta los nombres y rutas exactas indicadas por los marcadores
Si un archivo no tiene marcador claro, infiere el nombre desde su contenido
Si la cadena contiene solo documentación o descripciones sin código, genera los archivos
correspondientes sin aplicar análisis de compilación
No agregues texto después del enlace de descarga del ZIP
No preguntes si el usuario quiere el ZIP: simplemente generalo siempre
Si detectas que falta un archivo de configuración necesario para compilar
(pom.xml, package.json, requirements.txt, build.gradle, etc.), créalo e inclúyelo
inferiendo su contenido desde los imports y frameworks detectados en el código
Nunca corrijas problemas 🟡 aunque parezcan obvios o fáciles de mejorar.
El participante que recibirá este proyecto los debe encontrar y resolver él mismo.


INPUT
Aquí está la cadena con los archivos:

import boto3
import yaml

# === ARCHIVO: docs/investigacion_servicios_nube.md ===
# Documento de investigación con los principales servicios y mejores prácticas en el ecosistema de nube.
# Este documento se completará en la fase 1.

# === ARCHIVO: scripts/provisionamiento_servidor.py ===
import boto3

def provisionar_servidor(config):
    ec2 = boto3.client('ec2')
    instance = ec2.run_instances(
        ImageId=config['image_id'],
        InstanceType=config['instance_type'],
        MinCount=1,
        MaxCount=1
    )
    print(f'Servidor provisionado: {instance['Instances'][0]['InstanceId']}')

# === ARCHIVO: scripts/provisionamiento_almacenamiento.py ===
import boto3

def provisionar_almacenamiento(config):
    s3 = boto3.client('s3')
    bucket_name = config['bucket_name']
    s3.create_bucket(Bucket=bucket_name)
    print(f'Bucket de almacenamiento creado: {bucket_name}')

# === ARCHIVO: scripts/escalado_recursos.py ===
import boto3

def escalar_recursos(config):
    ec2 = boto3.client('ec2')
    instances = ec2.describe_instances(InstanceIds=config['instance_ids'])['Reservations'][0]['Instances']
    for instance in instances:
        ec2.modify_instance_attribute(InstanceId=instance['InstanceId'], InstanceType={'Value': config['new_instance_type']})
    print('Recursos escalados.')

# === ARCHIVO: scripts/implementacion_actualizaciones.py ===
import boto3

def implementar_actualizaciones(config):
    # Placeholder para implementación de actualizaciones
    print('Actualizaciones implementadas.')

# === ARCHIVO: scripts/monitorizacion_rendimiento.py ===
import boto3

def monitorizar_rendimiento(config):
    # Placeholder para monitorización de rendimiento
    print('Rendimiento monitorizado.')

# === ARCHIVO: config/configuracion.yaml ===
image_id: 'ami-0abcdef1234567890'
instance_type: 't2.micro'
bucket_name: 'mi-bucket-de-almacenamiento'
instance_ids:
  - 'i-0123456789abcdef0'
new_instance_type: 't2.large'
```
