from xml.etree.ElementTree import TreeBuilder
import ryans
import star_tech
import sky_land
import netstar
from datetime import date, datetime
import os


# File name

file_name = str(date.today()) + ".txt"

file_path = os.path.join("D:/Python Programme/PC Parts Prise Monitoring System(PPPMS)/Daily Price Comparison Files",
                         file_name)

# CPU Part

ryans_cpu_price = ryans.ryans_price_check(
    "https://www.ryanscomputers.com/intel-12th-gen-alder-lake-core-i5-12400-desktop-processor")

start_tech_cpu_price = star_tech.star_tech_price_check(
    "https://www.startech.com.bd/intel-12th-gen-core-i5-12400-alder-lake-processor")

sky_land_cpu_price = sky_land.sky_land_price_check(
    "https://www.skyland.com.bd/product/intel-core-i5-12400-gen-processor/")

cpu_average_price = (int(ryans_cpu_price) + int(start_tech_cpu_price) + int(sky_land_cpu_price)) // 3



# Ram Parts

ryans_ram_prise = ryans.ryans_price_check("https://www.ryanscomputers.com/corsair-vengeance-lpx-8gb-ddr4-3200mhz-desktop-ram")

star_tech_ram_prise = star_tech.star_tech_price_check("https://www.startech.com.bd/corsair-vengeance-lpx-8gb-3200mhz")

sky_land_ram_prise = sky_land.sky_land_price_check("https://www.skyland.com.bd/product/corsair-vengeance-lpx-8gb-3200mhz-ram/")

netstar_ram_prise = netstar.netstar_price_check("https://www.netstar.com.bd/product/corsair-vengeance-lpx-8gb-3200mhz-ddr4-desktop-ram/")

ram_average_prise = (int(ryans_ram_prise) + int(star_tech_ram_prise) + int(sky_land_ram_prise) + int(netstar_ram_prise)) // 4


# SSD Part

ryans_ssd_prise = ryans.ryans_price_check("https://www.ryanscomputers.com/team-mp33-256gb-m.2-2280-nvme-pcie-ssd")

star_tech_ssd_prise = star_tech.star_tech_price_check("https://www.startech.com.bd/team-mp33-256gb-ssd")

sky_land_ssd_prise = sky_land.sky_land_price_check("https://www.skyland.com.bd/product/team-mp33-256gb-m2-ssd/")

netstar_ssd_prise = netstar.netstar_price_check("https://www.netstar.com.bd/product/team-mp33-256gb-m-2-pcie-ssd/")

ssd_average_prise = (int(ryans_ssd_prise)+ int(star_tech_ssd_prise)+ int(sky_land_ssd_prise)+ int(netstar_ssd_prise))//4



# HDD Parts

ryans_hdd_prise = ryans.ryans_price_check("https://www.ryanscomputers.com/seagate-barracuda-1tb-35-inch-sata-7200rpm-desktop-hdd-st1000dm010")

star_tech_hdd_prise = star_tech.star_tech_price_check("https://www.startech.com.bd/seagate-1tb-barracuda")

sky_land_hdd_prise = sky_land.sky_land_price_check("https://www.skyland.com.bd/product/seagate-internal-1tb-sata-barracuda-hdd/")

netstar_hdd_prise = netstar.netstar_price_check("https://www.netstar.com.bd/404")

hdd_average_prise = (int(ryans_hdd_prise)+ int(sky_land_hdd_prise)) //2




report_string = f"              CPU         \n"\
                f"Intel 12th Gen Core i5-12400 Alder Lake Processor\n" \
                f"******************************\n" \
                f"Ryans: {ryans_cpu_price}\n" \
                f"Star Tech: {start_tech_cpu_price}\n" \
                f"Sky Land: {sky_land_cpu_price}\n" \
                f"Net Star: Not Available Currently!\n\n" \
                f"Average Price: {cpu_average_price} BDT\n\n\n"\
                f"**************************************************\n\n\n"\
                f"          RAM         \n"\
                f"Corsair Vengeance LPX 8GB DDR4 3200MHz Desktop RAM\n"\
                f"******************************\n" \
                f"Ryans: {ryans_ram_prise}\n"\
                f"Star Tech: {star_tech_ram_prise}\n"\
                f"Sky Land: {sky_land_ram_prise}\n"\
                f"Netstar: {netstar_ram_prise}\n\n"\
                f"Average RAM Prise {ram_average_prise}\n\n\n"\
                f"**************************************************\n\n\n"\
                f"          SSD         \n"\
                f"Team MP33 256GB M.2 PCIe SSD\n"\
                f"******************************\n" \
                f"Ryans: {ryans_ssd_prise}\n"\
                f"Star Tech: {star_tech_ssd_prise}\n"\
                f"Sky Land: {sky_land_ssd_prise}\n"\
                f"Netstar: {netstar_ssd_prise}\n\n"\
                f"Average RAM Prise {ssd_average_prise}\n\n\n"\
                f"**************************************************\n\n\n"\
                f"          HDD         \n"\
                f"Seagate Barracuda 7200RPM 1TB Desktop Hard disk(Internal)\n"\
                f"******************************\n" \
                f"Ryans: {ryans_hdd_prise}\n"\
                f"Star Tech: {star_tech_hdd_prise} [BUG Error]!\n"\
                f"Sky Land: {sky_land_hdd_prise}\n"\
                f"Netstar: {netstar_hdd_prise}\n\n"\
                f"Average RAM Prise {hdd_average_prise}\n\n\n"\





# Saving File


with open(file_path, "w") as file:
    file.write(report_string)
    file.close()
