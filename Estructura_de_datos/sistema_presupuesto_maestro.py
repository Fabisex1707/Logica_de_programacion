import pandas as pd
import pickle  # Para guardar y cargar datos
import os      # Para comprobar si el archivo de datos existe

# --- Funciones de Persistencia de Datos ---

def cargar_datos():
    """Intenta cargar el estado guardado (diccionarios y variables) desde un archivo."""
    archivo_datos = "datos_presupuesto.pkl"
    if os.path.exists(archivo_datos):
        try:
            with open(archivo_datos, "rb") as f:
                datos = pickle.load(f)
                print("--- Datos anteriores cargados exitosamente ---")
                return datos
        except Exception as e:
            print(f"Error al cargar datos: {e}. Iniciando con datos vacíos.")
    
    # Si no hay archivo o hay error, retorna un estado vacío
    return {
        'balance_inicial': {},
        'datos_productos': {},
        'datos_inventario': {},
        'datos_requerimientos': {},
        'datos_costos': {},
        'datos_adicionales': {},
        'datos_mano_obra': {}, 
        'totales_mod': {},
        'datos_gif': {},           
        'total_horas_mod_anual': 0,
        'total_gif_anual': 0,        
        'datos_ga': {},            
        'ventas_semestrales': (),
        'costos_unitarios': {},
        'total_inv_final_materiales': 0,     
        'total_inv_final_prod_terminado': 0,
        'costo_de_ventas': 0,
        'total_ga_total': 0,   
        'utilidad_neta': 0,
        'cobranza_2015': 0,
        'cobranza_2016': 0,
        'saldo_final_clientes': 0,
        'pago_prov_2015': 0,
        'pago_prov_2016': 0,
        'saldo_final_proveedores': 0,
        'isr_calculado_2016': 0, 
        'ptu_por_pagar': 0,
        'flujo_efectivo_final': 0
    }

def guardar_datos(estado):
    """Guarda el estado actual (diccionarios y variables) en un archivo."""
    archivo_datos = "datos_presupuesto.pkl"
    try:
        with open(archivo_datos, "wb") as f:
            pickle.dump(estado, f)
        print("--- Datos guardados exitosamente ---")
    except Exception as e:
        print(f"Error al guardar datos: {e}")

# --- Funciones de Presupuesto ---

def BalanceGeneral():
    print("----- Balance General -----")
    balance_inicial = {}

    print("--- Activos ---")
    balance_inicial['Efectivo'] = float(input("Ingrese el monto de Efectivo: "))
    balance_inicial['Clientes'] = float(input("Ingrese el monto de Clientes: "))
    balance_inicial['Deudores Diversos'] = float(input("Ingrese el monto de Deudores Diversos: "))
    balance_inicial['Funcionarios y Empleados'] = float(input("Ingrese el monto de Funcionarios y Empleados: "))
    balance_inicial['Inventario de Materiales'] = float(input("Ingrese el monto de Inventario de Materiales: "))
    balance_inicial['Inventario de Productos Terminados'] = float(input("Ingrese el monto de Inventario de Productos Terminados: "))
    balance_inicial['Terreno'] = float(input("Ingrese el monto de Terreno: "))
    balance_inicial['Planta y Equipo'] = float(input("Ingrese el monto de Planta y Equipo: "))
    balance_inicial['Depreciacion Acumulada'] = float(input("Ingrese el monto de Depreciación Acumulada: "))

    TotalDeActivoCirculante = (
        balance_inicial['Efectivo'] + balance_inicial['Clientes'] + 
        balance_inicial['Deudores Diversos'] + balance_inicial['Funcionarios y Empleados'] + 
        balance_inicial['Inventario de Materiales'] + balance_inicial['Inventario de Productos Terminados']
    )
    TotalDeActivoNoCirculante = (
        balance_inicial['Terreno'] + balance_inicial['Planta y Equipo'] - 
        balance_inicial['Depreciacion Acumulada']
    )
    TotalActivo = TotalDeActivoCirculante + TotalDeActivoNoCirculante

    print("--- Pasivos ---")
    balance_inicial['Proveedores'] = float(input("Ingrese el monto de Proveedores: "))
    balance_inicial['Documentos por Pagar'] = float(input("Ingrese el monto de Documentos por Pagar: "))
    balance_inicial['ISR por Pagar'] = float(input("Ingrese el monto de ISR por Pagar: "))
    balance_inicial['Préstamos Bancarios'] = float(input("Ingrese el monto de Préstamos Bancarios: "))
    balance_inicial['Capital Contribuido'] = float(input("Ingrese el monto de Capital Contribuido: "))
    balance_inicial['Capital Ganado'] = float(input("Ingrese el monto de Capital Ganado: "))

    TotalDePasivoCortoPlazo = (
        balance_inicial['Proveedores'] + balance_inicial['Documentos por Pagar'] + 
        balance_inicial['ISR por Pagar']
    )
    TotalDePasivoLargoPlazo = balance_inicial['Préstamos Bancarios']
    PasivoTotal = TotalDePasivoCortoPlazo + TotalDePasivoLargoPlazo
    CapitalContableTotal = balance_inicial['Capital Contribuido'] + balance_inicial['Capital Ganado']
    TotalPasivo = PasivoTotal + CapitalContableTotal 

    #DataFrame (solo para visualización, los datos ya están en el dict)
    data = {
        "Categoría": [
            "Efectivo", "Clientes", "Deudores Diversos", "Funcionarios y Empleados",
            "Inventario de Materiales", "Inventario de Productos Terminados", "Terreno",
            "Planta y Equipo", "Depreciación Acumulada", "Total de Activo Circulante",
            "Total de Activo No Circulante", "Total Activo", "Proveedores",
            "Documentos por Pagar", "ISR por Pagar", "Préstamos Bancarios",
            "Capital Contribuido", "Capital Ganado", "Total de Pasivo Corto Plazo",
            "Total de Pasivo Largo Plazo", "Pasivo Total", "Capital Contable Total",
            "Total Pasivo"
        ],
        "Monto": [
            balance_inicial['Efectivo'], balance_inicial['Clientes'], balance_inicial['Deudores Diversos'], 
            balance_inicial['Funcionarios y Empleados'], balance_inicial['Inventario de Materiales'],
            balance_inicial['Inventario de Productos Terminados'], balance_inicial['Terreno'],
            balance_inicial['Planta y Equipo'], balance_inicial['Depreciacion Acumulada'],
            TotalDeActivoCirculante, TotalDeActivoNoCirculante, TotalActivo,
            balance_inicial['Proveedores'], balance_inicial['Documentos por Pagar'], 
            balance_inicial['ISR por Pagar'], balance_inicial['Préstamos Bancarios'],
            balance_inicial['Capital Contribuido'], balance_inicial['Capital Ganado'],
            TotalDePasivoCortoPlazo, TotalDePasivoLargoPlazo, PasivoTotal,
            CapitalContableTotal, TotalPasivo
        ]
    }

    df = pd.DataFrame(data)
    
    # --- Formato de Impresión ---
    pd.options.display.float_format = '{:,.2f}'.format
    print(df)

    if abs(TotalActivo - TotalPasivo) < 0.01:
        print("\nEl Balance General está equilibrado.")
    else:
        print(TotalActivo)
        print(TotalPasivo)
        diferencia = TotalActivo - TotalPasivo
        print("\nEl Balance General NO está equilibrado. Favor de ingresar los datos correctamente.")
        print(f"\nDiferencia xd: {diferencia}")
        
    # Devolver el diccionario completo
    return balance_inicial

