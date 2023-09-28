import base64

encoded_data = "LHVHAHF1g/cJ2aIxFu9TyotO5x0ngAr0JbdOJi27xKJ0qDu1fBdva/xtCgj2XbDfVdmB5g=="
decoded_data = base64.b64decode(encoded_data)
print(decoded_data.decode('utf-8'))
