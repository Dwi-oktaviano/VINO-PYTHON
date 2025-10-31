

tuple_1 = (2,3,4)
tuple_2 = ("gino", "tari")
tuple_3 = (24, False, "hallo")
print(tuple_1, tuple_2, tuple_3)

#fungsi tuple
alphabets = tuple("abcdefgh")
print(alphabets)

#list ke tuple
number = tuple([1,2,3,4])
print(number)

#range ke tuple
r = range(0,100)
rtuple = tuple(r)
print(rtuple)

#tipe data dictionary
biodata_1 = {
    "nama": "vino",
    "umur": "16",
    "hobi": "main bola"
}

biodata_1 = {
    "nama": "vino",
    "umur": "16",
    "hobi": "main bola"
}

print("nama: %s" % (biodata_1)["nama"])
print("umur: %s" % (biodata_1)["umur"])
print("hobi: %s" % (biodata_1)["hobi"])

