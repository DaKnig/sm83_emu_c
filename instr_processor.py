# if for some unholy reason you wanna get it from the web directly: 
# import requests
# url = "https://gbdev.io/gb-opcodes/Opcodes.json"
# opcode_table = requests.get(url).json()
# #print(
# print(opcode_table.keys())

import json
opcode_table = json.load(open('Opcodes.json'))

unprefixed = [None] * 256

for k,v in opcode_table["unprefixed"].items():
    k = int(k, base=16)
    assert (unprefixed[k] == None) # never invoked on this hex code
    unprefixed[k] = v

prefixed = [None] * 256

for k,v in opcode_table["cbprefixed"].items():
    k = int(k, base=16)
    assert (prefixed[k] == None) # never invoked on this hex code
    prefixed[k] = v

def print_things():
    to_print = "#define UNPREFIXED(XX) \\\n"
    for i, instr in enumerate(unprefixed):
        if not instr:
            raise Exception(
                f"Message: found an invalid instruction: {instr}")
            continue
        
        to_print += "    XX( "
        to_print += '0x%02x, ' % i
        to_print += instr['mnemonic']

        if instr['operands']:
            to_print += '_'+'_'.join( map(lambda x: x['name'],
                                    instr['operands']))
        to_print += ',' + ' '*(28-len(to_print.split('\n')[-1]))
        
        to_print += '%d' % instr['bytes']

        if len(instr['cycles']) == 1:
            to_print += ', %d' % (instr['cycles'][0]//4)
        elif len(instr['cycles']) == 2:
            to_print += ', 0' # special value
        else:
            raise(Excpetion("wrong number of cycles"))
        to_print += ')' + ' '*(50 - len(to_print.split('\n')[-1]))+ '\\\n'
    return to_print
if __name__ == "__main__":
    print(print_things())
