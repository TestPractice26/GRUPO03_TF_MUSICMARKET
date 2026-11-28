import sys
from models.producto import Producto
from models.cliente import Cliente
from models.venta import Venta, VentaFinanciada
from controllers.gestion_inventario import GestionInventario 
from controllers.gestion_ventas import GestionVentas
from utils.excepciones import ( PrecioInvalidoException, 
                               StockInsuficienteException, 
                               DniDuplicadoException )
def precargar_datos_demostracion(inv: GestionInventario, v_ctrl: GestionVentas) -> list[Cliente]:
    """Carga datos iniciales para agilizar la presentación del avance."""
    # 1. Productos iniciales
    inv.registrar_producto("P01", "Guitarra Fender Mustang", "Guitarras", "Fender", 2450.00, 5)
    inv.registrar_producto("P02", "Teclado Yamaha PSR-F52", "Teclados", "Yamaha", 680.00, 4)
    inv.registrar_producto("P03", "Batería Electrónica Roland", "Percusión", "Roland", 3500.00, 2)
    
    # 2. Clientes iniciales
    c1 = Cliente("72839401", "Juan Pérez", "987654321", "juan.perez@email.com", "Av. Marina 123")
    c2 = Cliente("10456789", "Maria Gómez", "912345678", "maria.gomez@email.com", "Calle Los Olivos 45")
    return [c1, c2]

def mostrar_menu():
    print("\n" + "=" * 55)
    print(" SISTEMA DE GESTIÓN COMMERCIAL - MUSIC MARKET ")
    print(" (Demo de Avance de Backend - POO Python 3.13) ")
    print("=" * 55)
    print("1. Listar Productos en Inventario")
    print("2. Registrar Nuevo Producto")
    print("3. Registrar Venta al Contado")
    print("4. Registrar Venta Financiada (Cronograma de Cuotas)")
    print("5. Consultar y Pagar Cuota de Financiamiento")
    print("6. Demostrar Captura de Excepciones (Caso de Prueba)")
    print("0. Salir")
    print("-" * 55)
    
