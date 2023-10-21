from datetime import time

from app.models.create_invoices import CreateInvoices



invoice = CreateInvoices()

while True:
    # Agende a execução a cada 3 horas
    invoice.issue_invoices()
    time.sleep(3 * 60 * 60)  # 3 horas em segundos
