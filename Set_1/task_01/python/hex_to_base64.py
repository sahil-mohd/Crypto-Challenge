import binascii

hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

bin_string = binascii.a2b_hex(hex_string)
base64_string = binascii.b2a_base64(bin_string)

print(base64_string)