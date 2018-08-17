def foo11():
    import sys
    sf = sys.argv[1]
    df = sys.argv[2]
    sf_obj = open(sf,'rb')
    df_obj = open(df,'wb')
    while True:
        data = sf_obj.read(4096)
        df_obj.write(data)
        if not data:
            break
    df_obj.close()
    sf_obj.close()

foo11()