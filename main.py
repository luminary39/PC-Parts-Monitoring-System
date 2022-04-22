import ryans
import star_tech
import sky_land
import netstar
from datetime import date
import os



# File name

file_name = str(date.today()) + ".txt"

file_path = os.path.join("D:/Python Programme/PC Parts Prise Monitoring System(PPPMS)/Daily Price Comparison Files", file_name)

# CPU Part

ryans_cpu_price = ryans.ryans_price_check("https://www.ryanscomputers.com/intel-12th-gen-alder-lake-core-i5-12400-desktop-processor")

start_tech_cpu_price = star_tech.star_tech_price_check("https://www.startech.com.bd/intel-12th-gen-core-i5-12400-alder-lake-processor")

sky_land_cpu_price = sky_land.sky_land_price_checker("https://www.skyland.com.bd/product/intel-core-i5-12400-gen-processor/")

cpu_average_price = (ryans_cpu_price+start_tech_cpu_price+sky_land_cpu_price)//3

cpu_price_string = f"Intel 12th Gen Core i5-12400 Alder Lake Processor\n" \
                   f"******************************\n" \
                   f"Ryans: {ryans_cpu_price}\n" \
                   f"Star Tech: {start_tech_cpu_price}\n" \
                   f"Sky Land: {sky_land_cpu_price}\n" \
                   f"Net Star: Not Available Currently!\n\n" \
                   f"Average Price: {cpu_average_price} BDT\n\n" \

cpu_average_price = (ryans_cpu_price+start_tech_cpu_price+sky_land_cpu_price)//3

# print(cpu_price_string, file_name)


# Saving File


with open(file_path, "w") as file:

    file.write(cpu_price_string)
    file.close()