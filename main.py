# Liberias utilizadas
import psutil
import platform

# Cantidad de CPU's
print(f"Numero de nucleos fisicos:", {psutil.cpu_count(logical=False)})

# Cantidad de procesos ejecutandose
print(f"Procesos ejecutandose:", len(psutil.pids()))

# Cantidad de hilos
print(f"Numero de nucleos logicos:", {psutil.cpu_count(logical=True)})


# Tipo de bus de datos
(bits, Os) = platform.architecture()
print(f"Tipo de bus de datos:", bits)

# Cantidad de memoria RAM
print(f"Cantidad de memoria RAM: {round(psutil.virtual_memory().total/1000000000, 2)} GB")