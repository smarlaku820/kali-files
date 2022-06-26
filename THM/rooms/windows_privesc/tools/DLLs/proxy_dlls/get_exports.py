import pefile
import argparse

parser = argparse.ArgumentParser(description='Target DLL.')
parser.add_argument('--target', required=True, type=str,help='Target DLL')
parser.add_argument('--originalPath', required=True, type=str,help='Original DLL path')

args = parser.parse_args()

target = args.target
original_path = args.originalPath.replace('\\','/')

dll = pefile.PE(target)

print("EXPORTS", end="\r\n")

for export in dll.DIRECTORY_ENTRY_EXPORT.symbols:
    if export.name:
        print(f"    {export.name.decode()}={original_path}.{export.name.decode()} @{export.ordinal}", end="\r\n")
