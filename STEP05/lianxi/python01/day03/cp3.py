import sys
def cp3(src_fname,dst_fname):
    # print(sys.argv[1],sys.argv[2])
    src_fobj = open(src_fname,'rb')
    dst_fobj = open(dst_fname,'wb')
    while True:
        data = src_fobj.read(4096)
        if not data:
            break
        dst_fobj.write(data)
    src_fobj.close()
    dst_fobj.close()

cp3(sys.argv[1],sys.argv[2])