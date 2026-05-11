from docxtpl import DocxTemplate
from datetime import date
from pathlib import Path

def fecha(d: date )->str:
    meses =["enero","febrero","marzo","abril","mayo","junio",
            "julio","agosto","septiembre","octubre","noviembre","diciembre"]
    return f"{d.day} de {meses[d.month-1]} de {d.year}"


def generar_cesion_fisica_a_fisica_chile():
    #ruta
    plantilla = Path("Plantillas/chile/formato_cesión_fisica_a_fisica_chile.docx")

    print(f"\n{"*"*10}Cesión Persona física a Persona física{"*"*10}\n")

    #cedente fisico
    nombre_cedente = input("Ingrese nombre cedente: ")
    cedula_cedente = input("Ingrese cédula cedente: ")
    rut_cedente = input("Ingrese RUT cedente: ")
    rut_cedente_f = f"{rut_cedente[:-1]}-{rut_cedente[-1]}"
    domicilio_cedente = input("Ingrese domicilio cedente: ")
    correo_cedente = input("Ingrese correo cedente: ")

    #cesionario fisico
    nombre_cesionario = input("Ingrese nombre cesionario: ")
    cedula_cesionario = input("Ingrese cédula cesionario: ")
    rut_cesionario = input("Ingrese RUT cesionario: ")
    rut_cesionario_f = f"{rut_cesionario[:-1]}-{rut_cesionario[-1]}"
    domicilio_cesionario = input("Ingrese domicilio cesionario: ")
    correo_cesionario = input("Ingrese correo cesionario: ")

    #marca
    marca = input("Ingrese marca: ")

    #banco
    numero_cuenta = input("Ingrese número de cuenta: ")
    tipo_cuenta = input("Ingrese tipo de cuenta: ")
    banco = input("Ingrese nombre del banco: ")

    #info extra
    fecha_contrato = input("Ingrese fecha contrato: ")

    #nombre del archivo
    nombre_archivo = f"Cesión de derechos. {nombre_cesionario}-{fecha(date.today())}.docx"

    salida = Path("salidas/chile/") / nombre_archivo

    contexto = {
        "NOMBRE_CEDENTE": nombre_cedente,
        "CEDULA_CEDENTE": cedula_cedente,
        "RUT_CEDENTE": rut_cedente_f,
        "DOMICILIO_CEDENTE": domicilio_cedente,
        "CORREO_CEDENTE": correo_cedente,

        "NOMBRE_CESIONARIO": nombre_cesionario,
        "CEDULA_CESIONARIO": cedula_cesionario,
        "RUT_CESIONARIO": rut_cesionario_f,
        "DOMICILIO_CESIONARIO": domicilio_cesionario,
        "CORREO_CESIONARIO": correo_cesionario,

        "MARCA": marca,

        "NUMERO_CUENTA": numero_cuenta,
        "TIPO_CUENTA": tipo_cuenta,
        "BANCO": banco,

        "FECHA": fecha(date.today()),
        "FECHA_CONTRATO": fecha_contrato,
    }

    #rellenar plantilla
    docx = DocxTemplate(plantilla)
    docx.render(contexto)
    docx.save(salida)

    print("Documento generado\n")
    print("*"*20)

if __name__ == "__main__":
    generar_cesion_fisica_a_fisica_chile()