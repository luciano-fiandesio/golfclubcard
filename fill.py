#!/usr/bin/env python3

import pypdftk
import sys
import os.path

def exists(path):
    if not os.path.exists(path):
        print ("File [" + path_to_file + "] does not exist")
        sys.exit()

if len(sys.argv) < 3:
    print('Provide name file and pdf file') 
    sys.exit()

if not os.path.exists('gen'):
    os.makedirs('gen')

path_to_file=sys.argv[1]
path_to_pdf=sys.argv[2]

exists(path_to_file)
exists(path_to_pdf)

nomi = open(path_to_file, 'r')
for line in nomi:
    name = line.strip().upper()

    datas = {
        'name_lastname': name,
        'Text1': name
    }
#pypdftk.dump_data_fields('/Users/luciano/Downloads/graziano/card.pdf')
#print(i)
    pypdftk.fill_form(path_to_pdf, datas, 'gen/card_' + name.replace(' ', '_') + '.pdf')
    print(name + " -> ok!")

