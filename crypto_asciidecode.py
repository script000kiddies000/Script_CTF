import binascii

chiper = 'b01001010 h69 d107 o141 o40 h6b h61 h6c h69 h61 h6e o40 b01100010 o151 o163 h61 o40 b00100000 b01101101 b01100101 b01101101 b01100010 b01100001 b01100011 b01100001 d32 o151 d110 o151 b00100000 d98 o145 h72 h61 d114 o164 h69 h20 b01101011 o141 h6c d105 d97 h6e o40 o163 h75 h64 h61 h68 h20 o155 o145 o155 o145 o143 o141 o150 o153 o141 o156 d32 h73 h6f o141 b01101100 d32 d105 o156 h69 o40 b01101011 o141 h72 o145 d110 h61 o40 h6b h61 h6c h69 h61 h6e h20 h6c h75 h61 h72 h20 h62 h69 h61 h73 h61 d32 b01101001 d110 o151 b00100000 o146 d108 b01100001 h67 o40 d67 o124 h46 b01111011 d52 o163 h63 061 d49 o61 h5f b01100100 h31 o137 o103 h34 d109 d112 o165 h72 d95 b00110100 o144 d85 h6b b01011111 d77 o64 h63 o64 h6d d95 b01100111 o64 d100 h30 o62 d95 b01011000 o104 d125 o40 b01110100 d101 h72 o151 o155 h61 h6b d97 d115 o151 o150 d32 b01111001 d97 b00100000 h73 o165 h64 o141 d104 o40 h6d o141 h75 o40 b01101101 d101 o156 h79 d101 d108 h65 h73 d97 d105 d107 h61 h6e h20 d115 o157 h61 o154 b00100000 o151 h6e d105'

plain = ""
for a in chiper.split(' '):
	if a.startswith("h"):
		plain += a[1:].decode('hex')
	if a.startswith("d"):
		plain += chr(int(a[1:]))
	if a.startswith("o"):
		plain += chr(int(a[1:], 8))
	if a.startswith ("b"):
		plain += binascii.unhexlify('%x' % int(a[1:],2))
print plain
