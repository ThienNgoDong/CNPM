from app import app

@app.template_filter('to_uppercase')
def to_uppercase(v):
    return v.upper()