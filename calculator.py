#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculator Module
Berisi fungsi kalkulator universal yang menggunakan math_operations
Author: Yohanes 2026
"""

from math_operations import tambah, kali, kurang, bagi, pecah

def kalkulator(a, b, operasi):
    """
    Fungsi kalkulator universal yang bisa melakukan multiple operasi matematika
    
    Args:
        a (int/float): Bilangan pertama
        b (int/float): Bilangan kedua
        operasi (str): Jenis operasi ('tambah', 'kali', 'kurang', 'bagi', 'pecah')
        
    Returns:
        int/float/str: Hasil operasi atau error message
    """
    if operasi == "tambah":
        return tambah(a, b)
    elif operasi == "kali":
        return kali(a, b)
    elif operasi == "kurang":
        return kurang(a, b)  # Fixed: tanpa string concatenation
    elif operasi == "bagi":
        return bagi(a, b)
    elif operasi == "pecah":
        return pecah(a, b)
    else:
        return "Operasi tidak dikenal"

# Export fungsi untuk import *
__all__ = ['kalkulator']
