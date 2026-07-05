#!/usr/bin/env python3
import sys
import re

def eksekusi_jawa(kode, variabel_global=None):
    variabel = variabel_global if variabel_global is not None else {}
    baris_kode = kode.strip().split('\n')
    indeks = 0
    
    while indeks < len(baris_kode):
        baris = baris_kode[indeks].strip()
        
        if not baris or baris.startswith('#'):
            indeks += 1
            continue
            
        if ' #' in baris:
            baris = baris.split(' #')[0].strip()

        # 1. Perulangan: "mbaleni"
        if baris.startswith("mbaleni"):
            pola_loop = r"mbaleni (.+?) (luwih_sithik|luwih_akeh) (.+?) banjur (.+)"
            cocok_loop = re.match(pola_loop, baris)
            
            if cocok_loop:
                var_loop = cocok_loop.group(1).strip()
                operator_loop = cocok_loop.group(2).strip()
                target_loop = int(cocok_loop.group(3).strip())
                aksi_loop = cocok_loop.group(4).strip()
                
                def cek_kondisi():
                    val = variabel.get(var_loop, 0)
                    if operator_loop == "luwih_sithik": return val < target_loop
                    elif operator_loop == "luwih_akeh": return val > target_loop
                    return False
                
                while cek_kondisi():
                    eksekusi_jawa(aksi_loop, variabel)
            indeks += 1
            continue

        # 2. Percabangan: "yen"
        elif baris.startswith("yen"):
            pola_kondisi = r"yen (.+?) (gadhah|luwih_akeh|luwih_sithik) (.+?) banjur (.+?)(?: utawa (.+))?$"
            pencocokan = re.match(pola_kondisi, baris)
            
            if pencocokan:
                var_cek = pencocokan.group(1).strip()
                op_cek = pencocokan.group(2).strip()
                nilai_cek = pencocokan.group(3).strip()
                aksi_benar = pencocokan.group(4).strip()
                aksi_salah = pencocokan.group(5).strip() if pencocokan.group(5) else None
                
                if nilai_cek.isdigit(): nilai_cek = int(nilai_cek)
                elif nilai_cek.startswith('"') and nilai_cek.endswith('"'): nilai_cek = nilai_cek[1:-1]
                
                v_aktual = variabel.get(var_cek, 0)
                kondisi_terpenuhi = False
                
                if op_cek == "gadhah": kondisi_terpenuhi = (v_aktual == nilai_cek)
                elif op_cek == "luwih_akeh": kondisi_terpenuhi = (v_aktual > nilai_cek)
                elif op_cek == "luwih_sithik": kondisi_terpenuhi = (v_aktual < nilai_cek)
                
                if kondisi_terpenuhi: eksekusi_jawa(aksi_benar, variabel)
                elif aksi_salah: eksekusi_jawa(aksi_salah, variabel)
            indeks += 1
            continue

        # 3. Input Pengguna: "nyuwun"
        elif "nyuwun" in baris:
            kunci, _ = baris.split("nyuwun")
            kunci = kunci.strip()
            input_user = input()
            variabel[kunci] = int(input_user) if input_user.isdigit() else input_user

        # 4. Variabel & Matematika Lengkap
        elif "gadhah" in baris:
            kunci, nilai_mentah = baris.split("gadhah")
            kunci = kunci.strip()
            nilai_mentah = nilai_mentah.strip()
            
            operator_mat = None
            for op in ["ditambah", "dikurangi", "diping", "diporo"]:
                if op in nilai_mentah:
                    operator_mat = op
                    break
            
            if operator_mat:
                kiri, kanan = nilai_mentah.split(operator_mat)
                v_kiri = variabel.get(kiri.strip(), int(kiri.strip()) if kiri.strip().isdigit() else 0)
                v_kanan = variabel.get(kanan.strip(), int(kanan.strip()) if kanan.strip().isdigit() else 0)
                
                if operator_mat == "ditambah": variabel[kunci] = v_kiri + v_kanan
                elif operator_mat == "dikurangi": variabel[kunci] = v_kiri - v_kanan
                elif operator_mat == "diping": variabel[kunci] = v_kiri * v_kanan
                elif operator_mat == "diporo": variabel[kunci] = int(v_kiri / v_kanan) if v_kanan != 0 else 0
            
            elif nilai_mentah.startswith('"') and nilai_mentah.endswith('"'): variabel[kunci] = nilai_mentah[1:-1]
            elif nilai_mentah.isdigit(): variabel[kunci] = int(nilai_mentah)
                
        # 5. Cetak: "aturaken"
        elif baris.startswith("aturaken"):
            teks = re.findall(r'"([^"]*)"', baris)
            if teks:
                print(teks[0])
            else:
                nama_var = baris.replace("aturaken", "").strip()
                print(variabel.get(nama_var, f"Luput: Variabel '{nama_var}' ora ono"))
                
        indeks += 1

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Luput: Mangga lebokake file .nj sing pan ditiyang (Contoh: nj program.nj)")
    else:
        nama_file = sys.argv[1]
        if not nama_file.endswith('.nj'):
            print("Luput: File kudu nduweni ekstensi .nj")
        else:
            try:
                with open(nama_file, 'r', encoding='utf-8') as f:
                    isi_kode = f.read()
                eksekusi_jawa(isi_kode)
            except FileNotFoundError:
                print(f"Luput: File '{nama_file}' ora ditemokake!")
