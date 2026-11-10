# simple aes decryption brute forcer

import sys
import time
import pyAesCrypt

# helper to yield password lines from a dictionary file
def load_dictionary(dict_path):
    try:
        with open(dict_path, 'rb') as f:
            for line in f:
                yield line
    except OSError as e:
        print(f"Error: Could not read dictionary file '{dict_path}': {e}")
        sys.exit(1)

def main():
    if len(sys.argv) < 4:
        print("Usage: python pybrute.py <dictionary> <encrypted_file> <output_file>")
        sys.exit(1)

    dict_path = sys.argv[1]
    file_path = sys.argv[2]
    out_path = sys.argv[3]
    buffer_size = 64 * 1024

    print("***brute forcing file...***")
    start_time = time.time()
    
    # iterate through passwords without loading the entire file into memory
    for n, line in enumerate(load_dictionary(dict_path), 1):
        password = line.rstrip(b'\r\n').decode('utf-8', errors='ignore')
        
        try:
            pyAesCrypt.decryptFile(file_path, out_path, password, buffer_size)
            
            elapsed = time.time() - start_time
            print("  ***file decrypted***")
            print(f"password: {{{password}}}")
            print(f"time taken: {elapsed:.2f}s")
            
            if elapsed > 0:
                print(f"{n / elapsed:.2f} passwords per second")
            else:
                print("Completed instantly")
            return
            
        except ValueError:
            # pyAesCrypt raises ValueError for incorrect passwords
            continue
        except Exception as e:
            print(f"Error during decryption: {e}")
            sys.exit(1)

    print("Password not found in dictionary.")
    sys.exit(1)

if __name__ == '__main__':
    main()