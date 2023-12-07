from odoo import models, fields


class HotelRestaurant(models.Model):
    _name = 'hotel.restaurant'
    _description = 'This models is demo data for restaurant'

    food_name = fields.Char(string='Food Item')
    food_price = fields.Integer(string='Price')