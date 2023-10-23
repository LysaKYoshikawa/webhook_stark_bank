import requests
import json
import random
import time

class Invoices:

    starkbank_api_url = 'https://api.starkbank.com/v2/invoices'
    # Configure a URL da API do Stark Bank (substitua pela URL real)

    # Configure a chave de autenticação (substitua pela chave real)
    api_key = ""


    # Função para gerar detalhes aleatórios do destinatário
    def generate_random_recipient(self):
        names = ["Alice", "Bob", "Charlie", "David", "Eve"]
        return {
            "name": random.choice(names),
            "tax_id": f"{random.randint(100, 999)}.{random.randint(100, 999)}.{random.randint(100, 999)}/0001-80",
            "branch_code": "0001",
            "account_number": str(random.randint(1000000000000000, 9999999999999999)),
        }

    # Função para criar uma fatura
    def create_invoice(self):

        recipient = self.generate_random_recipient()
        amount = round(random.uniform(50, 500), 2)  # Valor aleatório entre R$50 e R$500

        # Configurar os dados da fatura
        invoice_data = {
            "amount": amount,
            "name": recipient["name"],
            "tax_id": recipient["tax_id"],
            "branch_code": recipient["branch_code"],
            "account_number": recipient["account_number"],
        }

        return invoice_data

    # Realizar a solicitação HTTP para criar a fatura
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }

    response = requests.post(starkbank_api_url, data=json.dumps(invoice_data), headers=headers)

    if response.status_code == 200:
        print(f"Fatura criada - Valor: R${amount:.2f}")
    else:
        print(f"Erro ao criar a fatura - Código de status: {response.status_code}")