# ----- FUNCIÓN MODIFICADA -----
def Redaccion():
    print("----- Redacción -----")
    print("\nREQUERIMIENTO DE MATERIALES")

    datos_requerimientos = {}

    print("\n----- PRODUCTO CL -----")
    CL_A = float(input("Ingrese la Materia Prima A metros: "))
    CL_B = float(input("Ingrese la Materia Prima B metros: "))
    CL_C = float(input("Ingrese la Materia Prima C piezas: "))
    CL_HR = float(input("Ingrese la Mano de Obra Directa horas: "))
    datos_requerimientos['CL_A'] = CL_A
    datos_requerimientos['CL_B'] = CL_B
    datos_requerimientos['CL_C'] = CL_C
    datos_requerimientos['CL_HR'] = CL_HR


    print("\n----- PRODUCTO CE -----")
    CE_A = float(input("Ingrese la Materia Prima A metros: "))
    CE_B = float(input("Ingrese la Materia Prima B metros: "))
    CE_C = float(input("Ingrese la Materia Prima C piezas: "))
    CE_HR = float(input("Ingrese la Mano de Obra Directa horas: "))
    datos_requerimientos['CE_A'] = CE_A
    datos_requerimientos['CE_B'] = CE_B
    datos_requerimientos['CE_C'] = CE_C
    datos_requerimientos['CE_HR'] = CE_HR

    print("\n----- PRODUCTO CR -----")
    CR_A = float(input("Ingrese la Materia Prima A metros: "))
    CR_B = float(input("Ingrese la Materia Prima B metros: "))
    CR_C = float(input("Ingrese la Materia Prima C piezas: "))
    CR_HR = float(input("Ingrese la Mano de Obra Directa horas: "))
    datos_requerimientos['CR_A'] = CR_A
    datos_requerimientos['CR_B'] = CR_B
    datos_requerimientos['CR_C'] = CR_C
    datos_requerimientos['CR_HR'] = CR_HR

    print("\n---- INFORMACION DE INVENTARIOS ----")
    datos_inventario={} 
    print("\n---- Inventario Inicial Primer Semestre ----")
    IIPA = float(input("Ingrese la Materia Prima A metros: "))
    IIPB = float(input("Ingrese la Materia Prima B metros: "))
    IIPC = float(input("Ingrese la Materia Prima C piezas: "))
    IIP_CL = float(input("Producto CL:"))#<----1
    IIP_CE = float(input("Producto CE:"))#<----2
    IIP_CR = float(input("Producto CR:"))#<----3
    
    datos_inventario['IIPA'] = IIPA
    datos_inventario['IIPB'] = IIPB
    datos_inventario['IIPC'] = IIPC
    datos_inventario['IIP_CL'] = IIP_CL
    datos_inventario['IIP_CE'] = IIP_CE
    datos_inventario['IIP_CR'] = IIP_CR

    print("\n---- Inventario Final Segundo Semestre ----")
    IIFSA = float(input("Ingrese la Materia Prima A metros: "))
    IIFSB = float(input("Ingrese la Materia Prima B metros: "))
    IIFSC = float(input("Ingrese la Materia Prima C piezas: "))
    IIF_CL = float(input("Producto CL:"))#<---1
    IIF_CE = float(input("Producto CE:"))#<----2
    IIF_CR = float(input("Producto CR:"))#<----3

    datos_inventario['IIFSA'] = IIFSA
    datos_inventario['IIFSB'] = IIFSB
    datos_inventario['IIFSC'] = IIFSC
    datos_inventario['IIF_CL'] = IIF_CL
    datos_inventario['IIF_CE'] = IIF_CE
    datos_inventario['IIF_CR'] = IIF_CR

    datos_costos = {}
    print("\n ----- COSTO PRIMER SEMESTRE -----")
    CPA = float(input("Costo Materia Prima A metros: "))
    CPB = float(input("Costo Materia Prima B metros: "))
    CPC = float(input("Costo Materia Prima C piezas: "))
    datos_costos['CPA'] = CPA
    datos_costos['CPB'] = CPB
    datos_costos['CPC'] = CPC
    
    print("\n ----- COSTO SEGUNDO SEMESTRE -----")
    CSA = float(input("Costo Materia Prima A metros: "))
    CSB = float(input("Costo Materia Prima B metros: "))
    CSC = float(input("Costo Materia Prima C piezas: "))
    datos_costos['CSA'] = CSA
    datos_costos['CSB'] = CSB
    datos_costos['CSC'] = CSC

    print("\n----- MANO DE OBRA -----")
    datos_mano_obra = {}
    cuota_ps = float(input("Cuota por hora 1er Semestre (ej. 15.00): "))
    cuota_ss = float(input("Cuota por hora 2do Semestre (ej. 18.00): "))
    datos_mano_obra['cuota_ps'] = cuota_ps
    datos_mano_obra['cuota_ss'] = cuota_ss

    print("\n----- PRODUCTOS -----")
    datos_productos = {}
    
    print("\n---- PRODUCTO CL ----")
    datos_productos['PVP_CL'] = float(input("Precio de Venta Primer Semestre CL: "))
    datos_productos['PVS_CL'] = float(input("Precio de Venta Segundo Semestre CL: "))
    datos_productos['VPP_CL'] = float(input("Ventas planteadas Primer Semestre CL: "))
    datos_productos['VPS_CL'] = float(input("Ventas planteadas Segundo Semestre CL: "))

    print("\n---- PRODUCTO CE ----")
    datos_productos['PVP_CE'] = float(input("Precio de Venta Primer Semestre CE: "))
    datos_productos['PVS_CE'] = float(input("Precio de Venta Segundo Semestre CE: "))
    datos_productos['VPP_CE'] = float(input("Ventas planteadas Primer Semestre CE: "))
    datos_productos['VPS_CE'] = float(input("Ventas planteadas Segundo Semestre CE: "))

    print("\n---- PRODUCTO CR ----")
    datos_productos['PVP_CR'] = float(input("Precio de Venta Primer Semestre CR: "))
    datos_productos['PVS_CR'] = float(input("Precio de Venta Segundo Semestre CR: "))
    datos_productos['VPP_CR'] = float(input("Ventas planteadas Primer Semestre CR: "))
    datos_productos['VPS_CR'] = float(input("Ventas planteadas Segundo Semestre CR: "))

    print("\n----- Gastos de Administracion y Ventas -----")
    datos_ga = {} 
    datos_ga['depreciacion'] = float(input("Depreciación (Anual): "))
    datos_ga['sueldos'] = float(input("Sueldos y Salarios (Anual): "))
    datos_ga['varios1'] = float(input("Varios (Primer Semestre): "))
    datos_ga['varios2'] = float(input("Varios (Segundo Semestre): "))
    datos_ga['intereses'] = float(input("Intereses por Préstamos (Anual): "))

    print("\n----- Gastos de Fabricacion Indirectos -----")
    datos_gif = {} 
    DepreciacionGF = float(input("Depreciación (Anual): "))
    Seguros = float(input("Seguros (Anual): "))
    MantenimientoPS = float(input("Mantenimiento (Primer Semestre): "))
    MantenimientoSS = float(input("Mantenimiento (Segundo Semestre): "))
    EnergeticosPS = float(input("Energéticos (Primer Semestre): "))
    EnergeticosSS = float(input("Energéticos (Segundo Semestre): "))
    VariosGF = float(input("Varios (Anual): "))
    
    datos_gif['depreciacion_gf'] = DepreciacionGF
    datos_gif['seguros'] = Seguros
    datos_gif['mantenimiento_ps'] = MantenimientoPS
    datos_gif['mantenimiento_ss'] = MantenimientoSS
    datos_gif['energeticos_ps'] = EnergeticosPS
    datos_gif['energeticos_ss'] = EnergeticosSS
    datos_gif['varios_gf'] = VariosGF
    
    print("\nDatos ingresados correctamente")
    
    # Devolver una tupla con SIETE diccionarios
    return (datos_productos, datos_inventario, datos_requerimientos, datos_costos, datos_mano_obra, datos_gif, datos_ga)


def DatosAdicionales():
    """Recopila datos y porcentajes adicionales para los cálculos."""
    print("----- Datos Adicionales -----")
    datos_add = {}
    
    # 1. Equipo nuevo
    datos_add['equipo_nuevo'] = float(input("1. Ingrese el valor del equipo nuevo a adquirir (ej. 85000): "))
    
    # 2. Tasa ISR
    tasa_isr = float(input("2. Ingrese la Tasa de ISR (ej. 30 para 30%): "))
    datos_add['tasa_isr'] = tasa_isr / 100.0
    
    # 3. Tasa PTU
    tasa_ptu = float(input("3. Ingrese la Tasa de PTU (ej. 10 para 10%): "))
    datos_add['tasa_ptu'] = tasa_ptu / 100.0
    
    # 4. Cobranza 2015
    cobranza_2015 = float(input("4. Ingrese el % de cobranza de clientes 2015 (ej. 100): "))
    datos_add['cobranza_2015'] = cobranza_2015 / 100.0
    
    # 5. Cobranza 2016
    cobranza_2016 = float(input("5. Ingrese el % de cobranza de ventas 2016 (ej. 80): "))
    datos_add['cobranza_2016'] = cobranza_2016 / 100.0
    
    # 6. Pago Proveedores 2015
    pago_prov_2015 = float(input("6. Ingrese el % de pago a proveedores 2015 (ej. 100): "))
    datos_add['pago_prov_2015'] = pago_prov_2015 / 100.0
    
    # 7. Pago Compras 2016
    pago_compras_2016 = float(input("7. Ingrese el % de pago de compras 2016 (ej. 50): "))
    datos_add['pago_compras_2016'] = pago_compras_2016 / 100.0
    
    # 8. Pago ISR 2015
    pago_isr_2015 = input("8. ¿Se pagará el ISR correspondiente al 2015? (S/N): ")
    datos_add['pago_isr_2015'] = pago_isr_2015.upper()
    
    # 9. Tasa Comisiones
    tasa_comisiones = float(input("9. Ingrese el % de Comisiones sobre ventas (ej. 1): "))
    datos_add['tasa_comisiones'] = tasa_comisiones / 100.0
    
    print("\nDatos adicionales guardados.")
    return datos_add

# ----- FUNCIÓN MODIFICADA -----
def PresupuestoVentas(datos_productos):
    """Genera y muestra la tabla de presupuesto de ventas"""
    print("----- 1. Presupuesto de Ventas -----")
    
    PVP_CL = datos_productos['PVP_CL']
    VPP_CL = datos_productos['VPP_CL']
    PVS_CL = datos_productos['PVS_CL']
    VPS_CL = datos_productos['VPS_CL']
    
    PVP_CE = datos_productos['PVP_CE']
    VPP_CE = datos_productos['VPP_CE']
    PVS_CE = datos_productos['PVS_CE']
    VPS_CE = datos_productos['VPS_CE']
    
    PVP_CR = datos_productos['PVP_CR']
    VPP_CR = datos_productos['VPP_CR']
    PVS_CR = datos_productos['PVS_CR']
    VPS_CR = datos_productos['VPS_CR']
    
    ImporteDeVentaCL1 = VPP_CL * PVP_CL
    ImporteDeVentaCL2 = VPS_CL * PVS_CL
    ImporteDeVenta2016_CL = ImporteDeVentaCL1 + ImporteDeVentaCL2

    ImporteDeVentaCE1 = VPP_CE * PVP_CE
    ImporteDeVentaCE2 = VPS_CE * PVS_CE
    ImporteDeVenta2016_CE = ImporteDeVentaCE1 + ImporteDeVentaCE2

    ImporteDeVentaCR1 = VPP_CR * PVP_CR
    ImporteDeVentaCR2 = VPS_CR * PVS_CR
    ImporteDeVenta2016_CR = ImporteDeVentaCR1 + ImporteDeVentaCR2

    TotalVentasSemestre = ImporteDeVentaCL1 + ImporteDeVentaCE1 + ImporteDeVentaCR1
    TotalVentasSemestre2 = ImporteDeVentaCL2 + ImporteDeVentaCE2 + ImporteDeVentaCR2
    TotalVentas2016 = ImporteDeVenta2016_CL + ImporteDeVenta2016_CE + ImporteDeVenta2016_CR

    df = pd.DataFrame({
        "1er Semestre": [
            "", VPP_CL, PVP_CL, ImporteDeVentaCL1,
            "", VPP_CE, PVP_CE, ImporteDeVentaCE1,
            "", VPP_CR, PVP_CR, ImporteDeVentaCR1,
            TotalVentasSemestre
        ],
        "2do Semestre": [
            "", VPS_CL, PVS_CL, ImporteDeVentaCL2,
            "", VPS_CE, PVS_CE, ImporteDeVentaCE2,
            "", VPS_CR, PVS_CR, ImporteDeVentaCR2,
            TotalVentasSemestre2
        ],
        "2016": [
            "", "", "", ImporteDeVenta2016_CL,
            "", "", "", ImporteDeVenta2016_CE,
            "", "", "", ImporteDeVenta2016_CR,
            TotalVentas2016
        ]
    })

    df.index = [
        "PRODUCTO CL",
        "Unidades a vender",
        "Precio de Venta",
        "Importe de Venta",
        "PRODUCTO CE",
        "Unidades a vender",
        "Precio de Venta",
        "Importe de Venta",
        "PRODUCTO CR",
        "Unidades a vender",
        "Precio de Venta",
        "Importe de Venta",
        "Total de Ventas por Semestre"
    ]

    print("\n")
    # --- Formato de Impresión ---
    pd.options.display.float_format = '{:,.2f}'.format
    print(df)
    print("\n")
    # Retorna los 3 valores
    return (TotalVentasSemestre, TotalVentasSemestre2, TotalVentas2016)

# ----- FUNCIÓN MODIFICADA -----
def SaldoClientesyFlujoDeEntradas(clientes:float, TotalVentasAnual:float, datos_adicionales: dict):
    """Genera y muestra la tabla Determinación del Saldo de Clientes y Flujos de Entrada"""
    print("----- 2. Saldo de clientes y flujo de entradas -----")
    
    tasa_cobranza_2015 = datos_adicionales.get('cobranza_2015', 1.0) 
    tasa_cobranza_2016 = datos_adicionales.get('cobranza_2016', 0.8) 
    
    SALDOCLIENTES = clientes
    VENTAS = TotalVentasAnual # <-- Recibe el total anual
    total_clientes_año = SALDOCLIENTES + VENTAS
    
    PORCOBRANZA2015 = SALDOCLIENTES * tasa_cobranza_2015
    PORCOBRANZA2016 = VENTAS * tasa_cobranza_2016
    
    TOTALCOBRANZA = PORCOBRANZA2015 + PORCOBRANZA2016
    SALDOCLIENTESFINAÑO = total_clientes_año - TOTALCOBRANZA

    df = pd.DataFrame(
        {
            "IMPORTE": [
                "",
                "",
                "",
                PORCOBRANZA2015,
                PORCOBRANZA2016, 
                "",
                ""
            ], 
            "TOTAL": [
                SALDOCLIENTES,
                VENTAS,
                total_clientes_año,
                "",
                "",
                TOTALCOBRANZA,
                SALDOCLIENTESFINAÑO
            ]
        }
    )

    df.index = [
        "Saldo de Clientes al inicio del año",
        "Ventas del año",           
        "Total Clientes del año",
        "Por cobranza del año 2015",
        "Por cobranza del año 2016",
        "Total cobranza",
        "Saldo de Clientes al final del año"
    ]

    print("\n")
    # --- Formato de Impresión ---
    pd.options.display.float_format = '{:,.2f}'.format
    print(df)
    print("\n")
    
    # Retornar los valores para el Flujo de Efectivo y Balance Final
    return (PORCOBRANZA2015, PORCOBRANZA2016, SALDOCLIENTESFINAÑO)

