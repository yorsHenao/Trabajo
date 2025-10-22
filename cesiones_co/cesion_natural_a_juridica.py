from docxtpl import DocxTemplate
from datetime import date
from pathlib import Path

#Función para formato fechas
def fecha(d: date )-> str:
    meses =["enero","febrero","marzo","abril","mayo","junio",
            "julio","agosto","septiembre","octubre","noviembre","diciembre"]
    return f"{d.day} de {meses[d.month-1]} de {d.year}"


def generar_cesion_natural_a_juridica():
    #rutas
    plantilla = Path("plantillas/colombia/cesion_Natural_a_Juridica.docx")

    #Palabras a rellenar
    print(f"\n{"*"*10}Cesión Persona fisica a juridica{"*"*10}\n")
    nombre_cedente = input("Ingrese nombre cedente: ")
    cedula_cedente = input("Ingrese cedula cedente: ")
    ciudad_cedente = input("Ingrese ciudad cedente: ")

    #cesionario

    nombre_cesionario = input("ingrese nombre razón social cesionario: ")
    nit_cesionario = input("Ingrese Nit razón social cesionario: ")
    ciudad_cesionario = input("Ingrese ciudad cesionario: ")
    rl_cesionario = input("Ingrese nombre representante RZ cesionario: ")
    cedula_rl_cesionario = input("Ingrese cedula RL cesionario: ")

    #fecha acuerdo principal

    fecha_contrato = input("Ingrese fecha contrato principal: ")

    #datos bancarios

    tipo_cuenta = input("Ingrese tipo de cuenta: ")
    numero_cuenta = input("Ingrese número de cuenta: ")
    banco = input("Ingrese nombre del banco: ")

    #nombre del archivo

    nombre_archivo = f"Acta cesión. Rappi-{nombre_cesionario}-{fecha(date.today())}.docx"

    salida = Path("salidas/colombia/")/ nombre_archivo

    contexto = {
        "NOMBRE_CEDENTE": nombre_cedente,
        "CEDULA_CEDENTE": cedula_cedente,
        "CIUDAD_CEDENTE": ciudad_cedente,
        "RS_CESIONARIO": nombre_cesionario,
        "NIT_CESIONARIO": nit_cesionario,
        "CIUDAD_CESIONARIO": ciudad_cesionario,
        "RL_CESIONARIO": rl_cesionario,
        "CEDULA_RL_CESIONARIO": cedula_rl_cesionario,
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
    generar_cesion_natural_a_juridica()
