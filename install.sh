#!/bin/bash

echo "Menginstal bahasa pemrograman Ne Jowo di Termux..."

# Memberikan akses eksekusi pada file utama
chmod +x nejowo.py

# Membuat shortcut 'nj' di folder bin Termux
cp nejowo.py $PREFIX/bin/nj

echo "Instalasi rampung! Saiki sampeyan bisa nggunakake perintah 'nj' kanggo nglakokake file .nj"
