import gpm
import gpm
import datetime

# Specify the time period you are interested in
start_time = datetime.datetime.strptime("2020-08-01 12:00:00", "%Y-%m-%d %H:%M:%S")
end_time = datetime.datetime.strptime("2020-08-02 12:00:00", "%Y-%m-%d %H:%M:%S")
# Specify the product and product type
product = "2A-MHS-METOPB-CLIM"  # "2A-GMI-CLIM", "2A-SSMIS-F17-CLIM", ...
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
