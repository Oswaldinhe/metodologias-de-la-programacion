
# Portada

# Nombre del estudiante: ESCOBEDO CONTRERAS OMAR OSWALDO
# Matrícula (student ID): 2430238
# Grupo: 1-1 IM
# Materia: Introducción a la Programación con Python
# Tarea: CRUD en memoria con funciones (inventario simple)
# Fecha: 2025-12-05
# LINK DL REPO EN GITHUB: https://github.com/Oswaldinhe/metodologias-de-la-programacion


# Resumen ejecutivo

# Un CRUD es un conjunto de operaciones básicas sobre datos:
# Create (crear), Read (leer), Update (actualizar) y Delete (eliminar).
# En este programa se implementa un CRUD sencillo en memoria para
# manejar "items" de inventario usando Python. Se eligió una lista de
# diccionarios como estructura de datos, donde cada diccionario
# representa un producto con id, name, price y quantity. El uso de
# funciones separadas para cada operación ayuda a organizar la lógica,
# evita repetir código y facilita el mantenimiento. El programa incluye
# un menú de texto para que el usuario seleccione las operaciones,
# validación de entradas y casos de prueba documentados.
#

# Documentación del problema

# Problem: In-memory CRUD manager with functions
#
# Descripción:
# Programa que implementa un CRUD (Crear, Leer, Actualizar, Eliminar)
# simple para elementos almacenados en una lista de diccionarios,
# usando funciones para cada operación y un menú de texto para
# interactuar con el usuario.
#
# Decisión de estructura de datos:
# Se eligió la opción B: list de dicts. Cada dict tiene la forma:
# {"id": <string>, "name": <string>, "price": <float>, "quantity": <int>}.
# Esta opción es fácil de recorrer, imprimir y extender a futuro.
#
# Inputs:
# - User menu options (int).
# - Para CREATE/UPDATE: item_id, name, price, quantity.
# - Para READ/DELETE: item_id.
#
# Outputs:
# - Mensajes que indican el resultado de cada operación:
#   "Item created", "Item updated", "Item deleted",
#   "Item not found", "Error: invalid input", "Items list:", etc.
#
# Validations:
# - Menu option must be valid (0..5).
# - item_id must not be empty.
# - Numeric fields must be valid numbers and >= 0.
# - On CREATE: disallow creating an item with an id that already exists.
# - On READ/UPDATE/DELETE: if the id does not exist, show "Item not found".
#
# Test cases:
# 1) Normal:
#    - Create item: id="P1", name="Pen", price=10.0, quantity=100
#      -> "Item created"
#    - Read item "P1"
#      -> shows item data
#    - Update item "P1" to price=12.0, quantity=80
#      -> "Item updated"
#    - Delete item "P1"
#      -> "Item deleted"
#
# 2) Border:
#    - Create item with minimal valid data:
#      id="X", name="Empty", price=0.0, quantity=0
#      -> "Item created" and item appears in list
#
# 3) Error:
#    - Menu option = 9 or "abc"
#      -> "Error: invalid input"
#    - Create item with empty id
#      -> "Error: invalid input"
#    - Create item with price="xyz"
#      -> "Error: invalid input"
#    - Read/Update/Delete non-existing id
#      -> "Item not found"
#
# Diagrama de flujo (texto simplificado):
# 1) Inicializar la estructura de datos (lista de items vacía).
# 2) Entrar en un bucle while principal que muestre el menú.
# 3) Leer la opción del usuario y validarla.
# 4) Según la opción:
#    - Pedir los datos necesarios.
#    - Validar entradas.
#    - Llamar a la función correspondiente (create/read/update/delete/list).
#    - Mostrar mensajes de resultado.
# 5) Repetir hasta que el usuario elija la opción de salir (0).

# Funciones de apoyo para el CRUD
=

