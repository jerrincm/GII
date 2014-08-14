from osv import osv
from osv import fields

class giicustomer(osv.osv):

    _inherit="res.partner"
 
    _columns = {
            'gii_trainee':fields.one2many('testing.testing','gii_cust_trainee','Trainee')
                        
            
            
        }
giicustomer()


