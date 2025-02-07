import hashlib
import sys 
        
def calculate_hash(file, algorithm = "sha256"):
    hash_function = getattr(hashlib, algorithm)()
    with open(file, "rb") as f:
        while chunk := f.read(4096):
            hash_function.update(chunk)
    return hash_function.hexdigest()
    
def compare_hash_file(file1, file2, algorithm="sha256"):
    file_1_hash = calculate_hash(file1, algorithm) 
    file_2_hash = calculate_hash(file2, algorithm)
    
    if file_1_hash == file_2_hash:
        print(f"File 1 and File 2's hashes are identical meaning none of the files have been tampered with.\nThey passed the file integrity check!")
    else:
        print(f"File 1 and File 2's hashes are NOT identical.\nThis either means they are completely different files, or one of the files has been tampered with.\nThey do not pass the file integrity check.")
        
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("The format to execute this is as followed:\n'py fileintegritychecker file1 file2' for Windows\n'python fileintegritychecker file1 file2' for Mac")
    else:
        compare_hash_file(sys.argv[1], sys.argv[2])
        
# Make sure to copy path of the fileintegrityfolder and set it as directory (cd "path") before running the program