def find_item_index_by_id(items_list, item_id):
    """
    Find the index of an item in the list by its id.
    Parameters:
        items_list (list[dict]): list of items.
        item_id (str): id to search for.
    Returns:
        int: index of the item, or -1 if not found.
    """
    for index, item in enumerate(items_list):
        if item["id"] == item_id:
            return index
    return -1


def create_item(items_list, item_id, name, price, quantity):
    """
    Create a new item and add it to the list if the id does not exist.
    Parameters:
        items_list (list[dict]): current list of items.
        item_id (str): unique item id.
        name (str): item name.
        price (float): item price >= 0.
        quantity (int): item quantity >= 0.
    Returns:
        bool: True if created, False if id already exists.
    """
    index = find_item_index_by_id(items_list, item_id)
    if index != -1:
        return False  # id already exists
    new_item = {
        "id": item_id,
        "name": name,
        "price": price,
        "quantity": quantity
    }
    items_list.append(new_item)
    return True


def read_item(items_list, item_id):
    """
    Read (retrieve) an item by its id.
    Parameters:
        items_list (list[dict]): current list of items.
        item_id (str): id to search for.
    Returns:
        dict or None: item dict if found, otherwise None.
    """
    index = find_item_index_by_id(items_list, item_id)
    if index == -1:
        return None
    return items_list[index]


def update_item(items_list, item_id, new_name, new_price, new_quantity):
    """
    Update an existing item identified by its id.
    Parameters:
        items_list (list[dict]): current list of items.
        item_id (str): id to search for.
        new_name (str): new name.
        new_price (float): new price >= 0.
        new_quantity (int): new quantity >= 0.
    Returns:
        bool: True if updated, False if item not found.
    """
    index = find_item_index_by_id(items_list, item_id)
    if index == -1:
        return False
    items_list[index]["name"] = new_name
    items_list[index]["price"] = new_price
    items_list[index]["quantity"] = new_quantity
    return True


def delete_item(items_list, item_id):
    """
    Delete an item identified by its id.
    Parameters:
        items_list (list[dict]): current list of items.
        item_id (str): id to search for.
    Returns:
        bool: True if deleted, False if item not found.
    """
    index = find_item_index_by_id(items_list, item_id)
    if index == -1:
        return False
    items_list.pop(index)
    return True


def list_items(items_list):
    """
    Return a copy of the items list (for printing or further processing).
    Parameters:
        items_list (list[dict]): current list of items.
    Returns:
        list[dict]: shallow copy of items_list.
    """
    return list(items_list)

# Código principal (menú CRUD)


EXIT_OPTION = 0


def print_menu():
    """
    Print the main menu options.
    """
    print("\nMenu:")
    print("1) Create item")
    print("2) Read item by id")
    print("3) Update item by id")
    print("4) Delete item by id")
    print("5) List all items")
    print("0) Exit")


