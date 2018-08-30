sf = "/usr/local/bin/python3"
df = "/tmp/py"

sf_obj = open(sf,'rb')
df_obj = open(df,'wb')

while True:
    data = sf_obj.read(4096)
    if not data:
        break
    df_obj.write(data)

sf_obj.close()
df_obj.close()