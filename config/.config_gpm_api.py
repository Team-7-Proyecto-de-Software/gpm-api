import gpm

username_pps = "<tu usuario PPS>" # Generalmente es tu correo en minuscula
password_pps = "<tu contraseña PPS>" # Generalmente es tu correo en minuscula
username_earthdata = "<tu usuario EarthData>"
password_earthdata = "<tu contraseña EarthData>"
base_dir = "../data/"  # Carpeta donde se guardarán los datos

gpm.define_configs(
    username_pps=username_pps,
    password_pps=password_pps,
    username_earthdata=username_earthdata,
    password_earthdata=password_earthdata,
    base_dir=base_dir,
)
print("Configuración guardada correctamente.")
