# simple aes decryption brute forcer

import sys
import time
import pyAesCrypt

def main():
    if len(sys.argv) < 4:
        print("Usage: python pybrute.py <dictionary> <encrypted_file> <output_file>")
        sys.exit(1)

    dict_path = sys.argv[1]
    file_path = sys.argv[2]
    out_path = sys.argv[3]
    buffer_size = 64 * 1024

    try:
        with open(dict_path, 'rb') as f:
            passwords = f.readlines()
    except OSError as e:
        print(f"Error: Could not read dictionary file '{dict_path}': {e}")
        sys.exit(1)

    print("***brute forcing file...***")
    start_time = time.time()
    
    for n, password in enumerate(passwords):
        passf = password.rstrip(b'\r\n')
        try:
            password_str = passf.decode('utf-8', errors='ignore')
            pyAesCrypt.decryptFile(file_path, out_path, password_str, buffer_size)
            
            elapsed = time.time() - start_time
            print("  ***file decrypted***")
            print(f"password: {{{password_str}}}")
            print(f"time taken: {elapsed:.2f}s")
            
            if elapsed > 0:
                print(f"{n / elapsed:.2f} passwords per second")
            else:
                print("Completed instantly")
            return
        except ValueError:
            # pyAesCrypt raises ValueError on incorrect password
            continue
        except Exception as e:
            # catch other unexpected issues like missing files during decrypt
            print(f"Error during decryption: {e}")
            sys.exit(1)

    print("Password not found in dictionary.")
    sys.exit(1)

if __name__ == '__main__':
    main()