# ----- FUNCIÓN MODIFICADA -----
def PresupuestoDeProduccion(DatosProductos: dict, DatosInventario: dict):
    """Genera y muestra la tabla Presupuesto de produccion y retorna las unidades a producir"""
    print("----- 3. Presupuesto de produccion -----")
    
    # Datos extraídos de DatosProductos
    UAVPS_CL=DatosProductos["VPP_CL"]
    UAVSS_CL=DatosProductos["VPS_CL"]
    UAVPS_CE=DatosProductos["VPP_CE"]
    UAVSS_CE=DatosProductos["VPS_CE"]
    UAVPS_CR=DatosProductos["VPP_CR"]
    UAVSS_CR=DatosProductos["VPS_CR"]
    
    # Datos extraídos de DatosInventario
    IFPS_CL=DatosInventario["IIP_CL"]
    IFSS_CL=DatosInventario["IIF_CL"]
    IFPS_CE=DatosInventario["IIP_CE"]
    IFSS_CE=DatosInventario["IIF_CE"]
    IFPS_CR=DatosInventario["IIP_CR"]
    IFSS_CR=DatosInventario["IIF_CR"]
    
    # Datos extraídos de DatosInventario
    IIPS_CL=DatosInventario["IIP_CL"]
    IISS_CL=DatosInventario["IIP_CL"] 
    IIPS_CE=DatosInventario["IIP_CE"]
    IISS_CE=DatosInventario["IIP_CE"] 
    IIPS_CR=DatosInventario["IIP_CR"]
    IISS_CR=DatosInventario["IIP_CR"] 

    #TOTAL DE UNIDADES PRIMER SEMESTRE
    total_unidades_ps_cl=UAVPS_CL+IFPS_CL
    total_unidades_ps_ce=UAVPS_CE+IFPS_CE
    total_unidades_ps_cr=UAVPS_CR+IFPS_CR
    #UNIDADES A PRODUCIR PRIMER SEMESTRE
    unidades_producir_ps_cl=total_unidades_ps_cl-IIPS_CL
    unidades_producir_ps_ce=total_unidades_ps_ce-IIPS_CE
    unidades_producir_ps_cr=total_unidades_ps_cr-IIPS_CR
    #TOTAL DE UNIDADES SEGUNDO SEMESTRE
    total_unidades_ss_cl=UAVSS_CL+IFSS_CL
    total_unidades_ss_ce=UAVSS_CE+IFSS_CE
    total_unidades_ss_cr=UAVSS_CR+IFSS_CR
    #UNIDADES A PRODUCIR SEGUNDO SEMESTRE
    unidades_producir_ss_cl=total_unidades_ss_cl-IISS_CL
    unidades_producir_ss_ce=total_unidades_ss_ce-IISS_CE
    unidades_producir_ss_cr=total_unidades_ss_cr-IISS_CR
    #TOTAL 2016
    unidades_vender_total_cl=UAVPS_CL+UAVSS_CL
    unidades_vender_total_ce=UAVPS_CE+UAVSS_CE
    unidades_vender_total_cr=UAVPS_CR+UAVSS_CR
    total_unidades_cl_total=total_unidades_ps_cl+total_unidades_ss_cl
    total_unidades_ce_total=total_unidades_ps_ce+total_unidades_ss_ce
    total_unidades_cr_total=total_unidades_ps_cr+total_unidades_ss_cr
    unidades_producir_total_cl=unidades_producir_ps_cl+unidades_producir_ss_cl
    unidades_producir_total_ce=unidades_producir_ps_ce+unidades_producir_ss_ce
    unidades_producir_total_cr=unidades_producir_ps_cr+unidades_producir_ss_cr

    df = pd.DataFrame(
        {
            "1.ER SEMESTRE": [
                "",
                UAVPS_CL,
                IFPS_CL, 
                total_unidades_ps_cl,
                IIPS_CL,
                unidades_producir_ps_cl,
                "",
                UAVPS_CE,
                IFPS_CE,
                total_unidades_ps_ce,
                IIPS_CE,
                unidades_producir_ps_ce,
                "",
                UAVPS_CR,
                IFPS_CR,
                total_unidades_ps_cr,
                IIPS_CR,
                unidades_producir_ps_cr
            ], 
            "2DO. SEMESTRE": [
                "",
                UAVSS_CL,
                IFSS_CL, 
                total_unidades_ss_cl,
                IISS_CL,
                unidades_producir_ss_cl,
                "",
                UAVSS_CE,
                IFSS_CE,
                total_unidades_ss_ce,
                IISS_CE,
                unidades_producir_ss_ce,
                "",
                UAVSS_CR,
                IFSS_CR,
                total_unidades_ss_cr,
                IISS_CR,
                unidades_producir_ss_cr
            ],
            "TOTAL 2016":[
                "",
                unidades_vender_total_cl,
                IFSS_CL,
                total_unidades_cl_total,
                IIPS_CL,
                unidades_producir_total_cl,
                "",
                unidades_vender_total_ce,
                IFSS_CE,
                total_unidades_ce_total,
                IIPS_CE,
                unidades_producir_total_ce,
                "",
                unidades_vender_total_cr,
                IFSS_CR,
                total_unidades_cr_total,
                IIPS_CR,
                unidades_producir_total_cr, 
            ]
        }
    )

    df.index = [
        "PRODUCTO CL",
        "Unidades a vendar",           
        "(+) Iventario final",
        "(=) Total de unidades",
        "(-) Iventario inicial",
        "(=) Unidades a producir",
        "PRODUCTO CE",
        "Unidades a vendar",           
        "(+) Iventario final",
        "(=) Total de unidades",
        "(-) Iventario inicial",
        "(=) Unidades a producir",
        "PRODUCTO CR",
        "Unidades a vendar",           
        "(+) Ivertario final",
        "(=) Total de unidades",
        "(-) Iventario inicial",
        "(=) Unidades a producir"
    ]

    print("\n")
    # --- Formato de Impresión ---
    pd.options.display.float_format = '{:,.2f}'.format
    print(df)
    print("\n")

    # Crear diccionario con los valores a retornar
    unidades_a_producir = {
        'ps_cl': unidades_producir_ps_cl, 'ss_cl': unidades_producir_ss_cl, 'total_cl': unidades_producir_total_cl,
        'ps_ce': unidades_producir_ps_ce, 'ss_ce': unidades_producir_ss_ce, 'total_ce': unidades_producir_total_ce,
        'ps_cr': unidades_producir_ps_cr, 'ss_cr': unidades_producir_ss_cr, 'total_cr': unidades_producir_total_cr
    }
    
    return unidades_a_producir

# ----- FUNCIÓN MODIFICADA -----
def PresupuestodeRequerimientosdeMateriales(unidades_producir: dict, req_materiales: dict):
    """Genera y muestra la tabla Presupuesto de Requerimiento de Materiales y retorna los totales"""
    print("----- 4. Presupuesto de Requerimiento de Materiales -----")

    # --- Extracción de datos de Unidades a Producir ---
    u_ps_cl = unidades_producir['ps_cl']
    u_ss_cl = unidades_producir['ss_cl']
    u_total_cl = unidades_producir['total_cl']
    
    u_ps_ce = unidades_producir['ps_ce']
    u_ss_ce = unidades_producir['ss_ce']
    u_total_ce = unidades_producir['total_ce']
    
    u_ps_cr = unidades_producir['ps_cr']
    u_ss_cr = unidades_producir['ss_cr']
    u_total_cr = unidades_producir['total_cr']

    # --- Extracción de datos de Requerimientos de Materiales ---
    r_a_cl = req_materiales['CL_A']
    r_b_cl = req_materiales['CL_B']
    r_c_cl = req_materiales['CL_C']
    
    r_a_ce = req_materiales['CE_A']
    r_b_ce = req_materiales['CE_B']
    r_c_ce = req_materiales['CE_C']
    
    r_a_cr = req_materiales['CR_A']
    r_b_cr = req_materiales['CR_B']
    r_c_cr = req_materiales['CR_C']

    # --- Cálculos Producto CL ---
    t_a_ps_cl = u_ps_cl * r_a_cl
    t_a_ss_cl = u_ss_cl * r_a_cl
    t_a_total_cl = u_total_cl * r_a_cl
    
    t_b_ps_cl = u_ps_cl * r_b_cl
    t_b_ss_cl = u_ss_cl * r_b_cl
    t_b_total_cl = u_total_cl * r_b_cl
    
    t_c_ps_cl = u_ps_cl * r_c_cl
    t_c_ss_cl = u_ss_cl * r_c_cl
    t_c_total_cl = u_total_cl * r_c_cl

    # --- Cálculos Producto CE ---
    t_a_ps_ce = u_ps_ce * r_a_ce
    t_a_ss_ce = u_ss_ce * r_a_ce
    t_a_total_ce = u_total_ce * r_a_ce
    
    t_b_ps_ce = u_ps_ce * r_b_ce
    t_b_ss_ce = u_ss_ce * r_b_ce
    t_b_total_ce = u_total_ce * r_b_ce
    
    t_c_ps_ce = u_ps_ce * r_c_ce
    t_c_ss_ce = u_ss_ce * r_c_ce
    t_c_total_ce = u_total_ce * r_c_ce
    
    # --- Cálculos Producto CR ---
    t_a_ps_cr = u_ps_cr * r_a_cr
    t_a_ss_cr = u_ss_cr * r_a_cr
    t_a_total_cr = u_total_cr * r_a_cr
    
    t_b_ps_cr = u_ps_cr * r_b_cr
    t_b_ss_cr = u_ss_cr * r_b_cr
    t_b_total_cr = u_total_cr * r_b_cr
    
    t_c_ps_cr = u_ps_cr * r_c_cr
    t_c_ss_cr = u_ss_cr * r_c_cr
    t_c_total_cr = u_total_cr * r_c_cr
    
    # --- Cálculos de Totales Generales ---
    total_req_A_ps = t_a_ps_cl + t_a_ps_ce + t_a_ps_cr
    total_req_A_ss = t_a_ss_cl + t_a_ss_ce + t_a_ss_cr
    total_req_A_total = t_a_total_cl + t_a_total_ce + t_a_total_cr
    
    total_req_B_ps = t_b_ps_cl + t_b_ps_ce + t_b_ps_cr
    total_req_B_ss = t_b_ss_cl + t_b_ss_ce + t_b_ss_cr
    total_req_B_total = t_b_total_cl + t_b_total_ce + t_b_total_cr
    
    total_req_C_ps = t_c_ps_cl + t_c_ps_ce + t_c_ps_cr
    total_req_C_ss = t_c_ss_cl + t_c_ss_ce + t_c_ss_cr
    total_req_C_total = t_c_total_cl + t_c_total_ce + t_c_total_cr

    # --- Construcción del DataFrame ---
    data = {
        "1er. Semestre": [
            "", u_ps_cl, 
            "", r_a_cl, t_a_ps_cl,
            "", r_b_cl, t_b_ps_cl,
            "", r_c_cl, t_c_ps_cl,
            "", u_ps_ce,
            "", r_a_ce, t_a_ps_ce,
            "", r_b_ce, t_b_ps_ce,
            "", r_c_ce, t_c_ps_ce,
            "", u_ps_cr,
            "", r_a_cr, t_a_ps_cr,
            "", r_b_cr, t_b_ps_cr,
            "", r_c_cr, t_c_ps_cr
        ],
        "2do. Semestre": [
            "", u_ss_cl,
            "", r_a_cl, t_a_ss_cl,
            "", r_b_cl, t_b_ss_cl,
            "", r_c_cl, t_c_ss_cl,
            "", u_ss_ce,
            "", r_a_ce, t_a_ss_ce,
            "", r_b_ce, t_b_ss_ce,
            "", r_c_ce, t_c_ss_ce,
            "", u_ss_cr,
            "", r_a_cr, t_a_ss_cr,
            "", r_b_cr, t_b_ss_cr,
            "", r_c_cr, t_c_ss_cr
        ],
        "Total 2016": [
            "", u_total_cl,
            "", r_a_cl, t_a_total_cl,
            "", r_b_cl, t_b_total_cl,
            "", r_c_cl, t_c_total_cl,
            "", u_total_ce,
            "", r_a_ce, t_a_total_ce,
            "", r_b_ce, t_b_total_ce,
            "", r_c_ce, t_c_total_ce,
            "", u_total_cr,
            "", r_a_cr, t_a_total_cr,
            "", r_b_cr, t_b_total_cr,
            "", r_c_cr, t_c_total_cr
        ]
    }
    
    index = [
        "PRODUCTO CL", "Unidades a producir",
        "Material A", "Requerimiento de material", "Total de Material A requerido",
        "Material B", "Requerimiento de material", "Total de Material B requerido",
        "Material C", "Requerimiento de material", "Total de Material C requerido",
        "PRODUCTO CE", "Unidades a producir",
        "Material A", "Requerimiento de material", "Total de Material A requerido",
        "Material B", "Requerimiento de material", "Total de Material B requerido",
        "Material C", "Requerimiento de material", "Total de Material C requerido",
        "PRODUCTO CR", "Unidades a producir",
        "Material A", "Requerimiento de material", "Total de Material A requerido",
        "Material B", "Requerimiento de material", "Total de Material B requerido",
        "Material C", "Requerimiento de material", "Total de Material C requerido"
    ]

    df = pd.DataFrame(data, index=index)
    
    # --- Añadir el bloque "Total de Requerimientos" ---
    df.loc[" "] = ["", "", ""] 
    df.loc["Total de Requerimientos"] = ["", "", ""] 
    df.loc["  Material A"] = [total_req_A_ps, total_req_A_ss, total_req_A_total]
    df.loc["  Material B"] = [total_req_B_ps, total_req_B_ss, total_req_B_total]
    df.loc["  Material C"] = [total_req_C_ps, total_req_C_ss, total_req_C_total]
    df.loc["   "] = ["", "", ""] 
    
    print("\n")
    # --- Formato de Impresión ---
    pd.options.display.float_format = '{:,.2f}'.format
    print(df) # Imprimir el DataFrame 'crudo'
    print("\n")
    
    # --- Crear diccionario de totales para retornar ---
    total_requerimientos = {
        'req_A_ps': total_req_A_ps, 'req_A_ss': total_req_A_ss, 'req_A_total': total_req_A_total,
        'req_B_ps': total_req_B_ps, 'req_B_ss': total_req_B_ss, 'req_B_total': total_req_B_total,
        'req_C_ps': total_req_C_ps, 'req_C_ss': total_req_C_ss, 'req_C_total': total_req_C_total,
    }
    
    return total_requerimientos


