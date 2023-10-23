import random
import time
from bradocs4py import GeradorCnpj


def valid_cnpj():
    cnpj = f"{random.randint(10, 99)}.{random.randint(100, 999)}.{random.randint(100, 999)}/0001-80"
    return cnpj


class CreateInvoices:

    def __init__(self):
        self.names = ['Alice de Oliveira', 5, 'Charlie', 'David', 'Eve']
        self.id = GeradorCnpj.gerar()



    def valid_name(self):
        valid_names = []
        for name in self.names:
            if isinstance(name, str):
                valid_names.append(name)
            else:
                print(f"Erro: {name} não é uma string.")
                #raise ValueError(f"Erro: {name} não é uma string.")

        return valid_names

    # Função para gerar detalhes aleatórios do destinatário
    def generate_random_recipient(self):
        names = random.choice(self.valid_name())
        recipient = {
            "name": names,
            "tax_id": valid_cnpj(),
            "branch_code": "0001",
            "account_number": str(random.randint(1000000000000000, 9999999999999999)),
            "account_type": "payment",
            "bank_code": 260,
        }
        return recipient

    # Função para criar uma fatura aleatória
    def create_invoice(self):
        recipient = self.generate_random_recipient()
        amount = round(random.uniform(50, 500), 2)  # Valor aleatório entre R$50 e R$500
        due_date = time.strftime("%Y-%m-%d %H:%M:%S",
                                 time.gmtime(time.time() + 5 * 24 * 3600))  # Prazo de pagamento em 5 dias

        invoice = {
            "recipient": recipient,
            "amount": amount,
            "due_date": due_date
        }
        return invoice

    # Função para emitir faturas aleatórias
    def issue_invoices(self):
        num_invoices = random.randint(8, 12)
        invoices = [self.create_invoice() for _ in range(num_invoices)]

        for invoice in invoices:
            print(
                f"Fatura criada - Destinatário: {invoice['recipient']['name']}, CNPJ:  {invoice['recipient']['tax_id']}, Valor: R${invoice['amount']:.2f}, Prazo: {invoice['due_date']}")
