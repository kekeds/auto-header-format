import pyperclip, json

fucked_headers=pyperclip.paste()
headers={}

for header in fucked_headers.splitlines():
    if not header[0:1]==":" and not "content-length" in header:#Fuck content length
        first,second=header.split(": ")
        headers[first]=second

pyperclip.copy(json.dumps(headers, indent=4))