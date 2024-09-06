# Proyecto de Aplicación de Viajes Compartidos

## Descripción
Este proyecto implementa una aplicación de viajes compartidos utilizando servicios de AWS. Incluye un diagrama de arquitectura generado con Python y la librería Diagrams.

## Estructura del Proyecto
ProyectoViajes/
│
├── src/
│ └── diagrama_arquitectura.py
│
├── docs/
│ └── diagrama_arquitectura.png
│
└── README.md

## Requisitos
- Python 3.9+
- pip3
- Graphviz
- Librería Diagrams

## Instalación

1. Instala Graphviz:
   ```
   brew install graphviz
   ```

2. Instala la librería Diagrams:
   ```
   pip3 install diagrams
   ```

## Uso

Para generar el diagrama de arquitectura:

1. Navega al directorio del proyecto.
2. Ejecuta:
   ```
   python3 src/diagrama_arquitectura.py
   ```
3. El diagrama se generará como `diagrama_arquitectura.png` en la carpeta `docs/`.

## Documentación Adicional

### Prompts Utilizados

1. Creación del diagrama de arquitectura:
   ```
   Ahora ayúdame a crear el diagrama de arquitectura utilizando la librería Diagram y Python para pintarla suponiendo que uso AWS
   ```

### Componentes del Diagrama de Arquitectura

El diagrama incluye los siguientes componentes de AWS:

1. API Gateway: Para manejar las solicitudes de usuarios y conductores.
2. Cognito: Para la autenticación de usuarios.
3. ECS (Elastic Container Service): Para el servicio principal de la API.
4. Lambda: Para funciones serverless (búsqueda de conductores, notificaciones, procesamiento de pagos).
5. RDS: Para la base de datos relacional.
6. SQS: Como cola de mensajes para solicitudes de viajes.
7. S3: Para almacenamiento de datos (perfiles de usuario, registros, etc.).

## Contribución
Si deseas contribuir a este proyecto, por favor crea un fork del repositorio y envía un pull request con tus cambios.

## Licencia
[Incluir información de licencia aquí]