def PresupuestodeComprasdeMateriales(total_req: dict, datos_inv: dict, datos_costos: dict):
    """Genera y muestra la tabla Presupuesto de Compras de Materiales"""
    print("----- 5. Presupuesto de Compras de Materiales -----")

    # --- Extracción de datos de Requerimientos Totales ---
    req_a_ps = total_req['req_A_ps']
    req_a_ss = total_req['req_A_ss']
    req_a_total = total_req['req_A_total']
    
    req_b_ps = total_req['req_B_ps']
    req_b_ss = total_req['req_B_ss']
    req_b_total = total_req['req_B_total']
    
    req_c_ps = total_req['req_C_ps']
    req_c_ss = total_req['req_C_ss']
    req_c_total = total_req['req_C_total']

    # --- Extracción de datos de Inventario (Materiales) ---
    ii_a_ps = datos_inv['IIPA']
    ii_b_ps = datos_inv['IIPB']
    ii_c_ps = datos_inv['IIPC']
    
    if_a_ps = datos_inv['IIPA'] 
    if_b_ps = datos_inv['IIPB']
    if_c_ps = datos_inv['IIPC']
    
    ii_a_ss = datos_inv['IIPA'] 
    ii_b_ss = datos_inv['IIPB']
    ii_c_ss = datos_inv['IIPC']
    
    if_a_ss = datos_inv['IIFSA'] 
    if_b_ss = datos_inv['IIFSB']
    if_c_ss = datos_inv['IIFSC']

    # --- Extracción de datos de Costos ---
    pc_a_ps = datos_costos['CPA']
    pc_b_ps = datos_costos['CPB']
    pc_c_ps = datos_costos['CPC']
    
    pc_a_ss = datos_costos['CSA']
    pc_b_ss = datos_costos['CSB']
    pc_c_ss = datos_costos['CSC']

    # --- Cálculos Material A ---
    total_mat_a_ps = req_a_ps + if_a_ps
    total_mat_a_ss = req_a_ss + if_a_ss
    mat_comp_a_ps = total_mat_a_ps - ii_a_ps
    mat_comp_a_ss = total_mat_a_ss - ii_a_ss
    total_costo_a_ps = mat_comp_a_ps * pc_a_ps
    total_costo_a_ss = mat_comp_a_ss * pc_a_ss
    # Total 2016 (Material A)
    total_req_a_2016 = req_a_total
    if_a_2016 = if_a_ss
    total_mat_a_2016 = total_req_a_2016 + if_a_2016
    ii_a_2016 = ii_a_ps
    mat_comp_a_2016 = mat_comp_a_ps + mat_comp_a_ss
    pc_a_2016 = ""
    total_costo_a_2016 = total_costo_a_ps + total_costo_a_ss

    # --- Cálculos Material B ---
    total_mat_b_ps = req_b_ps + if_b_ps
    total_mat_b_ss = req_b_ss + if_b_ss
    mat_comp_b_ps = total_mat_b_ps - ii_b_ps
    mat_comp_b_ss = total_mat_b_ss - ii_b_ss
    total_costo_b_ps = mat_comp_b_ps * pc_b_ps
    total_costo_b_ss = mat_comp_b_ss * pc_b_ss
    # Total 2016 (Material B)
    total_req_b_2016 = req_b_total
    if_b_2016 = if_b_ss
    total_mat_b_2016 = total_req_b_2016 + if_b_2016
    ii_b_2016 = ii_b_ps
    mat_comp_b_2016 = mat_comp_b_ps + mat_comp_b_ss
    pc_b_2016 = ""
    total_costo_b_2016 = total_costo_b_ps + total_costo_b_ss

    # --- Cálculos Material C ---
    total_mat_c_ps = req_c_ps + if_c_ps
    total_mat_c_ss = req_c_ss + if_c_ss
    mat_comp_c_ps = total_mat_c_ps - ii_c_ps
    mat_comp_c_ss = total_mat_c_ss - ii_c_ss
    total_costo_c_ps = mat_comp_c_ps * pc_c_ps
    total_costo_c_ss = mat_comp_c_ss * pc_c_ss
    # Total 2016 (Material C)
    total_req_c_2016 = req_c_total
    if_c_2016 = if_c_ss
    total_mat_c_2016 = total_req_c_2016 + if_c_2016
    ii_c_2016 = ii_c_ps
    mat_comp_c_2016 = mat_comp_c_ps + mat_comp_c_ss
    pc_c_2016 = ""
    total_costo_c_2016 = total_costo_c_ps + total_costo_c_ss

    # --- Cálculos Compras Totales ---
    compras_ps = total_costo_a_ps + total_costo_b_ps + total_costo_c_ps
    compras_ss = total_costo_a_ss + total_costo_b_ss + total_costo_c_ss
    compras_total = total_costo_a_2016 + total_costo_b_2016 + total_costo_c_2016

    # --- Construcción del DataFrame (Corregido) ---
    data = {
        "1er. Semestre": [
            "", # Para "Material A"
            req_a_ps, if_a_ps, total_mat_a_ps, ii_a_ps, mat_comp_a_ps, pc_a_ps, total_costo_a_ps,
            "", # Para " " (espaciador)
            "", # Para "Material B"
            req_b_ps, if_b_ps, total_mat_b_ps, ii_b_ps, mat_comp_b_ps, pc_b_ps, total_costo_b_ps,
            "", # Para "  " (espaciador)
            "", # Para "Material C"
            req_c_ps, if_c_ps, total_mat_c_ps, ii_c_ps, mat_comp_c_ps, pc_c_ps, total_costo_c_ps
        ],
        "2do. Semestre": [
            "", # Para "Material A"
            req_a_ss, if_a_ss, total_mat_a_ss, ii_a_ss, mat_comp_a_ss, pc_a_ss, total_costo_a_ss,
            "", # Para " " (espaciador)
            "", # Para "Material B"
            req_b_ss, if_b_ss, total_mat_b_ss, ii_b_ss, mat_comp_b_ss, pc_b_ss, total_costo_b_ss,
            "", # Para "  " (espaciador)
            "", # Para "Material C"
            req_c_ss, if_c_ss, total_mat_c_ss, ii_c_ss, mat_comp_c_ss, pc_c_ss, total_costo_c_ss
        ],
        "Total 2016": [
            "", # Para "Material A"
            total_req_a_2016, if_a_2016, total_mat_a_2016, ii_a_2016, mat_comp_a_2016, pc_a_2016, total_costo_a_2016,
            "", # Para " " (espaciador)
            "", # Para "Material B"
            total_req_b_2016, if_b_2016, total_mat_b_2016, ii_b_2016, mat_comp_b_2016, pc_b_2016, total_costo_b_2016,
            "", # Para "  " (espaciador)
            "", # Para "Material C"
            total_req_c_2016, if_c_2016, total_mat_c_2016, ii_c_2016, mat_comp_c_2016, pc_c_2016, total_costo_c_2016
        ]
    }

    index = [
        "Material A", "Requerimiento de materiales", "(+) Inventario Final", "Total de Materiales", "(-) Inventario Inicial", "Material a comprar", "Precio de Compra", "Total de Material A en $:",
        " ", # Espaciador
        "Material B", "Requerimiento de materiales", "(+) Inventario Final", "Total de Materiales", "(-) Inventario Inicial", "Material a comprar", "Precio de Compra", "Total de Material B en $:",
        "  ", # Espaciador
        "Material C", "Requerimiento de materiales", "(+) Inventario Final", "Total de Materiales", "(-) Inventario Inicial", "Material a comprar", "Precio de Compra", "Total de Material C en $:"
    ]

    df = pd.DataFrame(data, index=index)
    
    # --- Añadir el bloque "Compras totales" (sin formato) ---
    df.loc["   "] = ["", "", ""] # Espaciador
    df.loc["Compras totales"] = [compras_ps, compras_ss, compras_total]
    
    print("\n")
    # --- Formato de Impresión ---
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.options.display.float_format = '{:,.2f}'.format
    print(df) # Imprimir el DataFrame 'crudo'
    print("\n")

    return compras_total

