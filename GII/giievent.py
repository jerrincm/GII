from osv import osv
from osv import fields

class giievent(osv.osv):

    _inherit="event.event"
 
    _columns = {
            'gii_project_id':fields.many2one('project.project','Project', ondelete='set null'),
            'gii_public':fields.boolean('Public',required=False, readonly=False),
            'gii_lang':fields.many2one('gii.language','Language', ondelete='set null'),
            'gii_result_id':fields.one2many('result','product_id_event','Result'),
            'gii_session_id':fields.one2many('session','product_id_event','Session Planning'),
            'gii_sessionplanning_id':fields.one2many('sessionplanning','product_id_event','Session Planning'),
            'gii_feedback_id':fields.one2many('feeddback','product_id_event','Feedback'),
            'gii_comment':fields.text('Tutors Comment', size=64, required=False, readonly=False),
            
           #  'gii_name':fields.char('Event Id', size=64, required=False, readonly=False),
            'gii_iq1': fields.selection([('1-Disagree Strongly', '1-Disagree Strongly'),('2-Disagree','2-Disagree'),('3-Neither Agree nor Disagree','3-Neither Agree nor Disagree'),('4-Agree','4-Agree'),('5-Agree Strongly','5-Agree Strongly')],'Overall, how did the course meet your expectations?'),
            'gii_iq2': fields.selection([('1-Disagree Strongly', '1-Disagree Strongly'),('2-Disagree','2-Disagree'),('3-Neither Agree nor Disagree','3-Neither Agree nor Disagree'),('4-Agree','4-Agree'),('5-Agree Strongly','5-Agree Strongly')],'Did the course content meet the learning objectives stated ?'),
            'gii_iq3': fields.selection([('1-Disagree Strongly', '1-Disagree Strongly'),('2-Disagree','2-Disagree'),('3-Neither Agree nor Disagree','3-Neither Agree nor Disagree'),('4-Agree','4-Agree'),('5-Agree Strongly','5-Agree Strongly')],'How would you evaluate the quality of course material ? (text books, slides, other learning tools)'),
            'gii_iq4': fields.selection([('1-Disagree Strongly', '1-Disagree Strongly'),('2-Disagree','2-Disagree'),('3-Neither Agree nor Disagree','3-Neither Agree nor Disagree'),('4-Agree','4-Agree'),('5-Agree Strongly','5-Agree Strongly')],'Were the timing and length of the course adequate ?'),
            'gii_iq5': fields.selection([('1-Disagree Strongly', '1-Disagree Strongly'),('2-Disagree','2-Disagree'),('3-Neither Agree nor Disagree','3-Neither Agree nor Disagree'),('4-Agree','4-Agree'),('5-Agree Strongly','5-Agree Strongly')],'Did the sessions start and finish on time?'),
            
            'gii_i1': fields.selection([('1-Disagree Strongly', '1-Disagree Strongly'),('2-Disagree','2-Disagree'),('3-Neither Agree nor Disagree','3-Neither Agree nor Disagree'),('4-Agree','4-Agree'),('5-Agree Strongly','5-Agree Strongly')],'Were the registration procedures efficient and easy to complete?'),
            'gii_i2': fields.selection([('1-Disagree Strongly', '1-Disagree Strongly'),('2-Disagree','2-Disagree'),('3-Neither Agree nor Disagree','3-Neither Agree nor Disagree'),('4-Agree','4-Agree'),('5-Agree Strongly','5-Agree Strongly')],'How well did the management and admin staff communicate with you throughout the course?'),
            'gii_i3': fields.selection([('1-Disagree Strongly', '1-Disagree Strongly'),('2-Disagree','2-Disagree'),('3-Neither Agree nor Disagree','3-Neither Agree nor Disagree'),('4-Agree','4-Agree'),('5-Agree Strongly','5-Agree Strongly')],'Was the information provided about the course easily available, adequate and accurate?'),
            'gii_i4': fields.selection([('1-Disagree Strongly', '1-Disagree Strongly'),('2-Disagree','2-Disagree'),('3-Neither Agree nor Disagree','3-Neither Agree nor Disagree'),('4-Agree','4-Agree'),('5-Agree Strongly','5-Agree Strongly')],'Was the classroom well equipped, clean and seating adequate?'),
            'gii_i5': fields.selection([('1-Disagree Strongly', '1-Disagree Strongly'),('2-Disagree','2-Disagree'),('3-Neither Agree nor Disagree','3-Neither Agree nor Disagree'),('4-Agree','4-Agree'),('5-Agree Strongly','5-Agree Strongly')],'Were the refreshments provided adequate?'),
            
            'gii_t1': fields.selection([('1-Disagree Strongly', '1-Disagree Strongly'),('2-Disagree','2-Disagree'),('3-Neither Agree nor Disagree','3-Neither Agree nor Disagree'),('4-Agree','4-Agree'),('5-Agree Strongly','5-Agree Strongly')],'Was the instructor confident and knowledgeable about the subject?'),
            'gii_t2': fields.selection([('1-Disagree Strongly', '1-Disagree Strongly'),('2-Disagree','2-Disagree'),('3-Neither Agree nor Disagree','3-Neither Agree nor Disagree'),('4-Agree','4-Agree'),('5-Agree Strongly','5-Agree Strongly')],'Did the instructor present the course in an interesting and stimulating way?'),
            'gii_t3': fields.selection([('1-Disagree Strongly', '1-Disagree Strongly'),('2-Disagree','2-Disagree'),('3-Neither Agree nor Disagree','3-Neither Agree nor Disagree'),('4-Agree','4-Agree'),('5-Agree Strongly','5-Agree Strongly')],'Did the instructor communicate well with candidates?'),
            'gii_t4': fields.selection([('1-Disagree Strongly', '1-Disagree Strongly'),('2-Disagree','2-Disagree'),('3-Neither Agree nor Disagree','3-Neither Agree nor Disagree'),('4-Agree','4-Agree'),('5-Agree Strongly','5-Agree Strongly')],'Did the instructor encourage questions and discussion?'),
            'gii_t5': fields.selection([('1-Disagree Strongly', '1-Disagree Strongly'),('2-Disagree','2-Disagree'),('3-Neither Agree nor Disagree','3-Neither Agree nor Disagree'),('4-Agree','4-Agree'),('5-Agree Strongly','5-Agree Strongly')],'Did the instructor respond well and clearly to  questions?'),
            'gii_t6': fields.selection([('1-Disagree Strongly', '1-Disagree Strongly'),('2-Disagree','2-Disagree'),('3-Neither Agree nor Disagree','3-Neither Agree nor Disagree'),('4-Agree','4-Agree'),('5-Agree Strongly','5-Agree Strongly')],'Overall, how would you rate the instructor for this subject?'),
            'gii_tutor1_id':fields.many2one('hr.employee','Tutor 1', ondelete='set null'),
            
            'gii_tu1': fields.selection([('1-Disagree Strongly', '1-Disagree Strongly'),('2-Disagree','2-Disagree'),('3-Neither Agree nor Disagree','3-Neither Agree nor Disagree'),('4-Agree','4-Agree'),('5-Agree Strongly','5-Agree Strongly')],'Was the instructor confident and knowledgeable about the subject?'),
            'gii_tu2': fields.selection([('1-Disagree Strongly', '1-Disagree Strongly'),('2-Disagree','2-Disagree'),('3-Neither Agree nor Disagree','3-Neither Agree nor Disagree'),('4-Agree','4-Agree'),('5-Agree Strongly','5-Agree Strongly')],'Did the instructor present the course in an interesting and stimulating way?'),
            'gii_tu3': fields.selection([('1-Disagree Strongly', '1-Disagree Strongly'),('2-Disagree','2-Disagree'),('3-Neither Agree nor Disagree','3-Neither Agree nor Disagree'),('4-Agree','4-Agree'),('5-Agree Strongly','5-Agree Strongly')],'Did the instructor communicate well with candidates?'),
            'gii_tu4': fields.selection([('1-Disagree Strongly', '1-Disagree Strongly'),('2-Disagree','2-Disagree'),('3-Neither Agree nor Disagree','3-Neither Agree nor Disagree'),('4-Agree','4-Agree'),('5-Agree Strongly','5-Agree Strongly')],'Did the instructor encourage questions and discussion?'),
            'gii_tu5': fields.selection([('1-Disagree Strongly', '1-Disagree Strongly'),('2-Disagree','2-Disagree'),('3-Neither Agree nor Disagree','3-Neither Agree nor Disagree'),('4-Agree','4-Agree'),('5-Agree Strongly','5-Agree Strongly')],'Did the instructor respond well and clearly to  questions?'),
            'gii_tu6': fields.selection([('1-Disagree Strongly', '1-Disagree Strongly'),('2-Disagree','2-Disagree'),('3-Neither Agree nor Disagree','3-Neither Agree nor Disagree'),('4-Agree','4-Agree'),('5-Agree Strongly','5-Agree Strongly')],'Overall, how would you rate the instructor for this subject?'),
            'gii_tutor2_id':fields.many2one('hr.employee','Tutor 2', ondelete='set null'),
            
            'gii_comments1':fields.text('What was the most useful part of the course?', size=64, required=False, readonly=False),
            'gii_comments2':fields.text('What was the least useful part of the course?', size=64, required=False, readonly=False),
            'gii_comments3':fields.text('How did you hear about the course?', size=64, required=False, readonly=False),
            'gii_comments4':fields.text('Are there any other subjects you would like to study with us?', size=64, required=False, readonly=False),
            'gii_comments5':fields.text('Do you have any suggestions for us to improve marketing and increase participation?', size=64, required=False, readonly=False),
            'gii_comments6':fields.text('Any other comments or suggestions would you like to make?', size=64, required=False, readonly=False),
            
            'productid_event':fields.many2one('product.product', 'Sale Order', ondelete='set null',select=True)
            
              }
