## In this section we will be having fun with base64 data

## Decoding base64 data

# Windows
```bash
echo your_base64_encoded_data > encoded.txt
certutil -decode encoded.txt decoded.txt
type decoded.txt
```
# Linux

```bash
echo "your_base64_encoded_data" | base64 -d
```