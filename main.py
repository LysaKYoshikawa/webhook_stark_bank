import json
import time

import requests

from app.models.create_invoices import CreateInvoices

#invoice = CreateInvoices()


#while True:
#invoice.issue_invoices()
#time.sleep(3 * 60 * 60)  # 3 horas em segundos


# Configure a URL da API do Stark Bank (substitua pela URL real)
starkbank_api_url = 'https://sandbox.api.starkbank.com'

# Configure a chave de autenticação (substitua pela chave real)
api_key = ""

print('Aqui',api_key)

invoice_data = {
            "amount": "teste1",
            "name": "teste2",
            "tax_id": "teste3",
            "branch_code": "teste4",
            "account_number": "teste5",
        }

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

response = requests.post(starkbank_api_url, data=json.dumps(invoice_data), headers=headers)

print("O que é response: ", response)
