hex_str = "55 AA 03 08 45 4E 38 C2 B6 06 03 B3 06 02 AF 06 03 B5 06 06 C1 06 02 B3 06 01 BE 06 03 BE 06 02 CA C3 E9 0C 55 AA 03 08 44 4E 09 C4 C0 06 02 C3 06"
import struct
b = bytes.fromhex(hex_str.replace(" ", ""))

saRaw = b[6] | (b[7]<<8)
eaRaw = b[32] | (b[33]<<8)

sa = (saRaw - 0xA000) / 64.0
ea = (eaRaw - 0xA000) / 64.0

print(f"Start Angle: {sa}, End Angle: {ea}")
diff = ea - sa
print(f"Diff: {diff}")
