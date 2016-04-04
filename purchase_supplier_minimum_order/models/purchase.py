# -*- coding: utf-8 -*-

##############################################################################
#
# Set minimum order on suppliers
# Copyright (C) 2016 OpusVL (<http://opusvl.com/>)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp import models, fields, api
from openerp.exceptions import UserError

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    is_below_minimum_order = fields.Boolean(
        compute='_compute_minimum_order_fields',
    )

    minimum_value = fields.Float(
        related='partner_id.minimum_purchase_order_value',
        readonly=True,
    )

    @api.one
    def wkf_confirm_order(self):
        if self.is_below_minimum_order:
            raise UserError(
                'Cannot confirm order {} because the total value is below the minimum order of {} for supplier {}'.format(
                    self.name, self.minimum_value, self.partner_id.name))
        super(PurchaseOrder, self).wkf_confirm_order()


    @api.one
    @api.depends('minimum_value', 'amount_total')
    def _compute_minimum_order_fields(self):
        self.is_below_minimum_order = self.amount_total < self.minimum_value

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
