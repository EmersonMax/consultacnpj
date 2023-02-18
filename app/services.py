
import http.client
import json


def apicnpj(cnpj, estado):
    conn = http.client.HTTPSConnection("api.cnpja.com")
    payload = ''
    headers = {
    'Authorization': '8471c4b6-9394-46dc-b8d4-1e76e4614eb0-045d760c-1a95-4481-95eb-c6187bfcc586'
    }
    
    try:
        conn.request("GET", f"/office/{cnpj}?registrations={estado}", payload, headers)
        res = conn.getresponse()
        data = res.read()
        resp_api = json.loads(data.decode("utf-8"))
        #print(data[0].registrations)
        ie=resp_api['registrations'][0]['number']
        nome=resp_api['company']['name']
        status=resp_api['status']['text']
        
        dados = {
            'cnpj': cnpj,
            'nome': nome,
            'IE': ie,
            'status':status,
            'cep':resp_api['address']['zip'],
            'bairro':resp_api['address']['district'],
            'rua': resp_api['address']['street'],
            'numero':resp_api['address']['number'],
            'estado':resp_api['registrations'][0]['state'],
            'cnae': resp_api['mainActivity']['id'],
            'cnae_desc': resp_api['mainActivity']['text'],
        }
    except:
         dados = {
            ''
        }
    return (dados)
