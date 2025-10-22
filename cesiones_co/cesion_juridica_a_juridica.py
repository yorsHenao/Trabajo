from docxtpl import DocxTemplate
from datetime import date
from pathlib import Path

def fecha(d: date )-> str:
    meses =["enero","febrero","marzo","abril","mayo","junio",
            "julio","agosto","septiembre","octubre","noviembre","diciembre"]
    return f"{d.day} de {meses[d.month-1]} de {d.year}"


def generar_cesion_juridica_a_juridica():
    #ruta
    plantilla = Path("plantillas/colombia/cesion_juridica_a_juridica.docx")

    #palabras a rellenar

    print(f"\n{"*"*10}Cesión Personas Juridicas{"*"*10}\n")
    #cedente
    nombre_cedente = input("ingrese nombre razón social cedente: ")
    nit_cedente = input("Ingrese Nit razón social cedente: ")
    ciudad_cedente = input("Ingrese ciudad cedente: ")
    rl_cedente = input("Ingrese nombre representante RZ cedente: ")
    cedula_rl_cedente = input("Ingrese cedula RL cedente: ")


    #cesionario
    nombre_cesionario = input("ingrese nombre razón social cesionario: ")
    nit_cesionario = input("Ingrese Nit razón social cesionario: ")
    ciudad_cesionario = input("Ingrese ciudad cesionario: ")
    rl_cesionario = input("Ingrese nombre representante RZ cesionario: ")
    cedula_rl_cesionario = input("Ingrese cedula RL cesionario: ")

    #fecha acuerdo
    fecha_contrato = input("Ingrese fecha contrato principal: ")

    #datos bancarios

    tipo_cuenta = input("Ingrese tipo de cuenta: ")
    numero_cuenta = input("Ingrese número de cuenta: ")
    banco = input("Ingrese nombre del banco: ")

    #Nombre del archivo

    nombre_archivo = f"Acta cesión. Rappi-{nombre_cesionario}-{fecha(date.today())}.docx"
    salida = Path("salidas/colombia/")/ nombre_archivo


    #datos plantilla

    contexto = {
        "RS_CEDENTE": nombre_cedente,
        "NT_CEDENTE": nit_cedente,
        "CIUDAD_CEDENTE": ciudad_cedente,
        "RL_CEDENTE": rl_cedente,
        "CEDULA_CEDENTE": cedula_rl_cedente,
        "RS_CESIONARIO": nombre_cesionario,
        "NIT_CESIONARIO": nit_cesionario,
        "CIUDAD_CESIONARIO": ciudad_cesionario,
        "RL_CESIONARIO": rl_cesionario,
        "CEDULA_CESIONARIO": cedula_rl_cesionario,
        "FECHA_ACUERDO_P":fecha_contrato,
        "TIPO_CUENTA": tipo_cuenta,
        "NUMERO_CUENTA": numero_cuenta,
        "BANCO": banco,
        "FECHA": fecha(date.today())
    }

    #rellenar plantilla

    docx = DocxTemplate(plantilla)
    docx.render(contexto)
    docx.save(salida)
    
    print(f"Documento generado")
    print("*"*20)

if __name__ == "__main__":
    generar_cesion_juridica_a_juridica()


