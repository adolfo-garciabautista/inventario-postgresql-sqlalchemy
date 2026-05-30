# 📦 Sistema de Inventario con PostgreSQL y SQLAlchemy

Proyecto desarrollado en Python para la gestión de inventario utilizando PostgreSQL como base de datos y SQLAlchemy como ORM.

## 🚀 Tecnologías utilizadas

* Python 3
* PostgreSQL
* SQLAlchemy
* Git
* GitHub

---

## 📋 Funcionalidades

### Productos

* Agregar productos
* Listar productos
* Buscar productos por ID
* Buscar productos por nombre
* Actualizar stock
* Eliminar productos

### Reportes

* Productos sin stock
* Productos con bajo stock
* Total de productos registrados

---

## 🗄️ Base de datos

### Tabla: productos

| Campo  | Tipo    |
| ------ | ------- |
| id     | Integer |
| nombre | String  |
| precio | Integer |
| stock  | Integer |

### Tabla: proveedores

| Campo    | Tipo    |
| -------- | ------- |
| id       | Integer |
| nombre   | String  |
| telefono | String  |

### Tabla: movimientos_stock

| Campo       | Tipo    |
| ----------- | ------- |
| id          | Integer |
| producto_id | Integer |
| tipo        | String  |
| cantidad    | Integer |

---

## 🧠 Conceptos aplicados

* Programación orientada a funciones
* CRUD completo
* PostgreSQL
* SQLAlchemy ORM
* Foreign Keys
* Validaciones de datos
* Manejo de errores
* Reportes de inventario
* Persistencia de datos

---

## ▶️ Cómo ejecutar

### Instalar dependencias

```bash
pip install sqlalchemy
pip install psycopg2-binary
```

### Crear base de datos

```sql
CREATE DATABASE inventario;
```

### Ejecutar el proyecto

```bash
python Inventario.py
```

---

## 📚 Aprendizajes

Este proyecto fue desarrollado como práctica para consolidar conocimientos de:

* Python
* PostgreSQL
* SQLAlchemy
* Diseño de bases de datos
* CRUD
* Desarrollo Backend

---

## 👨‍💻 Autor

Adolfo Garcia Bautista

Proyecto realizado como parte de mi formación en Desarrollo Backend con Python.
