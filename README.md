# Fathipy

**Fathipy** es un paquete en Python que implementa clases para representar y manipular vectores, partículas del modelo estándar y operaciones de rotación en 3D. Este paquete incluye funcionalidades para trabajar con `ThreeVector`, `Rotation` y `StandardModelParticle`, lo que lo hace útil para cálculos y simulaciones en física, especialmente en el contexto de la teoría de partículas.

### Link de descarga de la paquetería desde github
https://github.com/Fath1710/Fathipy_package.git

## Instalación

Puedes instalar este paquete utilizando `pip` desde un repositorio local, si has descargado el proyecto o si tienes el archivo comprimido. Si tienes el proyecto en tu máquina, solo necesitas correr el siguiente comando en la terminal desde el directorio raíz del proyecto:

```bash
pip install .
```

## Interfaz grafica

**Fathipy** cuenta con una interfaz grafica de presentacion de la paquetería, así como un uso sencillo de los módulos disponibles.
Para acceder a la interfaz, debes ejecutar el siguiente comando.
```bash
Fathipy_gui
```

## Modulos disponibles y uso

A continuación, se describen los módulos disponibles en **Fathipy** y cómo usarlos.

### Módulo `ThreeVector`

La clase `ThreeVector` representa un vector tridimensional, con métodos para realizar operaciones comunes como la suma, la resta, el producto punto, y el producto cruzado.

#### Ejemplo de uso:

```python
from Fathipy.three_vector import ThreeVector

# Crear un vector
v1 = ThreeVector(1, 2, 3)

# Crear otro vector
v2 = ThreeVector(4, 5, 6)

# Sumar vectores
v3 = v1 + v2
print(v3)  

# Producto cruzado
v4 = v1.cross(v2)
print(v4)  

# Producto punto
dot_product = v1.dot(v2)
print(dot_product)  
```

### Módulo `Rotation`

La clase `Rotation` permite realizar rotaciones en 3D utilizando el ángulo de rotación y el eje de rotación. Implementa la fórmula de Rodrigues para obtener la matriz de rotación.

#### Ejemplo de uso:

```python
from Fathipy.rotation import Rotation
from Fathipy.three_vector import ThreeVector
import numpy as np

# Crear un eje de rotación
axis = ThreeVector(0, 0, 1)  # Eje Z

# Crear una rotación de 90 grados (π/2 radianes) alrededor del eje Z
rotation = Rotation(np.pi / 2, axis)

# Crear un vector
v = ThreeVector(1, 0, 0)

# Aplicar la rotación
v_rotated = rotation.apply(v)
print(v_rotated)  
```

### Módulo `StandardModelParticle`

La clase `StandardModelParticle` representa una partícula del modelo estándar de física de partículas. Permite almacenar propiedades como el nombre, símbolo, masa, carga, espín, tipo de partícula y si es una antipartícula. También tiene un método `info()` que devuelve una descripción de la partícula.

#### Ejemplo de uso:

```python
from Fathipy.SMparticle import StandardModelParticle

# Crear una partícula
electron = StandardModelParticle(
    name="Electron",
    symbol="e-",
    mass=0.511,
    charge=-1,
    spin=0.5,
    type_of_particle="fermion"
)

# Obtener la descripción de la partícula
print(electron.info())
# Output: Electron (e-) - Masa: 0.511 MeV/c^2, Carga: -1, Espín: 0.5, Tipo: fermion, Antipartícula: False
```

## Pruebas

El paquete incluye pruebas unitarias para asegurarse de que todas las funcionalidades están implementadas correctamente. Para ejecutar las pruebas, puedes usar el siguiente comando:

```bash
python -m unittest discover -s tests
```

Las pruebas están diseñadas para verificar el comportamiento esperado de cada clase y método en el paquete, como la correcta inicialización de objetos, las operaciones de rotación y las descripciones de partículas.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
