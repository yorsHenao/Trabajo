from docxtpl import DocxTemplate
from datetime import date
from pathlib import Path

def fecha(d: date )->str:
    meses =["enero","febrero","marzo","abril","mayo","junio",
            "julio","agosto","septiembre","octubre","noviembre","diciembre"]
    return f"{d.day} de {meses[d.month-1]} de {d.year}"

def generar_cesion_moral_a_fisica():
    #ruta
    plantilla = Path("plantillas/mexico/cesion_moral_a_fisica_mx.docx")

#palabras a rellenar

    print(f"\n{"*"*10}Cesión Personas moral a fisica{"*"*10}\n")

    #contrato antiguo o nuevo

    respuesta = input("¿Incluimos la clásula cuarta? (si/no): ").strip().lower()
    
    incluir_clausula = respuesta == "si"


    #clausula de pago

    nombre_clausula = input("Ingresa nombre de la cláusula (forma de pago o Contraprestacion): ").strip().lower()

    #cedente
    nombre_cedente = input("Ingrese razón social cedente: ")
    nombre_rl_cedente =input("Ingrese nombre representante legal cedente: ")
    domicilio_cedente = input("Ingrese dirección cedente: ")
    correo_cedente = input("Ingrese correo cedente: ")

    #cesionario
    nombre_cesionario = input("Ingrese nombre cesionario: ")
    rfc_cesionario = input("Ingrese RFC cesionario: ")
    domicilio_cesionario = input("Ingrese dirección cesionario: ")
    correo_cesionario = input("Ingrese correo cesionario: ")
    marca = input("Ingrese marca: ")

    #fecha acuerdo principal

    fecha_contrato = input("Ingrese fecha contrato principal: ")

    #datos bancarios

    numero_cuenta = input("Ingrese numero de cuenta: ")
    numero_clabe_interbancaria = input("Ingrese número clabe interbancaria: ")
    banco = input("Ingrese nombre del banco: ")

    #nombre del archivo

    nombre_archivo = f"Cesion de derechos. Rappi-{nombre_cesionario}-{fecha(date.today())}.docx"

    salida = Path("salidas/mexico/")/ nombre_archivo

    contexto = {
        "RS_CEDENTE": nombre_cedente,
        "RL_CEDENTE": nombre_rl_cedente,
        "DOMICILIO_CEDENTE": domicilio_cedente,
        "CORREO_CEDENTE": correo_cedente,
        
        "NOMBRE_CESIONARIO": nombre_cesionario,
        "RFC_CESIONARIO": rfc_cesionario,
        "DOMICILIO_CESIONARIO": domicilio_cesionario,
        "CORREO_CESIONARIO": correo_cesionario,
        "MARCA": marca,
        "NOMBRE_CLAUSULA": nombre_clausula,
        "incluir_clausula_cuarta": incluir_clausula,


        "FECHA_ACUERDO_P":fecha_contrato,
        "NUMERO_CUENTA": numero_cuenta,
        "CLABE_INTERBANCARIA": numero_clabe_interbancaria,
        "BANCO": banco,
        "FECHA": fecha(date.today()),
    }

    #rellenar plantilla
    docx = DocxTemplate(plantilla)
    docx.render(contexto)
    docx.save(salida)

    print(f"Documento generado \n")
    print("*"*20)

if __name__ == "__main__":
    generar_cesion_moral_a_fisica()