# ----- FUNCIÓN MODIFICADA -----
def TotaldeproveedoresyFlujodeSalidas(saldo_prov_2015, compras_2016, datos_ad):
    """Genera la tabla 6. Determinación del saldo de Proveedores y Flujo de Salidas"""
    print("----- 6. Determinación del saldo de Proveedores y Flujo de Salidas -----")

    # --- Extracción de datos ---
    tasa_pago_2015 = datos_ad.get('pago_prov_2015', 1.0) # 100%
    tasa_pago_2016 = datos_ad.get('pago_compras_2016', 0.5) # 50%
    
    # --- Cálculos ---
    total_prov_2016 = saldo_prov_2015 + compras_2016
    
    pago_2015 = saldo_prov_2015 * tasa_pago_2015
    pago_2016 = compras_2016 * tasa_pago_2016
    
    total_salidas = pago_2015 + pago_2016
    saldo_prov_2016 = total_prov_2016 - total_salidas

    # --- Construcción del DataFrame (según la imagen) ---
    data = {
        "Importe": [
            "",
            "",
            "",
            "", # "Salidas de Efectivo:"
            pago_2015,
            pago_2016,
            "", # "Total de Salidas 2016:"
            ""  # "Saldo de Proveedores del 2016"
        ],
        "Total": [
            saldo_prov_2015,
            compras_2016,
            total_prov_2016,
            "", # "Salidas de Efectivo:"
            "",
            "",
            total_salidas,
            saldo_prov_2016
        ]
    }
    
    index = [
        "Saldo de Proveedores 31-Dic-2015",
        "Compras 2016",
        "Total de Proveedores 2016",
        "Salidas de Efectivo:",
        "Por Proveedores del 2015",
        "Por Proveedores del 2016",
        "Total de Salidas 2016:",
        "Saldo de Proveedores del 2016"
    ]
    
    df = pd.DataFrame(data, index=index)
    
    print("\n")
    # --- Formato de Impresión ---
    pd.options.display.float_format = '{:,.2f}'.format
    print(df)
    print("\n")
    
    # Retornar los valores para el Flujo de Efectivo y Balance Final
    return (pago_2015, pago_2016, saldo_prov_2016)

# ----- FUNCIÓN MODIFICADA -----
def PresupuestoManoDeObraDirecta(unidades_producir: dict, req_materiales: dict, datos_mo: dict):
    """Genera la tabla 7. Presupuesto de Mano de Obra Directa (M.O.D.)"""
    print("----- 7. Presupuesto de Mano de Obra Directa -----")

    # --- Extracción de datos de Unidades a Producir ---
    u_ps_cl = unidades_producir['ps_cl']
    u_ss_cl = unidades_producir['ss_cl']
    u_total_cl = unidades_producir['total_cl']
    
    u_ps_ce = unidades_producir['ps_ce']
    u_ss_ce = unidades_producir['ss_ce']
    u_total_ce = unidades_producir['total_ce']
    
    u_ps_cr = unidades_producir['ps_cr']
    u_ss_cr = unidades_producir['ss_cr']
    u_total_cr = unidades_producir['total_cr']

    # --- Extracción de datos de Horas Requeridas por Unidad (HRU) ---
    hru_cl = req_materiales['CL_HR'] # CL usa MAHR
    hru_ce = req_materiales['CE_HR'] # CE usa MUHR
    hru_cr = req_materiales['CR_HR'] # CR usa MCHR

    # --- Extracción de datos de Cuota por Hora ---
    cuota_ps = datos_mo['cuota_ps']
    cuota_ss = datos_mo['cuota_ss']

    # --- Cálculos Producto CL ---
    thr_ps_cl = u_ps_cl * hru_cl
    thr_ss_cl = u_ss_cl * hru_cl
    thr_total_cl = thr_ps_cl + thr_ss_cl
    
    imp_ps_cl = thr_ps_cl * cuota_ps
    imp_ss_cl = thr_ss_cl * cuota_ss
    imp_total_cl = imp_ps_cl + imp_ss_cl

    # --- Cálculos Producto CE ---
    thr_ps_ce = u_ps_ce * hru_ce
    thr_ss_ce = u_ss_ce * hru_ce
    thr_total_ce = thr_ps_ce + thr_ss_ce
    
    imp_ps_ce = thr_ps_ce * cuota_ps
    imp_ss_ce = thr_ss_ce * cuota_ss
    imp_total_ce = imp_ps_ce + imp_ss_ce

    # --- Cálculos Producto CR ---
    thr_ps_cr = u_ps_cr * hru_cr
    thr_ss_cr = u_ss_cr * hru_cr
    thr_total_cr = thr_ps_cr + thr_ss_cr
    
    imp_ps_cr = thr_ps_cr * cuota_ps
    imp_ss_cr = thr_ss_cr * cuota_ss
    imp_total_cr = imp_ps_cr + imp_ss_cr

    # --- Cálculos de Totales Generales ---
    total_hr_ps = thr_ps_cl + thr_ps_ce + thr_ps_cr
    total_hr_ss = thr_ss_cl + thr_ss_ce + thr_ss_cr
    total_hr_total = thr_total_cl + thr_total_ce + thr_total_cr # <-- Este es el valor que necesitamos
    
    total_mod_ps = imp_ps_cl + imp_ps_ce + imp_ps_cr
    total_mod_ss = imp_ss_cl + imp_ss_ce + imp_ss_cr
    total_mod_total = imp_total_cl + imp_total_ce + imp_total_cr

    # --- Construcción del DataFrame ---
    data = {
        "1er. Semestre": [
            "", # PRODUCTO CL
            u_ps_cl,
            hru_cl,
            thr_ps_cl,
            cuota_ps,
            imp_ps_cl,
            "", # Espacio
            "", # PRODUCTO CE
            u_ps_ce,
            hru_ce,
            thr_ps_ce,
            cuota_ps,
            imp_ps_ce,
            "", # Espacio
            "", # PRODUCTO CR
            u_ps_cr,
            hru_cr,
            thr_ps_cr,
            cuota_ps,
            imp_ps_cr
        ],
        "2do. Semestre": [
            "", # PRODUCTO CL
            u_ss_cl,
            hru_cl,
            thr_ss_cl,
            cuota_ss,
            imp_ss_cl,
            "", # Espacio
            "", # PRODUCTO CE
            u_ss_ce,
            hru_ce,
            thr_ss_ce,
            cuota_ss,
            imp_ss_ce,
            "", # Espacio
            "", # PRODUCTO CR
            u_ss_cr,
            hru_cr,
            thr_ss_cr,
            cuota_ss,
            imp_ss_cr
        ],
        "Total 2016": [
            "", # PRODUCTO CL
            u_total_cl,
            hru_cl,
            thr_total_cl,
            "", # Cuota
            imp_total_cl,
            "", # Espacio
            "", # PRODUCTO CE
            u_total_ce,
            hru_ce,
            thr_total_ce,
            "", # Cuota
            imp_total_ce,
            "", # Espacio
            "", # PRODUCTO CR
            u_total_cr,
            hru_cr,
            thr_total_cr,
            "", # Cuota
            imp_total_cr
        ]
    }

    index = [
        "PRODUCTO CL",
        "Unidades a producir",
        "Horas requeridas por unidad",
        "Total de horas requeridas",
        "Cuota por hora",
        "Importe de M.O.D.",
        " ", # Espaciador
        "PRODUCTO CE",
        "Unidades a producir",
        "Horas requeridas por unidad",
        "Total de horas requeridas",
        "Cuota por hora",
        "Importe de M.O.D.",
        "  ", # Espaciador
        "PRODUCTO CR",
        "Unidades a producir",
        "Horas requeridas por unidad",
        "Total de horas requeridas",
        "Cuota por hora",
        "Importe de M.O.D."
    ]

    df = pd.DataFrame(data, index=index)
    
    # --- Añadir el bloque "Total de Requerimientos" ---
    df.loc["   "] = ["", "", ""] # Espaciador
    df.loc["Total de horas requeridas por semestre"] = [total_hr_ps, total_hr_ss, total_hr_total]
    df.loc["Total de M.O.D. por semestre"] = [total_mod_ps, total_mod_ss, total_mod_total]

    print("\n")
    
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.options.display.float_format = '{:,.2f}'.format

    print(df)
    print("\n")
    
    # --- Crear diccionario de totales de costo para retornar ---
    totales_mod = {
        'mod_ps': total_mod_ps,
        'mod_ss': total_mod_ss,
        'mod_total': total_mod_total
    }
    
    # Retornar una TUPLA con los costos y el total de horas anual
    return (totales_mod, total_hr_total)


def PresupuestoGastosIndirectosFabricacion(datos_gif: dict, total_horas_anual: float):
    """Genera la tabla 8. Presupuesto de Gastos Indirectos de Fabricación (G.I.F.)"""
    print("----- 8. Presupuesto de Gastos Indirectos de Fabricación -----")

    # --- Cálculos de la primera tabla (Gastos) ---
    dep_ps = datos_gif['depreciacion_gf'] / 2
    dep_ss = datos_gif['depreciacion_gf'] / 2
    dep_total = datos_gif['depreciacion_gf']
    
    seg_ps = datos_gif['seguros'] / 2
    seg_ss = datos_gif['seguros'] / 2
    seg_total = datos_gif['seguros']
    
    mant_ps = datos_gif['mantenimiento_ps']
    mant_ss = datos_gif['mantenimiento_ss']
    mant_total = mant_ps + mant_ss
    
    ener_ps = datos_gif['energeticos_ps']
    ener_ss = datos_gif['energeticos_ss']
    ener_total = ener_ps + ener_ss
    
    var_ps = datos_gif['varios_gf'] / 2
    var_ss = datos_gif['varios_gf'] / 2
    var_total = datos_gif['varios_gf']

    total_gif_ps = dep_ps + seg_ps + mant_ps + ener_ps + var_ps
    total_gif_ss = dep_ss + seg_ss + mant_ss + ener_ss + var_ss
    total_gif_total = total_gif_ps + total_gif_ss # <-- Valor que necesitamos retornar
    
    # --- Cálculo para Flujo de Efectivo ---
    total_gif_sin_dep = total_gif_total - dep_total # Total GIF menos depreciación

    # --- Construcción de la primera tabla ---
    data_gastos = {
        "1er. Semestre": [dep_ps, seg_ps, mant_ps, ener_ps, var_ps, total_gif_ps],
        "2do. Semestre": [dep_ss, seg_ss, mant_ss, ener_ss, var_ss, total_gif_ss],
        "Total 2016": [dep_total, seg_total, mant_total, ener_total, var_total, total_gif_total]
    }
    index_gastos = ["Depreciación", "Seguros", "Mantenimiento", "Energéticos", "Varios", "Total G.I.F. por semestre"]
    df_gastos = pd.DataFrame(data_gastos, index=index_gastos)

    # --- Cálculos de la segunda tabla (Coeficiente) ---
    costo_hora_gif = total_gif_total / total_horas_anual

    # --- Construcción de la segunda tabla ---
    data_coef = {
        "1er. Semestre": ["", "", ""],
        "2do. Semestre": ["", "", ""],
        "Total 2016": [total_gif_total, total_horas_anual, costo_hora_gif]
    }
    index_coef = ["Total de G.I.F.", "(/) Total horas M.O.D. Anual", "(=) Costo por Hora de G.I.F."]
    df_coef = pd.DataFrame(data_coef, index=index_coef)

    # --- Unir ambas tablas ---
    df_final = pd.concat([df_gastos, 
                          pd.DataFrame(index=[" "]), # Fila espaciadora
                          df_coef])
    
    df_final = df_final.fillna("")
    
    print("\n")
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.options.display.float_format = '{:,.2f}'.format
    
    print(df_final)
    print("\n")
    
    # Retornar una TUPLA con el coeficiente, el total anual, y el total sin depreciación
    return (costo_hora_gif, total_gif_total, total_gif_sin_dep) 


