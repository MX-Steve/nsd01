import sys
def unix2dos(src):
    dst_name=src+".txt"
    dst_obj=open(dst_name,'w')
    src_obj=open(src,'r')
    for line in src_obj:
        line=line.rstrip()+"/r/n"
        dst_obj.write(line)
    dst_obj.close()
    src_obj.close()

if __name__ == '__main__':
    unix2dos(sys.argv[1])