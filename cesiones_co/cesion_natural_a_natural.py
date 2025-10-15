from docxtpl import DocxTemplate
from datetime import date
from pathlib import Path

#Función para formato de fechas
def fecha(d: date )->str:
    meses =["enero","febrero","marzo","abril","mayo","junio",
            "julio","agosto","septiembre","octubre","noviembre","diciembre"]
    return f"{d.day} de {meses[d.month-1]} de {d.year}"


def generar_cesion_natural_a_natural():
    #ruta
    plantilla = Path("plantillas/colombia/Plantilla_cesión_Natural_a_Natural.docx")
    #Palabras a rellenar

    print(f"{"*"*10}Cesión Personas fisicas{"*"*10}")
    #cedente
    nombre_cedente = input("Ingrese nombre cedente: ")
    cedula_cedente = input("Ingrese cedula cedente: ")
    ciudad_cedente = input("Ingrese ciudad cedente: ")

    #cesionario
    nombre_cesionario = input("Ingrese nombre cesionario: ")
    cedula_cesionario = input("Ingrese cedula cesionario: ")
    ciudad_cesionario = input("Ingrese ciudad cesionario: ")

    #fecha acuerdo principal

    fecha_contrato = input("Ingrese fecha contrato principal: ")


    #datos bancarios

    tipo_cuenta = input("Ingrese tipo de cuenta: ")
    numero_cuenta = input("Ingrese número de cuenta: ")
    banco = input("Ingrese nombre del banco: ")

    #nombre del archivo

    nombre_archivo = f"Acta cesión. Rappi-{nombre_cesionario}-{fecha(date.today())}.docx"

    salida = Path("salidas/colombia/")/ nombre_archivo

    #datos plantilla

    contexto = {
        "NOMBRE_CEDENTE": nombre_cedente,
        "CEDULA_CEDENTE": cedula_cedente,
        "CIUDAD_CEDENTE": ciudad_cedente,
        "NOMBRE_CESIONARIO":nombre_cesionario,
        "CEDULA_CESIONARIO":cedula_cesionario,
        "CIUDAD_CESIONARIO":ciudad_cesionario,
        "FECHA_ACUERDO_P":fecha_contrato,
        "TIPO_DE_CUENTA": tipo_cuenta,
        "NUMERO_DE_CUENTA": numero_cuenta,
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
    generar_cesion_natural_a_natural()



