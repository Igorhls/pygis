import sys
import os

# Caminho para a instalação do QGIS
QGIS_PREFIX = r"C:\Program Files\QGIS 3.40.4"  # Ajuste conforme sua versão

# Adicionando caminhos do QGIS ao Python
sys.path.append(os.path.join(QGIS_PREFIX, "apps", "qgis", "python"))
sys.path.append(os.path.join(QGIS_PREFIX, "apps", "qgis", "bin"))
sys.path.append(os.path.join(QGIS_PREFIX, "apps", "Python39", "Scripts"))

# Importando PyQGIS
from qgis.core import *

# Testando a instalação
print("QGIS versão:", QgsApplication.qgisVersion())
