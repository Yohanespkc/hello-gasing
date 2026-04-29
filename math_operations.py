#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Math Operations Module
Berisi fungsi-fungsi matematika dasar yang reusable
Author: Yohanes 2026
"""

def tambah(a, b):
    """
    Fungsi penjumlahan dua bilangan
    
    Args:
        a (int/float): Bilangan pertama
        b (int/float): Bilangan kedua
        
    Returns:
        int/float: Hasil penjumlahan a + b
    """
    return a + b

def kali(a, b):
    """
    Fungsi perkalian dua bilangan
    
    Args:
        a (int/float): Bilangan pertama
        b (int/float): Bilangan kedua
        
    Returns:
        int/float: Hasil perkalian a * b
    """
    return a * b

def bagi(a, b):
    """
    Fungsi pembagian dua bilangan dengan validasi pembagian nol
    
    Args:
        a (int/float): Bilangan pembilang
        b (int/float): Bilangan penyebut
        
    Returns:
        int/float/str: Hasil pembagian a / b atau error message
    """
    if b == 0:
        return "Error: Tidak bisa dibagi dengan nol"
    return a / b

def kurang(a, b):
    """
    Fungsi pengurangan dua bilangan
    
    Args:
        a (int/float): Bilangan pertama
        b (int/float): Bilangan kedua
        
    Returns:
        int/float: Hasil pengurangan a - b
    """
    return a - b

def pecah(a, b):
    """
    Fungsi khusus: a + 2 * b
    
    Args:
        a (int/float): Bilangan pertama
        b (int/float): Bilangan kedua
        
    Returns:
        int/float: Hasil dari a + 2 * b
    """
    return a + 2 * b

def kuadrat(x):
    """
    Fungsi menghitung kuadrat dari sebuah bilangan
    
    Args:
        x (int/float): Bilangan yang akan dikuadratkan
        
    Returns:
        int/float: Hasil x * x
    """
    return x * x

# Export semua fungsi untuk import *
__all__ = ['tambah', 'kali', 'bagi', 'kurang', 'pecah', 'kuadrat']
