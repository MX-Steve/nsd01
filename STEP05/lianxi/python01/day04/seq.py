import keyword
from  string import ascii_letters, digits

first_letter = ascii_letters + "_"
other_letter = first_letter + digits

def chek_id(idt):
        if keyword.iskeyword(idt):
            return "%s is keyword" % idt
        if idt[0] not in first_letter:
            return "1st is invalid"
        for ind , ch in enumerate(idt[1:]):
            if ch not in other_letter:
                return "char in position %s is invalid "% (ind +2)
        return "%s is valid" % idt


if __name__ == '__main__':
    idt = input("input your val:")
    print(chek_id(idt))