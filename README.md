# Venta de herramientas

Aplicación desarrollada en Python utilizando MySQL y la biblioteca Tkinter. Permite a los usuarios registrarse, iniciar sesión, buscar herramientas disponibles, realizar compras y anular compras.

## Características

- **Inicio de sesión y registro de usuarios:** Los usuarios pueden registrarse y acceder al sistema.
- **Búsqueda de herramientas:** La aplicación permite buscar herramientas por nombre y muestra los resultados disponibles en una lista.
- **Compra de herramientas:** Los usuarios pueden seleccionar las herramientas que desean comprar, ingresar la cantidad y calcular el total de la compra.
- **Anulación de compras:** Existe la opción de anular compras realizadas previamente.

## Instalación y Configuración

#### 1. Clona el repositorio

```bash
git clone https://github.com/alonsoramoss/venta-herramientas.git
```

#### 2. Entra al directorio del proyecto

```bash
cd venta-herramientas
```

#### 2. Instala MySQL Connector

```bash
pip install mysql-connector-python
```

#### 3. Inicia Apache y MySQL en XAMPP

Abre el panel de control de XAMPP y activa los servicios de **Apache** y **MySQL**.

#### 4. Configura la base de datos

Crea una base de datos en MySQL llamada `ferreteria`.

- Ejecuta el siguiente script SQL para crear las tablas necesarias:

```sql
CREATE TABLE usuarios (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(50),
  apellido VARCHAR(50),
  dni VARCHAR(20),
  telefono VARCHAR(20),
  correo VARCHAR(50),
  password VARCHAR(100)
);

CREATE TABLE herramientas (
  id INT AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(50),
  precio DECIMAL(10,2)
);

CREATE TABLE venta (
  id INT AUTO_INCREMENT PRIMARY KEY,
  idUser INT,
  FOREIGN KEY (idUser) REFERENCES usuarios(id)
);

CREATE TABLE detalle_venta (
  id INT AUTO_INCREMENT PRIMARY KEY,
  venta_id INT,
  herramienta_id INT,
  cantidad INT,
  subtotal DECIMAL(10,2),
  FOREIGN KEY (venta_id) REFERENCES venta(id),
  FOREIGN KEY (herramienta_id) REFERENCES herramientas(id)
);
```

#### 5. Ejecuta la aplicación

```bash
py ventaherramientas.py
```
