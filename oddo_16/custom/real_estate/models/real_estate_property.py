from odoo import models, fields, exceptions
from dateutil.relativedelta import relativedelta



class RealEstateProperty(models.Model):
    _name = 'real.estate.property'
    _description = 'Property Details'

    name = fields.Char(string="Title", required=True, help='Enter Name')
    description = fields.Text(string='Description', help='Enter Property in Details')
    postcode = fields.Char(string='Postcode', required=True, help='Enter your PostalCode')
    date_availability = fields.Date("Available From", default=lambda self: self._default_date_availability(),
                                    copy=False)
    expected_price = fields.Float("Expected Price", required=True)
    selling_price = fields.Float("Selling Price", copy=False, readonly=True)
    bedrooms = fields.Integer("Bedrooms", default=2)
    living_area = fields.Integer("Living Area (sqm)")
    facades = fields.Integer("Facades")
    garage = fields.Boolean("Garage")
    garden = fields.Boolean("Garden")
    garden_area = fields.Integer("Garden Area (sqm)")
    garden_orientation = fields.Selection(
        selection=[
            ("N", "North"),
            ("S", "South"),
            ("E", "East"),
            ("W", "West"),
        ],
        string="Garden Orientation",
    )
    state = fields.Selection(
        selection=[
            ("new", "New"),
            ("offer_received", "Offer Received"),
            ("offer_accepted", "Offer Accepted"),
            ("sold", "Sold"),
            ("canceled", "Canceled"),
        ],
        string="Status",
        required=True,
        copy=False,
        default="new",
    )
    active = fields.Boolean("Active", default=True)

    # Action method
    def action_sold(self):
        if "canceled" in self.mapped("state"):
            raise UserError("Canceled properties cannot be sold.")
        return self.write({"state": "sold"})

    def action_cancel(self):
        if "sold" in self.mapped("state"):
            raise UserError("Sold properties cannot be canceled.")
        return self.write({"state": "canceled"})

    # default method
    def _default_date_availability(self):
        return fields.Date.context_today(self) + relativedelta(months=3)
