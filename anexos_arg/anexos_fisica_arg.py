from docxtpl import DocxTemplate
from datetime import date
from pathlib import Path

def fecha(d: date )->str:
    meses =["enero","febrero","marzo","abril","mayo","junio",
            "julio","agosto","septiembre","octubre","noviembre","diciembre"]
    return f"{d.day} de {meses[d.month-1]} de {d.year}"

def generar_anexo_fisica_arg():
    #ruta
    plantilla = Path("plantillas/argentina/Anexo_de_Adhesión_fisica_arg.docx")

#palabras a rellenar

    print(f"\n{"*"*10}Anexo adhesión persona fisica ARGENTINA{"*"*10}\n")


    #Aliado
    aliado = input("Ingrese nombre aliado a anexar: ")
    cuit_aliado = input("Ingrese Cuit aliado: ")
    cuit_aliado_f = f"{cuit_aliado[:2]}-{cuit_aliado[2:-1]}-{cuit_aliado[-1]}"
    

    #Razón social principal

    nombre_RZ_Principal = input("Ingrese razón social principal: ")
    cuit_RZ_Principal = input("Ingrese cuit razón social principal: ")
    cuit_RZ_Principal_f = f"{cuit_RZ_Principal[:2]}-{cuit_RZ_Principal[2:-1]}-{cuit_RZ_Principal[-1]}"

    #Marca

    marca =input("Ingrese marca: ")


    #datos bancarios

    numero_cuenta = input("Ingrese numero de cuenta: ")
    numero_cbu = input("Ingrese número cbu: ")
    banco = input("Ingrese nombre del banco: ")

    #nombre del archivo

    nombre_archivo = f"Anexo adhesión. Rappi-{aliado}-{fecha(date.today())}.docx"

    salida = Path("salidas/argentina/")/ nombre_archivo

    contexto = {
        "ALIADO": aliado,
        "CUIT_ALIADO": cuit_aliado_f,

        "RZ_PRINCIPAL": nombre_RZ_Principal,
        "CUIT_RZ_PRINCIPAL": cuit_RZ_Principal_f,

        "MARCA": marca,

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
    generar_anexo_fisica_arg()