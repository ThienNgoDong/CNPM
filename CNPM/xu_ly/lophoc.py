import sys  
sys.path.append('/Users/Dang Thang/Desktop/Git-project/CNPM/CNPM')  
from app import app,db
from models import ListClass


def cap_nhat_si_so(lop, sl_them_giam=1):
    try:
        lop = db.session.query(ListClass).filter(ListClass.id==lop).one()
        lop.siso += sl_them_giam
        db.session.flush()
        db.session.commit()
    except:
        db.session.rollback()
        return False
    return True

    
    