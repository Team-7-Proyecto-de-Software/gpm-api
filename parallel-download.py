import gpm
import datetime
from concurrent.futures import ThreadPoolExecutor

# Archivo para testear descargas de datos
# En este caso descargar datos de GPM 2A-GPM-SLH

# Specify the time period you are interested in
start_time = datetime.datetime.strptime("2023-08-01 00:00:01", "%Y-%m-%d %H:%M:%S")
end_time = datetime.datetime.strptime("2023-08-02 00:00:00", "%Y-%m-%d %H:%M:%S")

# Para descargar los archivos de manera paralela lo que haremos sera dividir el rango de fechas en partes iguales
# y luego descargar cada parte en un hilo diferente
# Podemos asumir que los tamaños de los archivos son iguales y que el tiempo de descarga es el mismo para cada uno


num_parts = 5  # Número de partes en las que quieres dividir el tiempo

# Dividir el tiempo en partes iguales
delta = (end_time - start_time) / num_parts
time_intervals = []

for i in range(num_parts):
    part_start = start_time + i * delta
    part_end = start_time + (i + 1) * delta
    time_intervals.append((part_start, part_end))

# Specify the time period you are interested in
start_time = datetime.datetime.strptime("2023-08-01 00:00:01", "%Y-%m-%d %H:%M:%S")
end_time = datetime.datetime.strptime("2023-08-02 00:00:00", "%Y-%m-%d %H:%M:%S")
# Specify the product and product type
product = "2A-GPM-SLH"  # 2A-PR
product_type = "RS"
storage = "GES_DISC"
# Specify the version
version = 7

# Función para descargar en paralelo
def download_data(time_range):
    part_start, part_end = time_range
    print(f"Descargando desde {part_start} hasta {part_end}...")
    gpm.download(
        product=product,
        product_type=product_type,
        version=version,
        start_time=part_start,
        end_time=part_end,
        storage=storage,
        force_download=False,
        verbose=True,
        progress_bar=True,
        check_integrity=False,
    )

# Ejecutar descargas en paralelo con ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=num_parts) as executor:
    executor.map(download_data, time_intervals)

print("Todas las descargas han finalizado.")