def main():
    """
    Main loop for the in-memory CRUD manager.
    """
    items_data = []  # list of dicts representing items

    while True:
        print_menu()
        option_text = input("Option: ")

        # Validar opción de menú
        try:
            option = int(option_text)
        except ValueError:
            print("Error: invalid input")
            continue

        if option == EXIT_OPTION:
            print("Exiting CRUD manager. Bye!")
            break

        if option < 0 or option > 5:
            print("Error: invalid input")
            continue

        # CREATE
        if option == 1:
            item_id = input("Enter item id: ")
            name = input("Enter item name: ")
            price_text = input("Enter item price: ")
            quantity_text = input("Enter item quantity: ")

            # Validación de entradas
            if item_id.strip() == "" or name.strip() == "":
                print("Error: invalid input")
                continue

            try:
                price = float(price_text)
                quantity = int(quantity_text)
            except ValueError:
                print("Error: invalid input")
                continue

            if price < 0.0 or quantity < 0:
                print("Error: invalid input")
                continue

            created = create_item(items_data, item_id.strip(), name.strip(), price, quantity)
            if created:
                print("Item created")
            else:
                print("Error: item id already exists")

        # READ
        elif option == 2:
            item_id = input("Enter item id to read: ")
            if item_id.strip() == "":
                print("Error: invalid input")
                continue

            item = read_item(items_data, item_id.strip())
            if item is None:
                print("Item not found")
            else:
                print("Item found:")
                print(f"  id: {item['id']}")
                print(f"  name: {item['name']}")
                print(f"  price: {item['price']}")
                print(f"  quantity: {item['quantity']}")

        # UPDATE
        elif option == 3:
            item_id = input("Enter item id to update: ")
            if item_id.strip() == "":
                print("Error: invalid input")
                continue

            existing_item = read_item(items_data, item_id.strip())
            if existing_item is None:
                print("Item not found")
                continue

            print("Leave field empty to keep current value.")
            new_name = input(f"Enter new name (current: {existing_item['name']}): ")
            new_price_text = input(f"Enter new price (current: {existing_item['price']}): ")
            new_quantity_text = input(f"Enter new quantity (current: {existing_item['quantity']}): ")

            # Mantener valores actuales si se deja vacío
            if new_name.strip() == "":
                new_name_final = existing_item["name"]
            else:
                new_name_final = new_name.strip()

            # Validar y asignar números
            if new_price_text.strip() == "":
                new_price_final = existing_item["price"]
            else:
                try:
                    new_price_final = float(new_price_text)
                except ValueError:
                    print("Error: invalid input")
                    continue
                if new_price_final < 0.0:
                    print("Error: invalid input")
                    continue

            if new_quantity_text.strip() == "":
                new_quantity_final = existing_item["quantity"]
            else:
                try:
                    new_quantity_final = int(new_quantity_text)
                except ValueError:
                    print("Error: invalid input")
                    continue
                if new_quantity_final < 0:
                    print("Error: invalid input")
                    continue

            updated = update_item(
                items_data,
                item_id.strip(),
                new_name_final,
                new_price_final,
                new_quantity_final
            )
            if updated:
                print("Item updated")
            else:
                # Teóricamente no debería ocurrir porque ya verificamos
                print("Item not found")

        # DELETE
        elif option == 4:
            item_id = input("Enter item id to delete: ")
            if item_id.strip() == "":
                print("Error: invalid input")
                continue

            deleted = delete_item(items_data, item_id.strip())
            if deleted:
                print("Item deleted")
            else:
                print("Item not found")

        # LIST
        elif option == 5:
            all_items = list_items(items_data)
            if not all_items:
                print("Items list: (empty)")
            else:
                print("Items list:")
                for item in all_items:
                    print(
                        f"- id: {item['id']}, "
                        f"name: {item['name']}, "
                        f"price: {item['price']}, "
                        f"quantity: {item['quantity']}"
                    )


if __name__ == "__main__":
    main()



# Conclusiones

# El uso de funciones separadas para cada operación (create, read,
# update, delete y list) simplificó la implementación del CRUD, ya que
# el menú principal sólo se encarga de la interacción con el usuario y
# delega la lógica de negocio. La estructura de lista de diccionarios
# resultó flexible para almacenar y recorrer los items, permitiendo
# ampliar fácilmente los campos en el futuro. La validación de entradas
# fue clave para evitar errores por ids vacíos u opciones de menú
# inválidas; manejar estos casos con mensajes claros mejora la
# experiencia del usuario. Este CRUD podría extenderse para guardar
# datos en archivos o bases de datos, reutilizando las mismas funciones
# y cambiando únicamente la capa de persistencia.

# Referencias

# References:
# 1) Python Software Foundation. "Data Structures — list, dict".
#    Python Documentation, https://docs.python.org/
# 2) Python Software Foundation. "Defining Functions".
#    Python Documentation, https://docs.python.org/
# 3) Tutoriales introductorios de Python sobre CRUD en memoria y
#    manejo de listas y diccionarios (por ejemplo, W3Schools,
#    Real Python y apuntes de clase).
