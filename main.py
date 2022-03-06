from urllib import response
from data import request_get
import templates as t

def build_html(url):
    response = request_get(url)
    texto = ''
    for resultados in response:
        texto += t.elem_template.substitute(
            titulo_es = resultados['name']['spanish'],
            title_en = resultados ['name']['english'],
            url = resultados ['images']['main']
        )
    return t.html_template.substitute(body=texto)

if __name__=='__main__':
    html = build_html('https://aves.ninjas.cl/api/birds')
    with open('output.html', 'w') as f:
        f.write(html)