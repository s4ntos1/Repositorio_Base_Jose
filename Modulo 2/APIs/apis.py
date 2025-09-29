import requests
response = requests.get('https://github.com/paunabuseta')
resposta=(response.status_code)
if resposta<=299:
 print(f"seu site está funcionando  {resposta}")
else :
 print(f"seu site está errado  {resposta}")
