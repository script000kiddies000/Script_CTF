newmap = {
4: "a",
5: "b",
6: "c",
7: "d",
8: "e",
9: "f",
10: "g",
11: "h",
12: "i",
13: "j",
14: "k",
15: "l",
16: "m",
17: "n",
18: "o",
19: "p",
20: "q",
21: "r",
22: "s",
23: "t",
24: "u",
25: "v",
26: "w",
27: "x",
28: "y",
29: "z",
30: "1",
31: "2",
32: "3",
33: "4",
34: "5",
35: "6",
36: "7",
37: "8",
38: "9",
39: "0",
44: " ",
45:"-",
47:"{",
48:"}",
56:"/",
55:"eror",
51:"eror",
}



myKeys = open('capdata')
i = 1
aw = ""
for line in myKeys:
  bytesArray = bytearray.fromhex(line.strip().split(':')[2])
  # print "Line Number: " + str(line.strip().split(':')[2])
  for byte in bytesArray:
    if byte != 0:
       keyVal = int(byte)
  if keyVal in newmap:
     aw+=newmap[keyVal]
  else:
     print "Tidak ada: " + str(keyVal)
  i+=1
print aw