def PresupuestoGastosDeOperacion(datos_ga: dict, ventas_semestrales: tuple, datos_ad: dict):
    """Genera la tabla 9. Presupuesto de Gastos de Operación (G.A.)"""
    print("----- 9. Presupuesto de Gastos de Operación -----")
    
    # --- Extracción de datos ---
    ventas_ps, ventas_ss = ventas_semestrales
    tasa_comision = datos_ad['tasa_comisiones']
    
    dep_anual = datos_ga['depreciacion']
    sueldos_anual = datos_ga['sueldos']
    interes_anual = datos_ga['intereses']
    
    # --- Cálculos por Semestre ---
    dep_ps = dep_anual / 2
    dep_ss = dep_anual / 2
    dep_total = dep_anual
    
    sueldos_ps = sueldos_anual / 2
    sueldos_ss = sueldos_anual / 2
    sueldos_total = sueldos_anual
    
    comis_ps = ventas_ps * tasa_comision
    comis_ss = ventas_ss * tasa_comision
    comis_total = comis_ps + comis_ss
    
    varios_ps = datos_ga['varios1']
    varios_ss = datos_ga['varios2']
    varios_total = varios_ps + varios_ss
    
    interes_ps = interes_anual / 2
    interes_ss = interes_anual / 2
    interes_total = interes_anual
    
    total_ga_ps = dep_ps + sueldos_ps + comis_ps + varios_ps + interes_ps
    total_ga_ss = dep_ss + sueldos_ss + comis_ss + varios_ss + interes_ss
    total_ga_total = total_ga_ps + total_ga_ss
    
    # --- Cálculo para Flujo de Efectivo ---
    total_ga_sin_dep = total_ga_total - dep_total # Total GA menos depreciación

    # --- Construcción del DataFrame ---
    data = {
        "1er. Semestre": [dep_ps, sueldos_ps, comis_ps, varios_ps, interes_ps, total_ga_ps],
        "2do. Semestre": [dep_ss, sueldos_ss, comis_ss, varios_ss, interes_ss, total_ga_ss],
        "Total 2016": [dep_total, sueldos_total, comis_total, varios_total, interes_total, total_ga_total]
    }
    index = ["Depreciación", "Sueldos y Salarios", "Comisiones", "Varios", "Intereses del Prestamo", "Total de Gastos de Operación:"]
    
    df = pd.DataFrame(data, index=index)
    
    print("\n")
    # Añadir las opciones de display de pandas para evitar el salto de línea
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.options.display.float_format = '{:,.2f}'.format
    print(df)
    print("\n")
    
    # Retornar el total y el total sin depreciación
    return (total_ga_total, total_ga_sin_dep)

# ----- FUNCIÓN MODIFICADA -----
def PresupuestoCostoUnitarioProductosTerminados(datos_costos: dict, datos_req: dict, datos_mo: dict, costo_hora_gif: float):
    """Genera la tabla 10. Determinación del Costo Unitario de Productos Terminados"""
    print("----- 10. Determinación del Costo Unitario de Productos Terminados -----")

    # --- Extracción de Costos (Usamos 2do Semestre según imagen) ---
    costo_a = datos_costos['CSA']
    costo_b = datos_costos['CSB']
    costo_c = datos_costos['CSC']
    costo_mo = datos_mo['cuota_ss']
    costo_gif = costo_hora_gif

    # --- Producto CL ---
    cant_a_cl = datos_req['CL_A']
    cant_b_cl = datos_req['CL_B']
    cant_c_cl = datos_req['CL_C']
    cant_mo_cl = datos_req['CL_HR'] # Cantidad de horas
    
    cu_a_cl = costo_a * cant_a_cl
    cu_b_cl = costo_b * cant_b_cl
    cu_c_cl = costo_c * cant_c_cl
    cu_mo_cl = costo_mo * cant_mo_cl
    cu_gif_cl = costo_gif * cant_mo_cl # GIF se aplica por hora de M.O.D.
    total_cu_cl = cu_a_cl + cu_b_cl + cu_c_cl + cu_mo_cl + cu_gif_cl

    data_cl = {
        'Costo': [costo_a, costo_b, costo_c, costo_mo, costo_gif, ""],
        'Cantidad': [cant_a_cl, cant_b_cl, cant_c_cl, cant_mo_cl, cant_mo_cl, ""],
        'Costo Unitario': [cu_a_cl, cu_b_cl, cu_c_cl, cu_mo_cl, cu_gif_cl, total_cu_cl]
    }
    index_base = ['Material A', 'Material B', 'Material C', 'Mano de Obra', 'Gastos Indirectos de Fabricación', 'Costo Unitario']
    df_cl = pd.DataFrame(data_cl, index=index_base)
    df_cl_title = pd.DataFrame(index=["PRODUCTO CL"]) # Título como fila

    # --- Producto CE ---
    cant_a_ce = datos_req['CE_A']
    cant_b_ce = datos_req['CE_B']
    cant_c_ce = datos_req['CE_C']
    cant_mo_ce = datos_req['CE_HR']
    
    cu_a_ce = costo_a * cant_a_ce
    cu_b_ce = costo_b * cant_b_ce
    cu_c_ce = costo_c * cant_c_ce
    cu_mo_ce = costo_mo * cant_mo_ce
    cu_gif_ce = costo_gif * cant_mo_ce
    total_cu_ce = cu_a_ce + cu_b_ce + cu_c_ce + cu_mo_ce + cu_gif_ce

    data_ce = {
        'Costo': [costo_a, costo_b, costo_c, costo_mo, costo_gif, ""],
        'Cantidad': [cant_a_ce, cant_b_ce, cant_c_ce, cant_mo_ce, cant_mo_ce, ""],
        'Costo Unitario': [cu_a_ce, cu_b_ce, cu_c_ce, cu_mo_ce, cu_gif_ce, total_cu_ce]
    }
    df_ce = pd.DataFrame(data_ce, index=index_base)
    df_ce_title = pd.DataFrame(index=["PRODUCTO CE"])

    # --- Producto CR ---
    cant_a_cr = datos_req['CR_A']
    cant_b_cr = datos_req['CR_B']
    cant_c_cr = datos_req['CR_C']
    cant_mo_cr = datos_req['CR_HR']
    
    cu_a_cr = costo_a * cant_a_cr
    cu_b_cr = costo_b * cant_b_cr
    cu_c_cr = costo_c * cant_c_cr
    cu_mo_cr = costo_mo * cant_mo_cr
    cu_gif_cr = costo_gif * cant_mo_cr
    total_cu_cr = cu_a_cr + cu_b_cr + cu_c_cr + cu_mo_cr + cu_gif_cr

    data_cr = {
        'Costo': [costo_a, costo_b, costo_c, costo_mo, costo_gif, ""],
        'Cantidad': [cant_a_cr, cant_b_cr, cant_c_cr, cant_mo_cr, cant_mo_cr, ""],
        'Costo Unitario': [cu_a_cr, cu_b_cr, cu_c_cr, cu_mo_cr, cu_gif_cr, total_cu_cr]
    }
    df_cr = pd.DataFrame(data_cr, index=index_base)
    df_cr_title = pd.DataFrame(index=["PRODUCTO CR"])
    
    # --- Unir todas las tablas ---
    df_final = pd.concat([
        df_cl_title, df_cl,
        pd.DataFrame(index=[" "]), # Espaciador
        df_ce_title, df_ce,
        pd.DataFrame(index=["  "]), # Espaciador
        df_cr_title, df_cr
    ]).fillna("") # Reemplazar NaN por ""
    
    print("\n")
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.options.display.float_format = '{:,.2f}'.format
    
    print(df_final)
    print("\n")
    
    # Retornar los costos unitarios para la siguiente tabla
    return {
        'cu_cl': total_cu_cl,
        'cu_ce': total_cu_ce,
        'cu_cr': total_cu_cr
    }

# ----- FUNCIÓN MODIFICADA -----
def ValuacionInventariosFinales(datos_inv: dict, datos_costos: dict, costos_unitarios: dict):
    """Genera la tabla 11. Valuación de Inventarios Finales"""
    print("----- 11. Valuación de Inventarios Finales -----")

    # --- Cálculos Tabla 1: Inventario Final de Materiales ---
    unidades_a = datos_inv['IIFSA']
    unidades_b = datos_inv['IIFSB']
    unidades_c = datos_inv['IIFSC']
    
    costo_a = datos_costos['CSA']
    costo_b = datos_costos['CSB']
    costo_c = datos_costos['CSC']
    
    total_a = unidades_a * costo_a
    total_b = unidades_b * costo_b
    total_c = unidades_c * costo_c
    total_materiales = total_a + total_b + total_c
    
    data_mat = {
        'Unidades': [unidades_a, unidades_b, unidades_c, ""],
        'Costo Unitario': [costo_a, costo_b, costo_c, ""],
        'Costo Total': [total_a, total_b, total_c, total_materiales]
    }
    index_mat = ['Material A', 'Material B', 'Material C', 'Inventario Final de Materiales']
    df_materiales_title = pd.DataFrame(index=["Inventario Final de Materiales"])
    df_materiales = pd.DataFrame(data_mat, index=index_mat)

    # --- Cálculos Tabla 2: Inventario Final de Producto Terminado ---
    unidades_cl = datos_inv['IIF_CL']
    unidades_ce = datos_inv['IIF_CE']
    unidades_cr = datos_inv['IIF_CR']
    
    costo_cl = costos_unitarios['cu_cl']
    costo_ce = costos_unitarios['cu_ce']
    costo_cr = costos_unitarios['cu_cr']
    
    total_cl = unidades_cl * costo_cl
    total_ce = unidades_ce * costo_ce
    total_cr = unidades_cr * costo_cr
    total_prod_terminado = total_cl + total_ce + total_cr
    
    data_pt = {
        'Unidades': [unidades_cl, unidades_ce, unidades_cr, ""],
        'Costo Unitario': [costo_cl, costo_ce, costo_cr, ""],
        'Costo Total': [total_cl, total_ce, total_cr, total_prod_terminado]
    }
    index_pt = ['Producto CL', 'Producto CE', 'Producto CR', 'Inventario Final de Producto Terminado']
    df_prod_term_title = pd.DataFrame(index=["Inventario Final de Producto Terminado"])
    df_prod_term = pd.DataFrame(data_pt, index=index_pt)

    # --- Unir todas las tablas ---
    df_final = pd.concat([
        df_materiales_title, df_materiales,
        pd.DataFrame(index=[" "]), # Espaciador
        df_prod_term_title, df_prod_term
    ]).fillna("") # Reemplazar NaN por ""
    
    print("\n")
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.options.display.float_format = '{:,.2f}'.format
    
    print(df_final)
    print("\n")
    
    # Retornar los dos totales para el Balance General
    return (total_materiales, total_prod_terminado)


