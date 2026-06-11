import os
import requests
import pandas as pd

def main():
    print("==================================================")
    print("=== PROGRAM OTOMASI PARSING DATA JSON - KELOMPOK 04 ===")
    print("==================================================")
    url = "https://dummyjson.com/products/2"
    print(f"[GET REQUEST] Mengakses endpoint: {url}\n")
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            
            # Safe data extraction using .get() to avoid KeyError
            prod_id = data.get("id", "N/A")
            title = data.get("title", "N/A")
            price = data.get("price", "N/A")
            sku = data.get("sku", "N/A")
            stock = data.get("stock", "N/A")
            tags = data.get("tags", [])
            
            print("==================================================")
            print("--- HASIL PARSING JSON DATA PRODUK (SUKSES 200 OK) ---")
            print("==================================================")
            print(f"ID Produk     : {prod_id}")
            print(f"Nama Produk   : {title}")
            print(f"Harga         : ${price}")
            print(f"SKU Kode      : {sku}")
            print(f"Stok Barang   : {stock} unit")
            print(f"Tags Kategori : {', '.join(tags)}")
            print("--------------------------------------------------\n")
            
            # Transform to DataFrame
            df = pd.DataFrame([{
                "id": prod_id,
                "name": title,
                "value": price
            }])
            
            print("[PROSES] Menampilkan Struktur Data Terstruktur (DataFrame):")
            print(df.to_string(index=False))
            print()
            
            # Determine path to save output file (output/parsed_result.csv)
            script_dir = os.path.dirname(os.path.abspath(__file__))
            output_dir = os.path.join(script_dir, "..", "output")
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
