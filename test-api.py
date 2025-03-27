import gpm
import datetime
# Archivo para testear descargas de datos
# En este caso descargar datos de GPM 2A-GPM-SLH

# Specify the time period you are interested in
start_time = datetime.datetime.strptime("2023-08-01 00:00:01", "%Y-%m-%d %H:%M:%S")
end_time = datetime.datetime.strptime("2023-08-02 00:00:00", "%Y-%m-%d %H:%M:%S")
# Specify the product and product type
product = "2A-GPM-SLH"  # 2A-PR
product_type = "RS"
storage = "GES_DISC"
# Specify the version
version = 7

# Download the data
gpm.download(
    product=product,
    product_type=product_type,
    version=version,
    start_time=start_time,
    end_time=end_time,
    storage=storage,
    force_download=False,
    verbose=True,
    progress_bar=True,
    check_integrity=False,
)
