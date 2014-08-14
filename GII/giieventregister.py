from osv import osv
from osv import fields

class giieventregistration(osv.osv):
    
        _inherit="event.registration"
 
        _columns = {
           
            'gii_attendance':fields.integer('Attendance (%)', size=64, required=False, readonly=False),
            'gii_marksobtained':fields.integer('Marks Obtained (%)', size=64, required=False, readonly=False),
            'gii_grade_event':fields.many2one('grades', 'Grade', ondelete='set null',select=True),
            'gii_event_award': fields.selection([('yes', 'Y'),('no','N')],'Award Completed'),
            'gii_certificate_issue':fields.date('Certificate Issue Date', size=64, required=False, readonly=False),
            'gii_register_events':fields.text('Remarks', size=64, required=False, readonly=False),
            'gii_location_event':fields.many2one('gii.location', 'Location', ondelete='set null',select=True)
            
            
        }
giieventregistration()



class giilocation(osv.osv):
 
    _name = 'gii.location'
    _description = 'gii.location'
 
    _columns = {
            'name':fields.char('Location', size=64, required=False, readonly=False)
        }
giilocation()