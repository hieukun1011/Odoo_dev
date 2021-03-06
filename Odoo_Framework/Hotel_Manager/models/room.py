from odoo import models, fields, api


class Room(models.Model):
    _name = 'room'
    _rec_name = 'name_room'

    avatar_room = fields.Binary(string='Image')
    name_room = fields.Char(string='Name')
    type_room = fields.Selection(selection=[('single', 'Single'),
                                            ('double', 'Double')],
                                 string='Type Room', default='single')
    price_room = fields.Float(string='Price ($)')
    state_room = fields.Selection(selection=[('available', 'Available'),
                                             ('confirmed', 'Confirmed'),
                                             ('operational', 'Operational')],
                                  string='State', default='available')
    description = fields.Text(string='Description')
    booking_ids = fields.Many2one(comodel_name='booking', string='Booking')

    @api.onchange('type_room')
    def onchange_price_room(self):
        if self.type_room == 'single':
            self.price_room = 30
        # elif self.price_room == 'double':
        #     self.price_room = 50
        else:
            self.price_room = 50
