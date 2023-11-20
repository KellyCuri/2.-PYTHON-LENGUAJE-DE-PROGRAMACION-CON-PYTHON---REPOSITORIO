###
print("KELLY CURI LAURA")
import pandas as pd
from sqlalchemy import create_engine

################ Conectar a la base de datos MySQL########################

##engine = create_engine('mysql+mysqlconnector://usuario:contraseña@host/nombre_basededatos')
## query = 'SELECT * FROM nombre_tabla'

# Cargar datos desde la base de datos
datos = pd.read_sql(query,engine)

import pandas as pd

# Suponiendo que 'datos' es tu DataFrame
descripcion = datos.describe()
print(descripcion)

## NUEVO