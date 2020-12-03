
from models import Product

def read_products():
    return Product.query.all()