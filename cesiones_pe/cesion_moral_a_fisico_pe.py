from docxtpl import DocxTemplate
from datetime import date
from pathlib import Path

#Función para formato de fechas
def fecha(d: date )->str:
    meses =["enero","febrero","marzo","abril","mayo","junio",
            "julio","agosto","septiembre","octubre","noviembre","diciembre"]
    return f"{d.day} de {meses[d.month-1]} de {d.year}"


def generar_cesion_moral_a_fisica_peru():
    #ruta
    plantilla = Path("plantillas/peru/cesion_moral_a_fisico_pe.docx")
    #Palabras a rellenar

    print(f"\n{"*"*10}Cesión Personas moral a fisica{"*"*10}\n")
    #cedente
    
    rs_cedente = input("Ingrese razon social cedente: ")
    rl_cedente = input("Ingrese Representante legal cedente ")
    dni_cedente = input ("Ingrese DNI del RL  cedente: ")
    ruc_cedente = input("Ingrese ruc del la Razon social cedente: ")
    domicilio_cedente = input("Ingrese domicilio cedente: ")
    distrito_cedente = input("Ingrese distrito cedente: ")
    provincia_cedente = input("Ingrese provincia cedente: ")


    #cesionario
    nombre_cesionario = input("Ingrese nombre cesionario: ")
    dni_cesionario = input ("Ingrese DNI cesionario: ")
    ruc_cesionario = input("Ingrese ruc cesionario: ")
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

    nombre_archivo = f"Cesion de posición Contractual + adenda cambio de cuenta bancaria. Rappi-{nombre_cesionario}-{fecha(date.today())}.docx"

    salida = Path("salidas/peru/")/ nombre_archivo

    #datos plantilla

    contexto = {
        "RS_CEDENTE": rs_cedente,
        "RL_CEDENTE": rl_cedente,
        "DNI_CEDENTE" : dni_cedente,
        "RUC_CEDENTE": ruc_cedente,
        "DOMICILIO_CEDENTE": domicilio_cedente,
        "DISTRITO_CEDENTE" : distrito_cedente,
        "PROVINCIA_CEDENTE" : provincia_cedente,

        "NOMBRE_CESIONARIO": nombre_cesionario,
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
    generar_cesion_moral_a_fisica_peru()



