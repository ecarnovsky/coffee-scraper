
from src.sale_item import SaleItem
from src.email_service import EmailService

def test_send_email():

    sale_items = [SaleItem("Red Dog Bed", "$4.99", "$5.99", "#")]

    email_service  = EmailService()

    email_service.send_email(sale_items)