from sqlalchemy import (
    create_engine, Column, Integer, String, Date, ForeignKey
)

from sqlalchemy.orm import (sessionmaker, declarative_base)

engine = create_engine(
    "postgresql://postgres:1234@localhost/Inventario"
)

Base = declarative_base()

class Productos(Base):

    __tablename__ = "productos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    precio = Column(Integer)
    stock = Column(Integer)

class Proveedores(Base):

    __tablename__ = "proveedores"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    telefono = Column(String)

class Movimientos_Stock(Base):

    __tablename__ = "movimientos_stock"

    id = Column(Integer, primary_key=True)
    producto_id = Column(Integer, ForeignKey("productos.id"))
    tipo = Column(String)
    cantidad = Column(Integer)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

def obtener_producto_por_id():

    while True:
        try:
            buscar_id = int(input("Ingrese el ID del producto: "))
            break

        except ValueError:
            print("Error: Ingrese solo numeros")

    producto = session.query(Productos).filter_by(id=buscar_id).first()
    return producto

def agregar_producto():

    producto_nuevo = input("Ingrese el nombre del producto: ").strip().title()

    while True:
        try: 
            precio = int(input("Ingrese el precio: "))
            stock = int(input("Ingrese el stock: "))
            break

        except ValueError:
            print("Error: Ingrese solo numeros")

    producto = Productos(
        nombre = producto_nuevo,
        precio = precio,
        stock = stock
    )

    session.add(producto)
    session.commit()
    print("Producto agregado con exito!")

def listas_productos():

    productos = session.query(Productos).all()

    for p in productos:
        print(
            f"ID:{p.id} | Nombre:{p.nombre} | Precio:{p.precio} | Stock: {p.stock}"
            )

def actualizar_stock():
    
    producto = obtener_producto_por_id()

    if producto:
        while True:
            try:
                stock_nuevo = int(input("Ingrese el stock: "))
                break
            except ValueError:
                print("Error: Ingrese solo numeros")

        producto.stock = stock_nuevo
        session.commit()

        print("Stock actualizado con exito!")
    
    else:
        print("No existe producto con ese ID")

def eliminar_producto():

    producto = obtener_producto_por_id()

    if producto:
        session.delete(producto)
        session.commit()
        print("Eliminado con exito!")

    else:
        print("No existe el producto con ese ID")
    
def buscar_producto():

    while True:
        opcion = input("Desea buscar el producto por 'ID' o 'Nombre': ").strip().lower()

        if opcion == "id":

            while True:
                try:
                    buscar_id = int(input("Ingrese el ID del producto: "))
                    break

                except ValueError:
                    print("Error: Ingrese solo numeros")

            producto = session.query(Productos).filter_by(id=buscar_id).first()

            if producto:

                print(producto.nombre)
                break

            else:

                print("No existe producto con ese ID")

                break

        if opcion == "nombre":

            nombre_producto = input("Ingrese el nombre del producto: ").strip().title()

            producto = session.query(Productos).filter_by(nombre=nombre_producto).first()

            if producto:
                print(
                    f"ID:{producto.id} | Nombre:{producto.nombre} | "
                    f"Precio:{producto.precio} | Stock:{producto.stock}"
                )

            else:
                print(f"No se encontro el producto con el nombre: {nombre_producto}")
            
            break

        print("Error: Ingrese una opcion valida (ID/Nombre)")

def reportes():

    print("\nProductos sin stock:\n")

    productos_sin_stock = session.query(Productos).filter_by(stock=0).all()
    
    if productos_sin_stock:
        
        for pr in productos_sin_stock:
            print(
                f"ID:{pr.id} | "
                f"Nombre:{pr.nombre} | "
                f"Stock:{pr.stock}"
)

    else:
        print("No hay productos sin stock")

    print("\nProductos con bajo stock:\n")

    productos_bajo_stock = session.query(Productos).filter(Productos.stock < 5,
        Productos.stock > 0).all()

    if productos_bajo_stock:

        for pr in productos_bajo_stock:
            print(
                f"ID:{pr.id} | "
                f"Nombre:{pr.nombre} | "
                f"Stock:{pr.stock}"
)

    total_pr = session.query(Productos).count()

    print(f"Total de productos: {total_pr} productos.")

def mostrar_menu():

    print("1. Agregar producto")
    print("2. Ver productos")
    print("3. Actualizar stock")
    print("4. Eliminar producto")
    print("5. Buscar producto")
    print("6. Reportes")
    print("7. Salir")

def escoger_opcion():

    while True:
        try:
            opcion = int(input("Ingrese la opcion (1-7): "))
            if opcion > 0 and opcion < 8:
                return opcion
            print("Ingrese una opcion dentro del rango (1-7)")

        except ValueError:
            print("Error: Ingrese solo numeros")

def mensaje_despedida():
    print("Gracias por usar el menu de opciones!") 

def main():

    try:

        while True:

            mostrar_menu()
            opcion = escoger_opcion()

            if opcion == 1:
                agregar_producto()

            elif opcion == 2:
                listas_productos()

            elif opcion == 3:
                actualizar_stock()

            elif opcion == 4:
                eliminar_producto()

            elif opcion == 5:
                buscar_producto()
            
            elif opcion == 6:
                reportes()

            elif opcion == 7:
                break

        mensaje_despedida()

    except Exception as e:
        print(f"Ocurrio un error: {e}")

    finally:

        session.close()
        print("<---Conexion con el servidor terminada--->")

main()






