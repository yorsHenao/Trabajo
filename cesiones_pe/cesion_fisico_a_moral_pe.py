from docxtpl import DocxTemplate
from datetime import date
from pathlib import Path

#Función para formato de fechas
def fecha(d: date )->str:
    meses =["enero","febrero","marzo","abril","mayo","junio",
            "julio","agosto","septiembre","octubre","noviembre","diciembre"]
    return f"{d.day} de {meses[d.month-1]} de {d.year}"


def generar_cesion_fisica_a_moral_peru():
    #ruta
    plantilla = Path("plantillas/peru/cesion_fisico_a_moral_pe.docx")
    #Palabras a rellenar

    print(f"\n{"*"*10}Cesión Personas fisicas a moral{"*"*10}\n")
    #cedente
    nombre_cedente = input("Ingrese nombre cedente: ")
    dni_cedente = input ("Ingrese DNI cedente: ")
    ruc_cedente = input("Ingrese ruc cedente: ")
    domicilio_cedente = input("Ingrese domicilio cedente: ")
    distrito_cedente = input("Ingrese distrito cedente: ")
    provincia_cedente = input("Ingrese provincia cedente: ")


    #cesionario
    rs_cesionario = input("Ingrese razon social cesionario: ")
    rl_cesionario = input("Ingrese Representante legal cesionario ")
    dni_cesionario = input ("Ingrese DNI del RL  cesionario: ")
    ruc_cesionario = input("Ingrese ruc del la Razon social cesionario: ")
    domicilio_cesionario = input("Ingrese domicilio cesionario: ")
    distrito_cesionario = input("Ingrese distrito cesionario: ")
    provincia_cesionario = input("Ingrese provincia cedente: ")

    #fecha acuerdo principal

    fecha_contrato = input("Ingrese fecha contrato principal: ")

    #marca
    marca= input("Ingrese Marca: ")


    #datos bancarios

    tipo_cuenta = input("Ingrese tipo de cuenta: ")
    numero_cuenta = input("Ingrese número de cuenta: ")
    banco = input("Ingrese nombre del banco: ")
    cci = input("Ingrese CCi: ")

    #nombre del archivo

    nombre_archivo = f"Cesion de posición Contractual + adenda cambio de cuenta bancaria. Rappi-{rs_cesionario}-{fecha(date.today())}.docx"

    salida = Path("salidas/peru/")/ nombre_archivo

    #datos plantilla

    contexto = {
        "NOMBRE_CEDENTE": nombre_cedente,
        "DNI_CEDENTE" : dni_cedente,
        "RUC_CEDENTE": ruc_cedente,
        "DOMICILIO_CEDENTE": domicilio_cedente,
        "DISTRITO_CEDENTE" : distrito_cedente,
        "PROVINCIA_CEDENTE" : provincia_cedente,

        "RS_CESIONARIO": rs_cesionario,
        "RL_CESIONARIO" : rl_cesionario,
        "DNI_CESIONARIO": dni_cesionario,
        "RUC_CESIONARIO":ruc_cesionario,
        "DOMICILIO_CESIONARIO": domicilio_cesionario,
        "DISTRITO_CESIONARIO" : distrito_cesionario,
        "PROVINCIA_CESIONARIO" : provincia_cesionario,
        "FECHA_CONTRATO":fecha_contrato,
        "MARCA" : marca,
        "TIPO_CUENTA": tipo_cuenta,
        "NUMERO_CUENTA": numero_cuenta,
        "CCI" : cci,
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
    generar_cesion_fisica_a_moral_peru()