giievent()

class giiresult(osv.osv):

    _name = 'result'
    _description = 'result'
 
    _columns = {
            'name':fields.char('Reg No', size=64, required=False, readonly=False),
            'gii_customer_id':fields.many2one('res.partner','Name', ondelete='set null'),
            'gii_attendance_event':fields.char('Attendance', size=64, required=False, readonly=False),                                    
            'gii_mark_event':fields.integer('Exam Marks', size=64, required=False, readonly=False),
            'gii_grade_event': fields.selection([('p', 'P'),('m','M'),('d','D'),('f','F')],'Grade'),
            'gii_awardcompleted_event': fields.selection([('yes', 'Y'),('no','N')],'Award Completed'),
            'gii_certificate_event':fields.date('Certificate Issue Date', size=64, required=False, readonly=False),            
            'gii_remarks_event':fields.char('Remarks', size=64, required=False, readonly=False),            
            'product_id_event':fields.many2one('event.event', 'Sale Order', ondelete='set null',select=True)
            
        }
giiresult()


class giisession(osv.osv):

    _name = 'session'
    _description = 'session'
 
    _columns = {
            'name':fields.date('Session Date', size=64, required=False, readonly=False),
            'gii_timestart':fields.many2one('time','Time Starts', ondelete='set null'),
            'gii_timeend':fields.many2one('time','Time Ends', ondelete='set null'),
            'gii_tutor':fields.many2one('hr.employee','Lecturer', ondelete='set null'),
            'gii_subject':fields.char('Subject', size=64, required=False, readonly=False),
            'gii_remarks':fields.text('Remarks', size=64, required=False, readonly=False),            
            'product_id_event':fields.many2one('event.event', 'Sale Order', ondelete='set null',select=True),
            'gii_sessionlanning_id':fields.many2one('sessionplanning', 'Sale Order', ondelete='set null',select=True)
        }
