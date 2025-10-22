from docxtpl import DocxTemplate
from datetime import date
from pathlib import Path

def fecha(d: date )->str:
    meses =["enero","febrero","marzo","abril","mayo","junio",
            "julio","agosto","septiembre","octubre","noviembre","diciembre"]
    return f"{d.day} de {meses[d.month-1]} de {d.year}"


def generar_cesion_fisica_a_fisica_arg():
    #ruta
    plantilla = Path("plantillas/argentina/acta_cesion_natural_natural_arg.docx")

#palabras a rellenar

    print(f"\n{"*"*10}Cesión Personas fisicas{"*"*10}\n")


    #cedente
    nombre_cedente = input("Ingrese nombre cedente: ")
    cuit_cedente = input("Ingrese Cuit cedente: ")
    cuit_cedente_f = f"{cuit_cedente[:2]}-{cuit_cedente[2:-1]}-{cuit_cedente[-1]}"
    

    #cesionario
    nombre_cesionario = input("Ingrese nombre cesionario: ")
    cuit_cesionario = input("Ingrese cuit cesionario: ")
    cuit_cesionario_f = f"{cuit_cesionario[:2]}-{cuit_cesionario[2:-1]}-{cuit_cesionario[-1]}"

    #fecha acuerdo principal

    fecha_contrato = input("Ingrese fecha contrato principal: ")

    #años actas
    añoAnterior = input("Ingrese año oferta anterior: ")
    añoActual = input("Ingrese año oferta actual: ")

    #datos bancarios

    numero_cuenta = input("Ingrese numero de cuenta: ")
    numero_cbu = input("Ingrese número cbu: ")
    banco = input("Ingrese nombre del banco: ")

    #nombre del archivo

    nombre_archivo = f"Acta Cesion de derechos. Rappi-{nombre_cesionario}-{fecha(date.today())}.docx"

    salida = Path("salidas/argentina/")/ nombre_archivo

    contexto = {
        "NOMBRE_CEDENTE": nombre_cedente,
        "CUIT_CEDENTE": cuit_cedente_f,
        
        "NOMBRE_CESIONARIO": nombre_cesionario,
        "CUIT_CESIONARIO": cuit_cesionario_f,

        "N_CESION_ANTIGUA":añoAnterior,
        "N_CESION": añoActual,

        "N_OFERTA_INICIAL":fecha_contrato,
        "NUMERO_CUENTA": numero_cuenta,
        "NUMERO_CUENTA": numero_cuenta,
        "CBU": numero_cbu,
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
    generar_cesion_fisica_a_fisica_arg()





