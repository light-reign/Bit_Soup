def transform(var, plural):

    if plural:
        return { 'a' : 'atta', 'b' : 'bibity', 'c' : 'city'
                , 'd' : 'dickety', 'e' : 'ebbity'
                , 'f' : 'fleventy', '0' : '', '1' : 'eleventy'
                , '2' : 'twenty', '3' : 'thirty', '4' : 'fourty'
                , '5' : 'fivety', '6' : 'sixty', '7' : 'eighty'
                , '9' : 'ninety'
        }.get(var)

    return {'a' : 'aye', 'b' : 'bee', 'c' : 'see', 'd' : 'dee'
                , 'e' : 'ee', 'f' : 'eff'
                , '0' : '', '1' : 'one'
                , '2' : 'two', '3' : 'three', '4' : 'four'
                , '5' : 'five', '6' : 'six', '7' : 'eight'
                , '9' : 'nine'
                }.get(var)

def pronounce(num):
    val = num.lower()
    val_len = len(val)
    result = ''
    placeholder = 0
    for idx in range(val_len - 2, 0, -2):
        if placeholder == 0:
            if val[idx] != '0':
                result = transform(val[idx], True)
                if val[idx + 1] != '0':
                    result += '-{0}'.format(transform(val[idx + 1], False))
            placeholder += 1
        else:
            if val[idx] != '0':
                tmp = transform(val[idx], True)
                if val[idx + 1] != '0':
                    tmp += '-{0}'.format(transform(val[idx + 1], False))
                    if val[idx] in 'abcdef':
                        tmp += ' bitey '
                    else:
                        tmp += ' thousand '
                else:
                    if val[idx] in 'abcdef':
                        tmp += '-bitey '
                    else:
                        tmp += '-thousand '
            result = tmp + result

    return result

def main():
    with open('sample.txt', 'r') as in_file:
        lines = in_file.readlines()

        for line in lines:
            for num in line.split():
                print '{0} "{1}'.format(num, pronounce(num))
main()