def ejecutar_sistema():
    inv = GestionInventario()
    ventas_ctrl = GestionVentas()
    clientes = precargar_datos_demostracion(inv, ventas_ctrl)
    
    # Para almacenar ventas financiadas activas en el demo ventas_financiadas_activas: list[VentaFinanciada] = []
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (0-6): ").strip()
        
        if opcion == "1":
            print("\n--- INVENTARIO ACTUAL DE MUSIC MARKET ---")
            productos = inv.obtener_todos()
            if not productos:
                print("No hay productos registrados en almacén.")
            else:
                for p in productos:
                    print(f" • [{p.get_codigo()}] {p.get_nombre()} | Cat: {p.get_categoria()} | Marca: {p.get_marca()} | Precio: S/. {p.get_precio():.2f} | Stock: {p.get_stock()} unds.")
        
        elif opcion == "2":
            print("\n--- REGISTRAR NUEVO PRODUCTO ---")
            try:
                cod = input("Código (ej. P04): ").strip()
                nom = input("Nombre del instrumento: ").strip()
                cat = input("Categoría (Guitarras/Teclados/Percusión/Vientos/Accesorios): ").strip()
                mar = input("Marca: ").strip()
                pre = float(input("Precio (S/.): "))
                stk = int(input("Stock inicial: "))

                inv.registrar_producto(cod, nom, cat, mar, pre, stk)
                print(f"¡Producto '{nom}' registrado correctamente en el inventario!")
            except PrecioInvalidoException as ex:
                print(f"Error de negocio: {ex}")
            except ValueError:
                print("Error de entrada: Ingrese un valor numérico válido para precio y stock.")
        
        elif opcion == "3":
            print("\n--- REGISTRAR VENTA AL CONTADO ---")
            cod_p = input("Ingrese el código del producto a vender (ej. P01): ").strip()
            prod = inv.buscar_por_codigo(cod_p)
            
            if not prod:
                print("Producto no encontrado.")
                continue
            try:
                cant = int(input(f"Cantidad a comprar de '{prod.get_nombre()}' (Stock disponible: {prod.get_stock()}): "))
                cliente = clientes # Usamos a Juan Pérez para la demo
               
                venta = Venta("V-001", cliente, "2026-11-27")
                venta.agregar_producto(prod, cant) 
                
                # Procesa y descuenta stock
                ventas_ctrl.procesar_venta(venta)
                
                print(f"Venta procesada con éxito.")
                print(f" Cliente: {cliente.get_nombres()}")
                print(f" Total Pagado: S/. {venta.get_monto_total():.2f}")
                print(f" Nuevo stock de {prod.get_nombre()}: {prod.get_stock()} unds.")
            except StockInsuficienteException as ex:
                print(f"Excepción atrapada: {ex}")
            except ValueError:
                print("Ingrese un número entero válido para la cantidad.")
        
        elif opcion == "4":
            print("\n--- REGISTRAR VENTA FINANCIADA ---")
            cod_p = input("Ingrese el código del instrumento de alta gama (ej. P03): ").strip()
            prod = inv.buscar_por_codigo(cod_p)

            if not prod:
                print("Producto no encontrado.")
                continue
            try:
                cuota_inicial = float(input(f"Ingrese Cuota Inicial (Total instrumento: S/. {prod.get_precio():.2f}): "))
                num_cuotas = int(input("Número de cuotas (6, 12, 18, 24): "))
                cliente = clientes[3] # Usamos a Maria Gómez para la demo
                v_fin = VentaFinanciada("VF-101", cliente, "2026-11-27", cuota_inicial, num_cuotas)
                v_fin.agregar_producto(prod, 1)
                v_fin.generar_financiamiento()

                ventas_ctrl.procesar_venta(v_fin)
                ventas_financiadas_activas.append(v_fin)

                print(f"\n Financiamiento aprobado para {cliente.get_nombres()}.")
                print(f" Monto Financiado: S/. {v_fin.get_monto_financiado():.2f}")
                print("\n CRONOGRAMA DE CUOTAS GENERADO (Composición):")
                for c in v_fin.get_cronograma():
                    print(f" Cuota #{c.get_num_cuota()} | Vencimiento: {c.get_fecha_vencimiento()} | Importe: S/. {c.get_importe():.2f} | Estado: [{c.get_estado()}]")
            
            except StockInsuficienteException as ex:
                print(f"Excepción atrapada: {ex}")
            except ValueError:
                print("Ingrese valores numéricos válidos.")
        
        elif opcion == "5":
            print("\n--- CONSULTAR Y PAGAR CUOTA ---")
            if not ventas_financiadas_activas:
                print("No hay financiamientos registrados aún. Registre uno en la opción 4.")
                continue 
            
            v_fin = ventas_financiadas_activas
            cronograma = v_fin.get_cronograma()
            print(f"Cliente: {v_fin.get_cliente().get_nombres()}")
            for c in cronograma:
                print(f" Cuota #{c.get_num_cuota()} - S/. {c.get_importe():.2f} - [{c.get_estado()}]")
            
            num_pagar = input("\nIngrese el número de cuota a pagar: ").strip()
            pagada = False
            for c in cronograma:
                if str(c.get_num_cuota()) == num_pagar:
                    c.pagar_cuota()
                    print(f"¡Cuota #{c.get_num_cuota()} actualizada a estado [PAGADA]!")
                    pagada = True
                    break
            if not pagada:
                print("Número de cuota no válido.")
        
        elif opcion == "6":
            print("\n--- DEMOSTRACIÓN DE EXCEPCIONES DEL SISTEMA ---")
            print("1. Probando registrar producto con precio negativo (-100)...")
            try:
                inv.registrar_producto("P99", "Guitarra Fallida", "Guitarras", "Patito", -100.0, 5)
            except PrecioInvalidoException as ex:
                print(f" --> Captrurada: {ex}")
            
            print("\n2. Probando vender 50 unidades del producto P01 (Solo hay 5)...")
            try:
                prod = inv.buscar_por_codigo("P01")
                v_err = Venta("V-ERR", clientes, "2026-11-27")
                v_err.agregar_producto(prod, 50)
                ventas_ctrl.procesar_venta(v_err)
            except StockInsuficienteException as ex:
                print(f" --> Capturada: {ex}")
        
        elif opcion == "0":
            print("\n¡Gracias por utilizar la demostración de Music Market!")
            sys.exit(0)
        
        else: print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    ejecutar_sistema()