especialistas_senior = 0
residentes_junior = 0

print("=== BIENVENIDO AL SISTEMA DE REGISTRO MÉDICO ===")

#Validar cantidad de médicos a registrar 

while True:
    try:
        cantidad = int(input("¿Cuántos médicos desea registrar?: "))
        if cantidad <= 0:
            print("¡Error! La cantidad de médicos debe ser un número entero positivo.")
            continue
        break
    except ValueError:
        print("¡Registro médico inválido! Ingresa un número entero válido para continuar.")

#Ciclo principal de registro

for i in range(1, cantidad + 1):
    print(f"--- Registro del médico {i} de {cantidad} ---")

 #Validar nombre de profesional

    while True:
        nombre = input("Nombre profesional (mínimos 6 caracteres sin espacios): ").strip()
        
        if len(nombre) < 6:
            print("¡Nombre inválido! Debe tener al menos 6 caracteres.")
        elif " " in nombre:
            print("¡Nombre inválido! No debe contener espacios intermedios.")
        else:
            break

 # Validar experiencia clínica

    while True:
        try:
            experiencia = int(input("Años de experiencia clínica: "))
            if experiencia <= 0:
                print("¡Error clínico! Los años de experiencia no pueden ser negativos.")
                continue
            break
        except ValueError:
            print("¡Error clínico! Ingresa un número entero válido para la experiencia.")

 #Clasificar al médico y actualizar
 
    if experiencia > 5:
        categoria = "Especialista Senior"
        especialistas_senior += 1
    else:
        categoria = "Residente Junior"
        residentes_junior += 1

    print(f" {nombre} registrado con éxito como {categoria}.")

#Salida final 

print("=" * 55)
print(f"¡El hospital cuenta con {especialistas_senior} Especialistas Senior y {residentes_junior} Residentes Junior! ¡Sistema listo para operar!")
print("=" * 55)
