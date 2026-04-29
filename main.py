#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Main Program - Kalkulator Sederhana
Program utama yang menggunakan fungsi-fungsi matematika modular
Author: Yohanes 2026
"""

# Import fungsi-fungsi dari module
from math_operations import tambah, kali, bagi, pecah, kurang, kuadrat
from calculator import kalkulator

def test_basic_operations():
    """Test semua fungsi operasi dasar"""
    print("=== TESTING FUNGSI DASAR ===")
    print("5 + 3 =", tambah(5, 3))
    print("4 × 6 =", kali(4, 6))
    print("9 : 2 =", bagi(9, 2))
    print("9 + 2*2 =", pecah(9, 2))
    print("10 - 3 =", kurang(10, 3))
    print("Kuadrat dari 5 =", kuadrat(5))
    print()

def test_calculator_function():
    """Test fungsi kalkulator universal"""
    print("=== TESTING FUNGSI KALKULATOR ===")
    print("Kalkulator: 8 + 2 =", kalkulator(8, 2, "tambah"))
    print("Kalkulator: 8 * 2 =", kalkulator(8, 2, "kali"))
    print("Kalkulator: 8 - 2 =", kalkulator(8, 2, "kurang"))
    print("Kalkulator: 8 / 2 =", kalkulator(8, 2, "bagi"))
    print("Kalkulator: 8 pecah 2 =", kalkulator(8, 2, "pecah"))
    print("Kalkulator: 8 / 0 =", kalkulator(8, 0, "bagi"))
    print("Kalkulator: 8 ? 2 =", kalkulator(8, 2, "unknown"))
    print()

def test_edge_cases():
    """Test edge cases dan error handling"""
    print("=== TESTING EDGE CASES ===")
    print("Pembagian dengan nol:", bagi(10, 0))
    print("Operasi tidak dikenal:", kalkulator(5, 3, "invalid"))
    print("Negative numbers:", tambah(-5, 3))
    print("Float numbers:", kali(2.5, 4))
    print()

def interactive_calculator():
    """Kalkulator interaktif sederhana"""
    print("=== KALKULATOR INTERAKTIF ===")
    print("Ketik 'quit' untuk keluar")
    
    while True:
        try:
            cmd = input("\nMasukkan perintah (contoh: 5 + 3): ").strip()
            
            if cmd.lower() == 'quit':
                break
                
            # Parse simple expression
            parts = cmd.split()
            if len(parts) == 3:
                a = float(parts[0])
                op = parts[1]
                b = float(parts[2])
                
                result = kalkulator(a, b, op)
                print(f"Hasil: {result}")
            else:
                print("Format: angka operasi angka (contoh: 5 + 3)")
                
        except ValueError:
            print("Error: Masukkan angka yang valid!")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

def main():
    """Main function"""
    print("=" * 50)
    print("    KALKULATOR SEDERHANA - MODULAR VERSION")
    print("=" * 50)
    print("Project Kalkulator Sederhana - Yohanes 2026")
    print()
    
    # Run all tests
    test_basic_operations()
    test_calculator_function()
    test_edge_cases()
    
    # Interactive mode
    print("Ingin mencoba kalkulator interaktif? (y/n): ", end="")
    choice = input().strip().lower()
    
    if choice == 'y':
        interactive_calculator()
    
    print("\nTerima kasih telah menggunakan kalkulator modular!")

if __name__ == "__main__":
    main()
