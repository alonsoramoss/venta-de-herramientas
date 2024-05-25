# Sistema de Gestión de Boletas y Usuarios con Tkinter y MySQL

Aplicación desarrollada en Python utilizando la biblioteca Tkinter y MySQL. Permite a los usuarios registrarse, iniciar sesión, buscar herramientas, calcular subtotales y totales de una compra. 

### Características:
- **Inicio de Sesión y Registro de Usuarios:** Permite a los usuarios registrarse y acceder al sistema.
- **Búsqueda y Selección de Herramientas:** Los usuarios pueden buscar herramientas disponibles y seleccionar las cantidades deseadas.
- **Cálculo de Subtotales y Totales:** Calcula automáticamente los subtotales y totales de la compra.
- **Almacenamiento en MySQL:** Todos los datos se almacenan en una base de datos MySQL llamada *ferreteria*.

### Configuración:
1. **Clonar el repositorio:**

2. **Instalar MySQL Connector:**
*pip install mysql-connector-python*

3. **Configurar la Base de Datos:**
- Crear una base de datos en MySQL llamada `ferreteria`.
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

4. **Ejecutar la Aplicación**
