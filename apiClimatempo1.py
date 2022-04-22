import requests
import json

# Pesquisar id da cidade, no caso Jacareí, SP
# http://apiadvisor.climatempo.com.br/api/v1/locale/city?name=jacarei&state=SP&token=4fb763f66f8134094bbf28f4077f0636

token = "4fb763f66f8134094bbf28f4077f0636"
cidadeId = "3849"

#  Alterar id da cidade cadastrado no token. Mudanças permitidas a cada 24 horas
"""
url = "http://apiadvisor.climatempo.com.br/api-manager/user-token/"+ token + "/locales" 
payload="localeId[]=" + cidadeId
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }
iRESPONSE = requests.request("PUT", url, headers=headers, data=payload)
print(iRESPONSE.text)
"""

# Traz informações acerca do tempo no dia
"""
url = "http://apiadvisor.climatempo.com.br/api/v1/weather/locale/3849/current?token=" + str(token)
response = requests.request("GET", url)
retorno = json.loads(response.text)
print(retorno)
"""

# Traz a condição de tempo relacionado a chuva do dia 
url = "http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/3849/days/15?token=" + str(token)
response = requests.request("GET", url)
retorno = json.loads(response.text)
print("\ncidade: " + str(retorno.get('name')) + "-" + str(retorno.get('state')))
for chave in retorno['data']:
    data = chave.get('date_br')
    chuva = chave['rain']['probability']
    txtMorning = chave['text_icon']['text']['phrase']['reduced']
    tempMin = chave['temperature']['min']
    tempMax = chave['temperature']['min']
    print("data: " + str(data) + " chuva: " + str(chuva) + "%" + " temp: min(" + str(tempMin) + ") max(" + str(tempMax) + ") resumo: " + str(txtMorning) + "\n")
    break # Para retornar apenas o dia da pesquisa
    

