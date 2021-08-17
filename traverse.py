import fileinput
import sys
import re


fname = str(sys.argv[1])
search_key = str(sys.argv[2])
api_name = str(sys.argv[3])

#file_path = 'index.html'
#search_text = 'INSERT V1'
#new_text = str(sys.argv[1])
#new_text = 'https://cies1zmpr4.execute-api.us-east-1.amazonaws.com/'
#new_text = 'https://nvyonspg4l.execute-api.us-east-2.amazonaws.com/multimigrate?token="+token.value+"&user="+username.value+"&phone="+phone.value'



def replace_in_file(file_path, search_text, new_text):
    with fileinput.input(file_path, inplace=True) as f:
        for line in f:
            new_line = line.replace(search_text, new_text)
            print(new_line, end='')

replace_in_file(fname,search_key,api_name)
