import struct

hex_str = "55 AA 03 08 45 4E 38 C2 B6 06 03 B3 06 02 AF 06 03 B5 06 06 C1 06 02 B3 06 01 BE 06 03 BE 06 02 CA C3 E9 0C 55 AA 03 08 44 4E 09 C4 C0 06 02 C3 06"
bytes_data = bytes.fromhex(hex_str.replace(" ", ""))

i = 0
found = False
while i < len(bytes_data) - 1:
    if bytes_data[i] == 0x55 and bytes_data[i+1] == 0xAA:
        found = True
        ct = bytes_data[i+2]
        ls = bytes_data[i+3]
        fsa = bytes_data[i+4] | (bytes_data[i+5] << 8)
        lsa = bytes_data[i+6] | (bytes_data[i+7] << 8)
        cs = bytes_data[i+8] | (bytes_data[i+9] << 8)
        
        sa = (fsa >> 1) / 64.0
        ea = (lsa >> 1) / 64.0
        
        print(f"\nHeader found at {i}: CT={ct}, LS={ls}, FSA={sa:.2f}, LSA={ea:.2f}, CS={hex(cs)}")
        
        print("2-byte distances:")
        for j in range(ls):
            off = i + 10 + j*2
            if off + 1 < len(bytes_data):
                dist = (bytes_data[off] | (bytes_data[off+1] << 8)) / 4.0
                print(f" Sample {j}: {dist} mm")
                
        print("3-byte intensity + distances:")
        for j in range(ls):
            off = i + 10 + j*3
            if off + 2 < len(bytes_data):
                dist = bytes_data[off+1] | (bytes_data[off+2] << 8)
                print(f" Sample {j}: dist={dist} mm")
        i += 10 + ls*3
    else:
        i += 1
if not found:
    print("No header found.")
