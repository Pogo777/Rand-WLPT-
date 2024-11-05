def convert_wltp_to_epa(wltp_distance_km):
    """
    แปลงระยะทางจาก WLTP เป็น EPA
    โดยใช้ค่าเฉลี่ยการลดลงของ EPA ที่ประมาณ 12.5% จาก WLTP
    """
    reduction_factor = 0.125  # 12.5%
    epa_distance_km = wltp_distance_km * (1 - reduction_factor)
    return epa_distance_km

def convert_epa_to_wltp(epa_distance_km):
    """
    แปลงระยะทางจาก EPA เป็น WLTP
    โดยการคำนวณย้อนกลับจาก EPA เพิ่มขึ้น 12.5% เพื่อให้ได้ WLTP
    """
    increase_factor = 1.125  # 12.5% increase to convert EPA to WLTP
    wltp_distance_km = epa_distance_km * increase_factor
    return wltp_distance_km

def main():
    print("เลือกตัวแปลงหน่วยระยะทางรถพลังงานไฟฟ้า (EV):")
    print("1: WLTP -> EPA")
    print("2: EPA -> WLTP")
    
    choice = input("ป้อนหมายเลขการแปลง (1 หรือ 2): ")

    if choice == "1":
        wltp_distance = float(input("ป้อนระยะทางตามมาตรฐาน WLTP (กิโลเมตร): "))
        epa_distance = convert_wltp_to_epa(wltp_distance)
        print(f"ระยะทางตามมาตรฐาน EPA คือประมาณ {epa_distance:.2f} กิโลเมตร")
    elif choice == "2":
        epa_distance = float(input("ป้อนระยะทางตามมาตรฐาน EPA (กิโลเมตร): "))
        wltp_distance = convert_epa_to_wltp(epa_distance)
        print(f"ระยะทางตามมาตรฐาน WLTP คือประมาณ {wltp_distance:.2f} กิโลเมตร")
    else:
        print("เลือกไม่ถูกต้อง! กรุณาเลือก 1 หรือ 2.")

if __name__ == "__main__":
    main()
