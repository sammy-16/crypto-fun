import base64

encoded_data = "OB3W4LTDN5WGYZLHMV5WG6KPIRQW63CWKRZHU2CWHBUDSMRQMVUXMURZNFREIMROKFMDE52TJZ5ES6SXPUFA===="
decoded_data = base64.b32decode(encoded_data)
print(decoded_data.decode('utf-8'))
