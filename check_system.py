import os
import shutil

def check_disk_usage():
    total, used, free = shutil.disk_usage("/")
    usage_percent = (used / total) * 100
    print(f"Uso de Disco: {usage_percent:.2f}%")
    if usage_percent > 80:
        print("ALERTA: Espaço em disco insuficiente!")

if __name__ == "__main__":
    check_disk_usage()
