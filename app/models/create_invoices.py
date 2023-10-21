import random
import time


class CreateInvoices:

    # Função para gerar detalhes aleatórios do destinatário
    def generate_random_recipient(self):
        names = ["Alice", "Bob", "Charlie", "David", "Eve"]
        recipient = {
            "name": random.choice(names),
            "tax_id": f"{random.randint(100, 999)}.{random.randint(100, 999)}.{random.randint(100, 999)}/0001-80",
            "branch_code": "0001",
            "account_number": str(random.randint(1000000000000000, 9999999999999999)),
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
                f"Fatura criada - Destinatário: {invoice['recipient']['name']}, Valor: R${invoice['amount']:.2f}, Prazo: {invoice['due_date']}")