def EstadoCostoProduccionVentas(inv_ini_mat, compras_total, inv_final_mat, mod_total, gif_total, inv_ini_pt, inv_final_pt):
    """Genera la tabla 12. Estado de Costo de Producción y Ventas"""
    print("----- 12. Estado de Costo de Producción y Ventas -----")
    
    # --- Cálculos ---
    mat_disponible = inv_ini_mat + compras_total
    mat_utilizados = mat_disponible - inv_final_mat
    costo_produccion = mat_utilizados + mod_total + gif_total
    total_prod_disponible = costo_produccion + inv_ini_pt
    costo_de_ventas = total_prod_disponible - inv_final_pt

    # --- Construcción del DataFrame ---
    data = {
        "Importe": [
            "", # Saldo Inicial de Materiales
            "", # (+) Compras de Materiales
            "", # (=) Material Disponible
            "", # (-) Inventario Final de Materiales
            "", # (=) Materiales Utilizados
            "", # (+) Mano de Obra Directa
            "", # (+) Gastos de Fabricación Indirectos
            "", # (=) Costo de Producción
            "", # (+) Inventario Inicial de Productos Terminados
            "", # (=) Total de Producción Disponible
            "", # (-) Inventario Final de Productos Terminados
            ""  # (=) Costo de Ventas
        ],
        "Total": [
            inv_ini_mat,
            compras_total,
            mat_disponible,
            inv_final_mat,
            mat_utilizados,
            mod_total,
            gif_total,
            costo_produccion,
            inv_ini_pt,
            total_prod_disponible,
            inv_final_pt,
            costo_de_ventas
        ]
    }
    
    index = [
        "Saldo Inicial de Materiales",
        "(+) Compras de Materiales",
        "(=) Material Disponible",
        "(-) Inventario Final de Materiales",
        "(=) Materiales Utilizados",
        "(+) Mano de Obra Directa",
        "(+) Gastos de Fabricación Indirectos",
        "(=) Costo de Producción",
        "(+) Inventario Inicial de Productos Terminados",
        "(=) Total de Producción Disponible",
        "(-) Inventario Final de Productos Terminados",
        "(=) Costo de Ventas"
    ]
    
    df = pd.DataFrame(data, index=index).fillna("") # Rellenar vacíos
    
    print("\n")
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    
    # --- CORRECCIÓN AÑADIDA ---
    pd.options.display.float_format = '{:,.2f}'.format
    
    print(df)
    print("\n")
    
    return costo_de_ventas # Retornar el valor final


def EstadoDeResultados(total_ventas, costo_ventas, gastos_op, datos_ad):
    """Genera la tabla 13. Estado de Resultados"""
    print("----- 13. Estado de Resultados -----")
    
    # --- Extracción de tasas ---
    tasa_isr = datos_ad['tasa_isr']
    tasa_ptu = datos_ad['tasa_ptu']
    
    # --- Cálculos ---
    utilidad_bruta = total_ventas - costo_ventas
    utilidad_operacion = utilidad_bruta - gastos_op
    isr = utilidad_operacion * tasa_isr # <-- Valor que necesitamos
    ptu = utilidad_operacion * tasa_ptu # <-- Valor que necesitamos
    utilidad_neta = utilidad_operacion - isr - ptu

    # --- Construcción del DataFrame ---
    data = {
        "Importe": ["", "", "", "", "", "", "", ""],
        "Total": [
            total_ventas,
            costo_ventas,
            utilidad_bruta,
            gastos_op,
            utilidad_operacion,
            isr,
            ptu,
            utilidad_neta
        ]
    }
    
    index = [
        "Ventas",
        "(-) Costo de Ventas",
        "(=) Utilidad Bruta",
        "(-) Gastos de Operación",
        "(=) Utilidad de Operación",
        "(-) ISR",
        "(-) PTU",
        "(=) Utilidad Neta"
    ]
    
    df = pd.DataFrame(data, index=index).fillna("") # Rellenar vacíos
    
    print("\n")
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.options.display.float_format = '{:,.2f}'.format
    
    print(df)
    print("\n")
    
    # Retornar la utilidad neta, ISR y PTU a pagar
    return (utilidad_neta, isr, ptu)


def EstadoFlujoEfectivo(efectivo_ini, cob_2015, cob_2016, pago_prov_2015, pago_prov_2016, 
                       pago_mod, pago_gif_sin_dep, pago_ga_sin_dep, 
                       compra_activo, pago_isr_2015, pago_isr_2016):
    """Genera la tabla 14. Estado de Flujo de Efectivo"""
    print("----- 14. Estado de Flujo de Efectivo -----")

    # --- Cálculos de Entradas ---
    total_entradas = cob_2015 + cob_2016
    efectivo_disponible = efectivo_ini + total_entradas

    # --- Cálculos de Salidas ---
    total_salidas = (
        pago_prov_2015 + pago_prov_2016 + pago_mod + 
        pago_gif_sin_dep + pago_ga_sin_dep + 
        compra_activo + pago_isr_2015 + pago_isr_2016 # pago_isr_2016 será 0
    )
    
    # --- Cálculo Final ---
    flujo_efectivo_actual = efectivo_disponible - total_salidas
    
    # --- Construcción del DataFrame ---
    data = {
        "Importe": [
            "", # Saldo Inicial
            "", # Entradas:
            cob_2016,
            cob_2015,
            "", # Total de Entradas
            "", # Efectivo Disponible
            "", # Salidas:
            pago_prov_2016,
            pago_prov_2015,
            pago_mod,
            pago_gif_sin_dep,
            pago_ga_sin_dep,
            compra_activo,
            pago_isr_2015,
            pago_isr_2016, # <-- Esto mostrará 0.00
            "", # Total de Salidas
            ""  # Flujo de Efectivo Actual
        ],
        "Total": [
            efectivo_ini,
            "", # Entradas:
            "",
            "",
            total_entradas,
            efectivo_disponible,
            "", # Salidas:
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            total_salidas,
            flujo_efectivo_actual
        ]
    }
    
    index = [
        "Saldo Inicial de Efectivo",
        "Entradas:",
        "Cobranza 2016",
        "Cobranza 2015",
        "Total de Entradas",
        "Efectivo Disponible",
        "Salidas:",
        "Proveedores 2016",
        "Proveedores 2015",
        "Pago Mano de Obra Directa",
        "Pago Gastos Indirectos de Fabricación",
        "Pago de Gastos de Operación",
        "Compra de Activo Fijo (Maquinaria)",
        "Pago ISR 2015",
        "Pago ISR 2016",
        "Total de Salidas",
        "Flujo de Efectivo Actual"
    ]
    
    df = pd.DataFrame(data, index=index).fillna("") # Rellenar vacíos
    
    print("\n")
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.options.display.float_format = '{:,.2f}'.format
    
    print(df)
    print("\n")
    
    return flujo_efectivo_actual


# ----- NUEVA FUNCIÓN AÑADIDA -----
def BalanceGeneralPresupuestado(b_ini: dict, estado_app: dict):
    """Genera la tabla 15. Balance General Presupuestado al 31 de Dic de 2016"""
    print("----- 15. Balance General Presupuestado (Final) -----")

    # --- Cálculos de Activo Circulante ---
    efectivo = estado_app['flujo_efectivo_final']
    clientes = estado_app['saldo_final_clientes']
    deudores = b_ini.get('Deudores Diversos', 0)
    funcionarios = b_ini.get('Funcionarios y Empleados', 0)
    inv_mat = estado_app['total_inv_final_materiales']
    inv_pt = estado_app['total_inv_final_prod_terminado']
    total_circulante = efectivo + clientes + deudores + funcionarios + inv_mat + inv_pt
    
    # --- Cálculos de Activo No Circulante ---
    terreno = b_ini.get('Terreno', 0)
    planta_eq_ini = b_ini.get('Planta y Equipo', 0)
    compra_activo = estado_app['datos_adicionales'].get('equipo_nuevo', 0)
    planta_eq_final = planta_eq_ini + compra_activo
    
    dep_acum_ini = b_ini.get('Depreciacion Acumulada', 0)
    dep_ga = estado_app['datos_ga'].get('depreciacion', 0)
    dep_gif = estado_app['datos_gif'].get('depreciacion_gf', 0)
    dep_acum_final = dep_acum_ini + dep_ga + dep_gif
    
    total_no_circulante = terreno + planta_eq_final - dep_acum_final
    total_activo = total_circulante + total_no_circulante
    
    # --- Cálculos de Pasivo Corto Plazo ---
    proveedores = estado_app['saldo_final_proveedores']
    doc_pagar = b_ini.get('Documentos por Pagar', 0)
    isr_pagar = estado_app['isr_calculado_2016']
    ptu_pagar = estado_app['ptu_por_pagar']
    total_pasivo_cp = proveedores + doc_pagar + isr_pagar + ptu_pagar
    
    # --- Cálculos de Pasivo Largo Plazo ---
    prestamos_lp = b_ini.get('Préstamos Bancarios', 0)
    total_pasivo_lp = prestamos_lp
    
    pasivo_total = total_pasivo_cp + total_pasivo_lp
    
    # --- Cálculos de Capital Contable ---
    cap_contribuido = b_ini.get('Capital Contribuido', 0)
    cap_ganado = b_ini.get('Capital Ganado', 0)
    utilidad_ejercicio = estado_app['utilidad_neta']
    total_capital = cap_contribuido + cap_ganado + utilidad_ejercicio
    
    # --- Suma Final ---
    suma_pasivo_capital = pasivo_total + total_capital
    
    # --- Construcción del DataFrame ---
    data = {
        "ACTIVO": ["Circulante", "Efectivo", "Clientes", "Deudores Diversos", "Funcionarios y Empleados",
                   "Inventario de Materiales", "Inventario de Producto Terminado", "Total de Activos Circulantes",
                   "", "No Circulante", "Terreno", "Planta y Equipo", "Depreciacion Acumulada", "Total Activos No Circulantes",
                   "ACTIVO TOTAL", "", "PASIVO", "Corto Plazo", "Proveedores", "Documentos por Pagar", "ISR por Pagar", "PTU por Pagar",
                   "Total de Pasivo Corto Plazo", "", "Largo Plazo", "Préstamos Bancarios", "Total de Pasivo Largo Plazo",
                   "PASIVO TOTAL", "", "CAPITAL CONTABLE", "Capital Contribuido", "Capital Ganado", "Utilidad del Ejercicio",
                   "Total de Capital Contable", "", "SUMA DE PASIVO Y CAPITAL"],
        "Importe": ["", efectivo, clientes, deudores, funcionarios, inv_mat, inv_pt, "",
                    "", "", terreno, planta_eq_final, -dep_acum_final, "",
                    "", "", "", "", proveedores, doc_pagar, isr_pagar, ptu_pagar,
                    "", "", "", prestamos_lp, "",
                    "", "", "", cap_contribuido, cap_ganado, utilidad_ejercicio,
                    "", "", ""],
        "Total": ["", "", "", "", "", "", "", total_circulante,
                  "", "", "", "", "", total_no_circulante,
                  total_activo, "", "", "", "", "", "", "",
                  total_pasivo_cp, "", "", "", total_pasivo_lp,
                  pasivo_total, "", "", "", "", "",
                  total_capital, "", suma_pasivo_capital]
    }
    
    df = pd.DataFrame(data).fillna("") # Rellenar vacíos
    
    print("\n")
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.options.display.float_format = '{:,.2f}'.format
    
    print(df)
    print("\n")
    
    # --- Verificación Final ---
    if abs(total_activo - suma_pasivo_capital) < 0.01:
        print("¡ÉXITO! El Balance General Presupuestado está CUADRADO.")
    else:
        diferencia = total_activo - suma_pasivo_capital
        print(f"¡ERROR! El Balance NO CUADRA. Diferencia: {diferencia:,.2f}")


