import os
import sys

# Agrega la ruta de Graphviz al PATH
os.environ["PATH"] += os.pathsep + '/usr/local/bin'
# Imprime el PATH para verificar
print(os.environ["PATH"])
# Imprime la versión de Python
print(sys.version)

from diagrams import Diagram, Cluster
from diagrams.aws.compute import ECS, Lambda
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.aws.mobile import APIGateway
from diagrams.aws.security import Cognito
from diagrams.aws.integration import SQS
from diagrams.aws.storage import S3

with Diagram("Arquitectura de Aplicación de Viajes Compartidos", show=False, filename="diagrama_arquitectura"):
    # Usuarios y conductores
    usuarios = APIGateway("API Gateway")
    auth = Cognito("Autenticación")

    with Cluster("Servicios de Aplicación"):
        api = ECS("Servicio API")
        busqueda = Lambda("Búsqueda de Conductores")
        notificaciones = Lambda("Notificaciones")

    # Base de datos
    db = RDS("Base de Datos")

    # Cola de mensajes
    cola = SQS("Cola de Solicitudes")

    # Almacenamiento
    s3 = S3("Almacenamiento")

    # Sistema de pago
    pago = Lambda("Procesamiento de Pago")

    # Flujo principal
    usuarios >> auth >> api
    api >> busqueda
    busqueda >> cola
    cola >> api
    api >> db
    api >> notificaciones
    api >> pago
    api >> s3