giisession()

class sessionplanning(osv.osv):
 
    _name = 'sessionplanning'
    _description = 'sessionplanning'
 
    _columns = {
            'gii_holi':fields.boolean('Skip Holidays',required=False, readonly=False),            
            'gii_dur_id':fields.many2one('gii.duration','Duration (hours)', ondelete='set null'),
            'gii_freq_id':fields.many2one('frequency','Frequency', ondelete='set null'),
            'gii_starttime_id':fields.many2one('time','Session Starting Time', ondelete='set null'),
            'gii_endtime_id':fields.many2one('time','Session Ending Time', ondelete='set null'),
            'gii_breaktime_id':fields.many2one('gii.duration','Add Break Time (minutes)', ondelete='set null'),
            'gii_session_id':fields.one2many('session','product_id_event','Session Planning'),
            'gii_sun':fields.boolean('SUN',required=False, readonly=False),
            'gii_mon':fields.boolean('MON',required=False, readonly=False),
            'gii_tue':fields.boolean('TUE',required=False, readonly=False),
            'gii_wed':fields.boolean('WED',required=False, readonly=False),
            'gii_thu':fields.boolean('THU',required=False, readonly=False),
            'gii_fri':fields.boolean('FRI',required=False, readonly=False),
            'gii_sat':fields.boolean('SAT',required=False, readonly=False),
            'product_id_event':fields.many2one('event.event', 'Sale Order', ondelete='set null',select=True)
            
        }
sessionplanning()

