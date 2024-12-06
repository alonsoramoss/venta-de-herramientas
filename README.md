# Sistema de Venta de Herramientas con Tkinter y MySQL

Aplicación desarrollada en Python utilizando la biblioteca Tkinter y MySQL. Permite a los usuarios registrarse, iniciar sesión, buscar herramientas disponibles, realizar compras y anular compras.

## Características
- **Inicio de Sesión y Registro de Usuarios:** Los usuarios pueden registrarse y acceder al sistema.
- **Búsqueda de Herramientas:** La aplicación permite buscar herramientas por nombre y muestra los resultados disponibles en una lista.
- **Compra de Herramientas:** Los usuarios pueden seleccionar las herramientas que desean comprar, ingresar la cantidad y calcular el total de la compra.
- **Anulación de Compras:** Existe la opción de anular compras realizadas previamente.

## Pasos para utilizar la aplicación
#### 1. Clonar el repositorio

#### 2. Instalar MySQL Connector
    pip install mysql-connector-python

#### 3. Configurar la Base de Datos
Crear una base de datos en MySQL llamada `ferreteria`.
- Ejecutar el siguiente script SQL para crear las tablas necesarias:
  
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

#### 4. Ejecutar la Aplicación
