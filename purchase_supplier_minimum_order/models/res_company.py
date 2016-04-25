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

class ResCompany(models.Model):
    _inherit = 'res.company'

    purchase_min_supplier_order_mode = fields.Selection(
        lambda rs: rs._purchase_min_supplier_order_modes(),
        default=lambda rs: 'enforcing',
        required=True,
        string="Minimum PO value mode",
    )

    @api.model
    def _purchase_min_supplier_order_modes(self):
        return [
            ('enforcing', 'Enforcing'),
            ('advisory', 'Advisory'),
        ]

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