# ----- Main() MODIFICADA -----

def main():
    # Cargar datos guardados al iniciar (o crear un estado vacío)
    estado_app = cargar_datos()
    
    while(True):
        print("\n--- MENÚ PRINCIPAL DEL PRESUPUESTO MAESTRO ---")
        print("1.- Ingresar/Actualizar Balance General Inicial")
        print("2.- Ingresar/Actualizar Redacción (Datos de Producción)")
        print("3.- Datos Adicionales") 
        print("4.- Generar Presupuesto Maestro Completo (SECUENCIAL)")
        print("5.- Salir")
        
        try:
            opcion = int(input("Seleccione una opcion: "))

            if opcion == 1:
                # --- MODIFICADO ---
                balance_inicial = BalanceGeneral()
                estado_app['balance_inicial'] = balance_inicial
                
                # Extraer valores clave para otras funciones (por compatibilidad)
                estado_app['clientes'] = balance_inicial.get('Clientes', 0)
                estado_app['proveedores'] = balance_inicial.get('Proveedores', 0)
                estado_app['inv_ini_materiales'] = balance_inicial.get('Inventario de Materiales', 0)
                estado_app['inv_ini_prod_terminado'] = balance_inicial.get('Inventario de Productos Terminados', 0)
                estado_app['efectivo_inicial'] = balance_inicial.get('Efectivo', 0)
                estado_app['isr_por_pagar_2015'] = balance_inicial.get('ISR por Pagar', 0)
                
                guardar_datos(estado_app)

            elif opcion == 2:
                # Ejecuta la función y desempaca los 7 diccionarios
                (dp, di, dr, dc, dm, dgif, dga) = Redaccion()
                # Actualiza el estado con los nuevos diccionarios
                estado_app.update({
                    'datos_productos': dp,
                    'datos_inventario': di,
                    'datos_requerimientos': dr,
                    'datos_costos': dc,
                    'datos_mano_obra': dm,
                    'datos_gif': dgif, 
                    'datos_ga': dga 
                })
                guardar_datos(estado_app)

            elif opcion == 3: 
                # Llama a la nueva función y guarda su resultado
                estado_app['datos_adicionales'] = DatosAdicionales()
                guardar_datos(estado_app)

            elif opcion == 4: 
                # --- EJECUCIÓN SECUENCIAL ---
                print("\n\n>>> INICIANDO CÁLCULO DEL PRESUPUESTO MAESTRO COMPLETO <<<")
                
                # Paso 1: Verificar que tengamos todos los datos necesarios
                if (not estado_app.get('balance_inicial') or # Chequeo principal
                    not estado_app.get('datos_productos') or 
                    not estado_app.get('datos_inventario') or 
                    not estado_app.get('datos_requerimientos') or 
                    not estado_app.get('datos_costos') or
                    not estado_app.get('datos_adicionales') or
                    not estado_app.get('datos_mano_obra') or
                    not estado_app.get('datos_gif') or
                    not estado_app.get('datos_ga')): 
                    
                    print("\n[ERROR] Faltan datos. Asegúrese de haber completado las Opciones 1, 2 y 3.")
                    continue # Vuelve al menú principal

                # Si tenemos datos, procedemos en orden
                try:
                    # 1. Presupuesto de Ventas
                    ventas_sem_1, ventas_sem_2, total_ventas_anual = PresupuestoVentas(estado_app['datos_productos'])
                    estado_app['ventas_semestrales'] = (ventas_sem_1, ventas_sem_2) 
                    
                    # 2. Saldo de Clientes
                    (cobranza_2015, cobranza_2016, 
                     saldo_clientes_final) = SaldoClientesyFlujoDeEntradas(
                        estado_app['balance_inicial']['Clientes'], total_ventas_anual, estado_app['datos_adicionales']
                    )
                    estado_app['cobranza_2015'] = cobranza_2015
                    estado_app['cobranza_2016'] = cobranza_2016
                    estado_app['saldo_final_clientes'] = saldo_clientes_final 
                    
                    # 3. Presupuesto de Producción
                    unidades_a_producir = PresupuestoDeProduccion(estado_app['datos_productos'], estado_app['datos_inventario'])
                    
                    # 4. Presupuesto de Requerimientos
                    total_requerimientos = PresupuestodeRequerimientosdeMateriales(unidades_a_producir, estado_app['datos_requerimientos'])
                    
                    # 5. Presupuesto de Compras
                    compras_2016 = PresupuestodeComprasdeMateriales(total_requerimientos, estado_app['datos_inventario'], estado_app['datos_costos'])
                    
                    # 6. Saldo de Proveedores
                    (pago_prov_2015, pago_prov_2016, 
                     saldo_prov_final) = TotaldeproveedoresyFlujodeSalidas(
                        estado_app['balance_inicial']['Proveedores'], compras_2016, estado_app['datos_adicionales']
                    )
                    estado_app['pago_prov_2015'] = pago_prov_2015
                    estado_app['pago_prov_2016'] = pago_prov_2016
                    estado_app['saldo_final_proveedores'] = saldo_prov_final 

                    # 7. Presupuesto de Mano de Obra
                    totales_mod, total_horas_mod_anual = PresupuestoManoDeObraDirecta(
                        unidades_a_producir, 
                        estado_app['datos_requerimientos'], 
                        estado_app['datos_mano_obra']
                    )
                    estado_app['totales_mod'] = totales_mod
                    estado_app['total_horas_mod_anual'] = total_horas_mod_anual 
                    
                    # 8. Presupuesto de G.I.F.
                    (costo_hora_gif, 
                     total_gif_anual, 
                     total_gif_sin_dep) = PresupuestoGastosIndirectosFabricacion(
                        estado_app['datos_gif'],
                        estado_app['total_horas_mod_anual']
                    )
                    estado_app['costo_hora_gif'] = costo_hora_gif 
                    estado_app['total_gif_anual'] = total_gif_anual 
                    estado_app['total_gif_sin_dep'] = total_gif_sin_dep 
                    
                    # 9. Presupuesto de Gastos de Operación
                    total_ga_total, total_ga_sin_dep = PresupuestoGastosDeOperacion(
                        estado_app['datos_ga'],
                        estado_app['ventas_semestrales'],
                        estado_app['datos_adicionales']
                    )
                    estado_app['total_ga_total'] = total_ga_total 
                    estado_app['total_ga_sin_dep'] = total_ga_sin_dep 

                    # 10. Costo Unitario de Productos Terminados
                    costos_unitarios = PresupuestoCostoUnitarioProductosTerminados(
                        estado_app['datos_costos'],
                        estado_app['datos_requerimientos'],
                        estado_app['datos_mano_obra'],
                        estado_app['costo_hora_gif']
                    )
                    estado_app['costos_unitarios'] = costos_unitarios 
                    
                    # 11. Valuación de Inventarios Finales
                    total_mat, total_pt = ValuacionInventariosFinales(
                        estado_app['datos_inventario'],
                        estado_app['datos_costos'],
                        estado_app['costos_unitarios']
                    )
                    estado_app['total_inv_final_materiales'] = total_mat
                    estado_app['total_inv_final_prod_terminado'] = total_pt

                    # 12. Estado de Costo de Producción y Ventas 
                    costo_de_ventas = EstadoCostoProduccionVentas(
                        estado_app['balance_inicial']['Inventario de Materiales'],
                        compras_2016, 
                        estado_app['total_inv_final_materiales'], 
                        estado_app['totales_mod']['mod_total'], 
                        estado_app['total_gif_anual'], 
                        estado_app['balance_inicial']['Inventario de Productos Terminados'],
                        estado_app['total_inv_final_prod_terminado'] 
                    )
                    estado_app['costo_de_ventas'] = costo_de_ventas
                    
                    # 13. Estado de Resultados
                    utilidad_neta, isr_2016, ptu_2016 = EstadoDeResultados(
                        total_ventas_anual,
                        estado_app['costo_de_ventas'],
                        estado_app['total_ga_total'],
                        estado_app['datos_adicionales']
                    )
                    estado_app['utilidad_neta'] = utilidad_neta
                    estado_app['isr_calculado_2016'] = isr_2016 
                    estado_app['ptu_por_pagar'] = ptu_2016 
                    
                    # Verificar si se paga el ISR 2015
                    pago_isr_2015_monto = 0.0
                    if estado_app['datos_adicionales']['pago_isr_2015'] == 'S':
                        pago_isr_2015_monto = estado_app['balance_inicial']['ISR por Pagar']
                    
                    # 14. Estado de Flujo de Efectivo
                    flujo_final = EstadoFlujoEfectivo(
                        estado_app['balance_inicial']['Efectivo'],
                        estado_app['cobranza_2015'],
                        estado_app['cobranza_2016'],
                        estado_app['pago_prov_2015'],
                        estado_app['pago_prov_2016'],
                        estado_app['totales_mod']['mod_total'],
                        estado_app['total_gif_sin_dep'],
                        estado_app['total_ga_sin_dep'],
                        estado_app['datos_adicionales']['equipo_nuevo'],
                        pago_isr_2015_monto,  
                        0.0 # Pago ISR 2016 es 0
                    )
                    estado_app['flujo_efectivo_final'] = flujo_final
                    
                    # 15. Balance General Presupuestado
                    BalanceGeneralPresupuestado(
                        estado_app['balance_inicial'],
                        estado_app
                    )

                    guardar_datos(estado_app) # Guardar todos los nuevos resultados

                    print(">>> PRESUPUESTO MAESTRO COMPLETO GENERADO EXITOSAMENTE <<<\n")
                
                except KeyError as e:
                    print(f"\n[ERROR DE CÁLCULO] Falta un dato clave: {e}. Revise la 'Redacción' (Opción 2) o 'Balance' (Opción 1).")
                except Exception as e:
                    print(f"\n[ERROR DE CÁLCULO] Ocurrió un error inesperado: {e}")

            elif opcion == 5:
                print("Saliendo del programa...")
                break
            
            else:
                print("Opción no válida. Intente de nuevo.")

        except ValueError:
            print("\nError: Debe ingresar un número válido para la opción del menú.")
        except Exception as e:
            print(f"\nError inesperado en el menú: {e}")

if __name__ == "__main__":
    main()