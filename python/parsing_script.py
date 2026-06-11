# Script parsing data Kelompok 04
print("Hello World dari Kelompok 04")
import os
import requests
import pandas as pd

def main():
    print("==================================================")
    print("=== PROGRAM OTOMASI PARSING DATA JSON - KELOMPOK 04 ===")
    print("==================================================")
    
    # UBAH DISINI: Gunakan endpoint utama '/products' untuk mengambil list data
    # Anda juga bisa batasi jumlahnya lewat parameter, misal: /products?limit=5
    url = "https://dummyjson.com/products?limit=5" 
    print(f"[GET REQUEST] Mengakses endpoint: {url}\n")
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            root_data = response.json()
            
            # DummyJSON mengembalikan objek dengan key "products" yang berisi list/array data
            products_list = root_data.get("products", [])
            
            print("==================================================")
            print("--- HASIL PARSING JSON DATA PRODUK (SUKSES 200 OK) ---")
            print("==================================================")
            
            # List penampung untuk DataFrame
            all_products = []
            
            # Lakukan looping untuk mengambil minimal 2 data atau lebih
            for data in products_list:
                prod_id = data.get("id", "N/A")
                title = data.get("title", "N/A")
                price = data.get("price", "N/A")
                sku = data.get("sku", "N/A")
                stock = data.get("stock", "N/A")
                tags = data.get("tags", [])
                
                print(f"ID Produk     : {prod_id}")
                print(f"Nama Produk   : {title}")
                print(f"Harga         : ${price}")
                print(f"SKU Kode      : {sku}")
                print(f"Stok Barang   : {stock} unit")
                print(f"Tags Kategori : {', '.join(tags)}")
                print("--------------------------------------------------")
                
                # Masukkan data ke dalam list penampung
                all_products.append({
                    "id": prod_id,
                    "name": title,
                    "value": price
                })
            
            print()
            # Transform to DataFrame (Sekarang berisi banyak data)
            df = pd.DataFrame(all_products)
            
            print("[PROSES] Menampilkan Struktur Data Terstruktur (DataFrame):")
            print(df.to_string(index=False))
            print()
            
            # Determine path to save output file (output/parsed_result.csv)
            script_dir = os.path.dirname(os.path.abspath(__file__))
            output_dir = os.path.join(script_dir, "output")
            os.makedirs(output_dir, exist_ok=True)
            output_file = os.path.join(output_dir, "parsed_result.csv")
            
            df.to_csv(output_file, index=False)
            print(f"[SUCCESS] Berhasil mengekspor DataFrame ke file 'output/parsed_result.csv'")
            
        else:
            print(f"[ERROR] Gagal mengakses API. Status Code: {response.status_code}")
    except Exception as e:
        print(f"[ERROR] Terjadi kesalahan saat melakukan request/parsing: {e}")

if __name__ == "__main__":
    main()