sf = "/etc/passwd"
df = "/tmp/pass"

sf_obj = open(sf,'rb')
df_obj = open(df,'wb')

while True:
    data = sf_obj.read(4096)
    if data == b'':
        break
    df_obj.write(data)

sf_obj.close()
df_obj.close()