import requests
import webbrowser
from random import sample

def url_to_file(url,filename):
    result = requests.get(url)
    result.raise_for_status()
    with open(filename,'wb') as FILE:
        for chunk in result.iter_content(102400):
            FILE.write(chunk)

res = requests.get('https://en.wikipedia.org/wiki/Low-pressure_area')
text = res.text
toks = text.split('<img')[1:]
toks = [tok.split('src="')[1] for tok in toks]
toks = [tok.split('"')[0] for tok in toks]

for tok in sample(toks,3):
    if tok.startswith('//'):
        url = 'https:'+tok
    elif tok.startswith('/'):
        url = 'https://en.wikipedia.org'+tok
    elif tok.startswith('https://') or tok.startswith('http://'):
        url = tok
    else:
        url = 'https://en.wikipedia.org/wiki/'+tok
    # webbrowser.open(url)
    try:
        url_to_file(url, 'pic/'+url.split('/')[-1])
    except:
        print('Problematic url:',url)
    
    
    
    
    
    
    
    
    
    
    