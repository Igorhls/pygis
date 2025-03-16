from qgis.core import *
from qgis.utils import iface

# Inicializar o QGIS (se necessário, para rodar fora do ambiente QGIS)
QgsApplication.setPrefixPath("C:\Program Files\QGIS 3.40.4", True)
qgs = QgsApplication([], False)
qgs.initQgis()

# Enviar mensagem para o QGIS
iface.messageBar().pushMessage("Hello, World!", duration=3)

# Finalizar QGIS (caso não esteja rodando dentro dele)
qgs.exitQgis()
