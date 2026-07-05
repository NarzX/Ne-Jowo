#!/usr/bin/env python3
# =====================================================================
# NE JOWO ( .nj ) - Version 2.1.0 (Color Update Release)
# Advanced Transpiler Engine with Terminal Color Support
# =====================================================================
import sys
import os
import subprocess

# Kode Warna ANSI untuk Termux
IJO_PADANG = "\\033[1;32m"  # Hijau Terang untuk Output
ABANG = "\\033[1;31m"       # Merah untuk Error
KUNING = "\\033[1;33m"      # Kuning untuk Warning
RESIK = "\\033[0m"          # Reset warna kembali normal

KAMUS_KATA = {
    " gadhah ": " = ",
    " ditambah ": " + ",
    " dikurangi ": " - ",
    " diping ": " * ",
    " diporo ": " / ",
    " podo_karo ": " == ",
    " luwih_akeh ": " > ",
    " luwih_sithik ": " < "
}

def transpile_ke_python(kode_jowo):
    baris_kode = kode_jowo.split('\n')
    kode_python = []
    level_indentasi = 0
    
    for baris in baris_kode:
        baris_bersih = baris.strip()
        
        if not baris_bersih or baris_bersih.startswith('#'):
            kode_python.append("    " * level_indentasi + baris_bersih)
            continue
            
        if baris_bersih == "wis_rampung":
            level_indentasi = max(0, level_indentasi - 1)
            continue
            
        baris_baru = "    " * level_indentasi + baris_bersih
        
        # 3. Perintah Cetak Berwarna Hijau Otomatis
        if baris_bersih.startswith("aturaken "):
            isi = baris_bersih[9:].strip()
            # Menyisipkan kode warna ANSI di awal dan akhir print
            baris_baru = "    " * level_indentasi + f"print(f'{IJO_PADANG}', {isi}, f'{RESIK}', sep='', flush=True)"
            
        elif " nyuwun_input" in baris_bersih:
            var_name = baris_bersih.split(" nyuwun_input").strip()
            baris_baru = "    " * level_indentasi + f"{var_name} = input()"
            
        elif " nyuwun_angka" in baris_bersih:
            var_name = baris_bersih.split(" nyuwun_angka").strip()
            baris_baru = "    " * level_indentasi + f"try:\n" + "    " * (level_indentasi + 1) + f"{var_name} = int(input())\n" + "    " * level_indentasi + f"except ValueError:\n" + "    " * (level_indentasi + 1) + f"{var_name} = 0"
            
        elif baris_bersih.startswith("yen ") and baris_bersih.endswith(" banjur"):
            kondisi = baris_bersih[4:-7].strip()
            for jowo, py in KAMUS_KATA.items():
                kondisi = kondisi.replace(jowo, py)
            baris_baru = "    " * level_indentasi + f"if {kondisi}:"
            level_indentasi += 1
            
        elif baris_bersih.startswith("utawa_yen ") and baris_bersih.endswith(" banjur"):
            kondisi = baris_bersih[10:-7].strip()
            for jowo, py in KAMUS_KATA.items():
                kondisi = kondisi.replace(jowo, py)
            baris_baru = "    " * (level_indentasi - 1) + f"elif {kondisi}:"
            
        elif baris_bersih == "utawa":
            baris_baru = "    " * (level_indentasi - 1) + "else:"
            
        elif baris_bersih.startswith("mbaleni ") and baris_bersih.endswith(" banjur"):
            kondisi = baris_bersih[8:-7].strip()
            for jowo, py in KAMUS_KATA.items():
                kondisi = kondisi.replace(jowo, py)
            baris_baru = "    " * level_indentasi + f"while {kondisi}:"
            level_indentasi += 1
            
        else:
            for jowo, py in KAMUS_KATA.items():
                baris_baru = baris_baru.replace(jowo, py)
                
        kode_python.append(baris_baru)
        
    return '\n'.join(kode_python)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("\033[1;36m==================================================\033[0m")
        print("\033[1;32mSugeng Rawuh ing Ne Jowo v2.1.0 Compiler (Colors)\033[0m")
        print("\033[1;36m==================================================\033[0m")
        print("Cara nganggo: nj [jeneng_file.nj]")
        sys.exit(0)
        
    # PERBAIKAN: Ambil elemen indeks ke-1 dari list sys.argv
    nama_file = sys.argv[1]
    
    if not nama_file.endswith('.nj'):
        print(f"\033[1;31mLuput: Berkas kudu nduweni ekstensi .nj\033[0m")
        sys.exit(1)
        
    try:
        with open(nama_file, 'r', encoding='utf-8') as f:
            isi_jowo = f.read()
            
        isi_python = transpile_ke_python(isi_jowo)
        file_temp = nama_file + ".v2.py"
        
        with open(file_temp, 'w', encoding='utf-8') as f_temp:
            f_temp.write(isi_python)
            
        subprocess.run([sys.executable, file_temp])
        
        if os.path.exists(file_temp):
            os.remove(file_temp)
            
    except FileNotFoundError:
        print(f"\033[1;31mLuput: File '{nama_file}' ora ditemokake!\033[0m")
    except KeyboardInterrupt:
        print("\n\033[1;33m[!] Program dipeksa mandeg dening pangguna.\033[0m")
