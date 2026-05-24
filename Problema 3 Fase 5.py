# ============================================================
# Problema 3: Auditoría de Inventario
# Autor: Jamir José Carrascal Mejía
# Materia: Fundamentos de Programación
# Universidad: UNAD - Zona Caribe, Centro Puerto Colombia
# Grupo: 213022_15
# ============================================================

# --- MÓDULO (FUNCIÓN) ---
# Función que determina la cantidad exacta a pedir para un artículo

def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    """
    Determina la cantidad exacta a pedir para reabastecer un artículo.
    
    Parámetros:
        stock_actual (int): Cantidad de unidades actualmente en inventario.
        stock_minimo (int): Cantidad mínima requerida en inventario.
    
    Retorna:
        int: Cantidad de unidades a pedir. Cero si el stock es suficiente.
    """
    if stock_actual < stock_minimo:
        # Si el stock actual es menor al mínimo, se pide la diferencia
        cantidad_a_pedir = stock_minimo - stock_actual
    else:
        # Si el stock es suficiente, no se pide nada
        cantidad_a_pedir = 0
    return cantidad_a_pedir


# --- MATRIZ DE INVENTARIO ---
# Estructura: [Código Artículo, Nombre, Stock Actual, Stock Mínimo Requerido]

inventario = [
    ["A001", "Tornillos M6",         15,  50],
    ["A002", "Cable eléctrico 2mm",  80, 100],
    ["A003", "Resistencias 1kΩ",      5,  30],
    ["A004", "Condensadores 10µF",   45,  45],
    ["A005", "LEDs rojos",           12,  60],
    ["A006", "Fusibles 5A",          25,  20],
    ["A007", "Borneras 2 pines",      3,  40],
]


# --- PROGRAMA PRINCIPAL ---

print("=" * 55)
print("      SISTEMA DE AUDITORÍA DE INVENTARIO")
print("=" * 55)
print(f"{'Artículo':<25} {'Stock Actual':>12} {'Stock Mín.':>10} {'A Pedir':>8}")
print("-" * 55)

lista_pedidos = []  # Lista para guardar los artículos que necesitan reabastecimiento

for articulo in inventario:
    codigo        = articulo[0]
    nombre        = articulo[1]
    stock_actual  = articulo[2]
    stock_minimo  = articulo[3]
    
    # Llamada al módulo para calcular la cantidad a pedir
    cantidad = calcular_cantidad_a_pedir(stock_actual, stock_minimo)
    
    print(f"{nombre:<25} {stock_actual:>12} {stock_minimo:>10} {cantidad:>8}")
    
    # Si hay que pedir, se agrega a la lista de pedidos
    if cantidad > 0:
        lista_pedidos.append((nombre, cantidad))

# --- SALIDA: LISTA DE PEDIDOS ---
print("=" * 55)
print("\n LISTA DE PEDIDOS (artículos a reabastecer):")
print("-" * 45)

if lista_pedidos:
    for nombre, cantidad in lista_pedidos:
        print(f" {nombre}: solicitar {cantidad} unidades")
else:
    print(" Todos los artículos tienen stock suficiente.")

print("-" * 45)
print(f"  Total de artículos a pedir: {len(lista_pedidos)}")
print("=" * 55)
