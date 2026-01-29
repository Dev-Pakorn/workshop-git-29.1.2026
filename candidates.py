def show_list():
    # กำหนดรหัสสี (ANSI Escape Codes) ใช้แทน CSS ใน Terminal
    HEADER = '\033[95m'  # สีม่วง
    BLUE = '\033[94m'    # สีฟ้า
    GREEN = '\033[92m'   # สีเขียว
    YELLOW = '\033[93m'  # สีเหลือง
    RED = '\033[91m'     # สีแดง
    BOLD = '\033[1m'     # ตัวหนา
    RESET = '\033[0m'    # ล้างค่าสีกลับเป็นปกติ

    # ส่วนหัวข้อ (ตกแต่งคล้าย Header)
    print(f"\n{HEADER}╔══════════════════════════════════════════════╗{RESET}")
    print(f"{HEADER}║        🗳️  รายชื่อผู้สมัครประธานสาขา         ║{RESET}")
    print(f"{HEADER}╚══════════════════════════════════════════════╝{RESET}\n")

    # ผู้สมัครเบอร์ 1
    print(f"  {BOLD}{YELLOW}[ เบอร์ 1 ]{RESET} {GREEN}นายสมชาย{RESET}")
    print(f"  {BLUE}📢 นโยบาย:{RESET} เรียนดี เรียนฟรี มีเกียร์")
    print("-" * 45) # ขีดเส้นคั่น

    # ผู้สมัครเบอร์ 2
    print(f"  {BOLD}{YELLOW}[ เบอร์ 2 ]{RESET} {GREEN}นางสาวสมหญิง{RESET}")
    print(f"  {BLUE}📢 นโยบาย:{RESET} เน็ตมอแรง ทุกจุด")
    print("-" * 45 + "\n")

    # ผู้สมัครเบอร์ 3
    print(f"  {BOLD}{YELLOW}[ เบอร์ 3 ]{RESET} {GREEN}นายเขมร{RESET}")
    print(f"  {BLUE}📢 นโยบาย:{RESET} เรียนไม่เข้ารุ่ง มุ่งกู้ภัย")
    print("-" * 45) # ขีดเส้นคั่น

    
    # ผู้สมัครเบอร์ 4
    print(f"  {BOLD}{YELLOW}[ เบอร์ 4 ]{RESET} {GREEN}นายเจย์{RESET}")
    print(f"  {BLUE}📢 นโยบาย:{RESET} เรียนไม่รุ่ง มุ่งคิดถึงคนเก่า")
    print("-" * 45) # ขีดเส้นคั่น

    # ผู้สมัครเบอร์ 5
    print(f"  {BOLD}{YELLOW}[ เบอร์ 5 ]{RESET} {GREEN}นายตาต้า{RESET}")
    print(f"  {BLUE}📢 นโยบาย:{RESET} คนดีพี่ขอโทษ")
    print("-" * 45) # ขีดเส้นคั่น
