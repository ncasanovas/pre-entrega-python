# Sistema de gestión básica de productos

# 1. Agregar producto
# 2. Mostrar productos
# 3. Buscar producto
# 4. Eliminar producto
# 5. Salir

productos = [['Mochila', 'Accesorios', 10000], ['Cartuchera', 'Útiles', 300], ['Regla', 'Útiles', 100]]
menu_opciones = ("Agregar producto", "Mostrar productos", "Buscar producto", "Eliminar producto", "Salir")
salir = False
opcion_elegida = 0

while not salir:
  print()
  
  print("="*40)
  print(f"{"-"*15} Productos {"-"*15}")
  print("="*40)

  for i in range(len(menu_opciones)):
    print(f"{i+1}. {menu_opciones[i]}")
  opcion_elegida = input('Elegí la opción: ').strip()

  print()
  match opcion_elegida:  
    case "1":
      cantidad = input("Ingresa cuántos productos desea agregar: ")
      while not cantidad.isdigit():
        print("Error. La cantidad debe ser un número. ")
        cantidad = input("Ingresa cuántos productos desea agregar: ")

      cantidad_int = int(cantidad)
      if cantidad_int > 0:
        for i in range(cantidad_int):
          print()
          nombre = input("Nombre del producto: ").strip()
          while nombre == "":
            print("Error. El nombre del producto no puede estar vacío. ")
            nombre = input("Nombre del producto: ").strip()
          

          categoria = input("Categoría del producto: ").strip()
          while categoria == "":
            print("Error. La categoría del producto no puede estar vacía. ")
            categoria = input("Categoría del producto: ").strip()
          

          precio_str = input("Precio del producto (sin centavos): ").strip()
          while not precio_str.isdigit():
            print("Error. El precio debe ser un número positivo. ")
            precio_str = input("Precio del producto (sin centavos): ").strip()
          precio = int(precio_str)
          
          productos.append([nombre, categoria, precio])  
        print()         
        print(f"{"-"*6} Lista de productos actualizada {"-"*6}")
        print()           
        for i in range(len(productos)):
          print(f"{i+1} - Nombre: {productos[i][0]}\n    Categoría: {productos[i][1]}\n    Precio: ${productos[i][2]}")
      else:
        print("La cantidad debe ser mayor a cero.")
      
    case "2":
      if len(productos) != 0:
        print(f"{"-"*10} Lista de productos {"-"*10}")
        print()             
     
        for i in range(len(productos)):
           print(f"{i+1} - Nombre: {productos[i][0]}\n    Categoría: {productos[i][1]}\n    Precio: ${productos[i][2]}")
        
      else:
        print("No hay productos agregados por el momento.")
    case "3":
      encontrado = False
      if len(productos) != 0:
        busqueda = input("Ingresá el nombre del producto que estás buscando: ").strip().lower()
                  
        while busqueda == "":
          print("Error: escribi un producto para buscar.")
          busqueda = input("Ingresá el nombre del producto que estás buscando: ").strip().lower()

        for i in range(len(productos)):
          if busqueda in productos[i][0].lower():
            print()
            print(f"Producto encontrado: ID {i + 1}\n Nombre: {productos[i][0]}\n Categoría: {productos[i][1]}\n Precio: ${productos[i][2]} ")
            encontrado = True
        if not encontrado: 
            print("Producto no encontrado.")
      else:
              print("No hay productos agregados por el momento.")
    case "4":      
      
      if len(productos) == 0:
        print('No hay productos en la lista.')
      else:
        print(f"{"-"*10} Lista de productos {"-"*10}")
        print()       
        for i in range(len(productos)):
          print(f"{i+1} - Nombre: {productos[i][0]}\n    Categoría: {productos[i][1]}\n    Precio: ${productos[i][2]}")

        print()
        id_prod = input("Ingresá ID del producto que querés eliminar: ").strip()
       
        while not id_prod.isdigit() or int(id_prod) < 1 or int(id_prod) > len(productos):
          print("ID inválido. Ingresá un número de la lista.")
          id_prod = input("Ingresá ID del producto que querés eliminar: ").strip()

        indice_prod = int(id_prod) - 1
        prod_eliminado = productos.pop(indice_prod)
       
        print(f"Producto eliminado {prod_eliminado[0]}")
   
        print("")
        print(f"{"-"*6} Lista de productos actualizada {"-"*6}")
        for i in range(len(productos)):
          print(f"{i+1} - Nombre: {productos[i][0]}\n    Categoría: {productos[i][1]}\n    Precio: ${productos[i][2]}")
    case "5":
      print("¡¡Muchas gracias por usar el programa!!")
      salir = True
      break
    case _:
      print("Opción inválida. Ingrese una opción válida del 1 al 5")
     
    