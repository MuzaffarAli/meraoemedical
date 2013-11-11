# -*- coding: utf-8 -*-
#/#############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2004-TODAY Tech-Receptives(<http://www.techreceptives.com>)
#    Special Credit and Thanks to Thymbra Latinoamericana S.A.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#/#############################################################################
from osv import osv
from osv import fields

  

class OeMedicalAppointment(osv.Model):
    def autoApp(self,cr,uid,ids,appointment_type,context=None):
		if appointment_type:
			
			x=appointment_type
			if x == "newcase":
				
				return {'value':{'doctor': {"LOL","rofl"}}}
		
		return {'value':{'doctor':''}}
		
    
  
  
    _name = 'oemedical.appointment'

    _columns = {
        'consultations': fields.many2one('product.product',
                                         string='Consultation Services',
                                          help='Consultation Services'),
        'patient_id': fields.many2one('oemedical.patient', string='Patient',
                                   required=True, select=True,
                                   help='Patient Name'),
        'name': fields.char(size=256, string='Appointment ID', readonly=True),
        'appointment_date': fields.datetime(string='Date and Time'),
        'duration': fields.float('Duration'),
        'doctor': fields.char(string="Physician", size=50),
        'comments': fields.text(string='Comments'),
        'appointment_type': fields.selection([('newcase', 'New Case'),
											 ('ontreatment', 'On Treatment')], 
											 string='Type'),
        'institution': fields.many2one('res.partner',
                                       string='Health Center',
                                       help='Medical Center'),
        'urgency': fields.selection([
            ('a', 'Normal'),
            ('b', 'Emergency'), ],
            string='Urgency Level'),
        'speciality': fields.many2one('oemedical.specialty',
                                      string='Specialty', 
                                      help='Medical Specialty / Sector'),
    }
    
    _defaults = {
         'name': lambda obj, cr, uid, context: 
            obj.pool.get('ir.sequence').get(cr, uid, 'oemedical.appointment'),
		}

OeMedicalAppointment()
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

"""'doctor': fields.many2one('oemedical.physician',
                                  string='Physician',select=True, 
                                  help='Physician\'s Name'),"""
