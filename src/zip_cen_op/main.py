import sys
import mmap

CEN_FLAG = b'PK\x01\x02'
CEN_ENCRYPTED_FLAG = b'\x09\x08'
CEN_NOT_ENCRYPTED_FLAG = b'\x00\x08'


def operate(file_path, method):
    with open(file_path, 'r+b') as f:
        mm = mmap.mmap(f.fileno(), 0)
        position = 0
        while position < len(mm):
            if mm[position:position + 4] == CEN_FLAG:
                if method == 'r':
                    mm[position + 8:position + 10] = CEN_NOT_ENCRYPTED_FLAG
                elif method == 'e':
                    mm[position + 8:position + 10] = CEN_ENCRYPTED_FLAG
                position += 10
            else:
                position += 1
        mm.flush()
    print("Success!")


def main():
    if len(sys.argv) != 3 or sys.argv[1] not in ['e', 'r']:
        print("""
        Usage:
        python zip_cen_op.py <option> <file>
        option:
            r : recover a PKZip (remove encryption flag)
            e : do a fake encryption (set encryption flag)
        """)
        return

    method, file_path = sys.argv[1], sys.argv[2]
    try:
        operate(file_path, method)
    except IOError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
