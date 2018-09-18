"""
unix:文件还行符号\n
windows：文件还行符号\r\n
只需要把结尾/n 删了，加上/r/n即可
"""
import sys


def unix2dos(fname):
    dst_name = fname + '.txt'
    src_obj = open(fname)
    dst_obj = open(dst_name, 'w')
    for line in src_obj:
        line = line.rstrip() + '\r\n'
        dst_obj.write(line)
    src_obj.close()
    dst_obj.close()


if __name__ == '__main__':
    unix2dos(sys.argv[1])
