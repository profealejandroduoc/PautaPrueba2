from os import system
system("cls")


hb=0
hc=0
hgl=0
hgmf=0

while True:
    print("""
1. Huevos Blancos $7000
2. Huevos Color $ $8000
3. Huevos Gallina Libre $8500
4. Huevos Gallina Mega Feliz $10000
5. Finalizar pedido
    
    """)
    op=input("Ingrese opcion: ")
    match op:
        case "1":
            hb+=1
        case "2":
            hc+=1
        case "3":
            hgl+=1
        case "4":
            hgmf+=1
        case "5":
            break
        case other:
            print("no válido....")

while True:
    codigo=input("Ingrese código de descuento: ")
    if codigo!="":
        break

if codigo=="megustaelhue":
    descuento=0.15
else:
    descuento=0

prod=hc+hb+hgl+hgmf
total=hc*8000+hb*7000+hgl*8500+hgmf*10000
print(f"""
******************************
TOTAL PRODUCTOS:{prod}
******************************
Huevos Blancos :{hb}
Huevos Color :{hc}
Gallina Libre :{hgl}
Gallina mega feliz :{hgmf}
******************************
Subtotal por pagar: ${total}
Descuento por código: ${total*descuento}
TOTAL: ${total-(total*descuento)}


""")