from openerp.osv import fields, osv
from openerp.tools.translate import _

class ship(osv.Model):
    _name = 'sales.ship'

    _columns = {
        'IMO': fields.char('IMO', size=64, required=True, translate=True),
        'hull_number': fields.char('Hull Number', size=64, required=True),
        'engine_number': fields.char('Engine Number', size=64, required=True),
        'vessel_name': fields.char('Vessel Name', size=64, required=True),
        'build_year': fields.date('Build Year', required=True),
        'ship_yard': fields.many2one('res.partner', 'Ship Yard'),
        'ship_owner': fields.many2one('res.partner', 'Ship Owner'),
        'ship_management': fields.many2one('res.partner', 'Ship Management'),
        'engine_builder': fields.many2one('res.partner', 'Engine Builder'),
    }

    _defaults = {
        'IMO': '0',
    }
    _rec_name = 'IMO'

    def _check_imo(self, cr, uid, ids, context=None):
        # if context is None:
        #     context = {}
        obj = self.browse(cr, uid, ids, context=context)
        vals = self.search(cr, uid, [], context=context)
        for value in self.browse(cr, uid, vals[:-1], context=context):
            if obj.IMO != value.IMO:
                continue
            else:
                return False
        return True

    _constraints = [
        (_check_imo, 'IMO number must be unique', ['IMO'])
    ]
    _sql_constraints = [
        ('IMO_uniq', 'unique(IMO)', "IMO must be unique!"),
    ]



class inherit_ship_order(osv.Model):
    _inherit = 'sale.order'

    def writes(self, cr, uid, ids, context=None):
        try:
            sale_order_obj = self.browse(cr, uid, ids[0], context=context)
            sale_order_line_obj = self.pool.get('sale.order.line')
            if not sale_order_obj.shipping:
                raise osv.except_osv(_('Alert: Empty Shipment Id'), _('Sorry! your shipment id field is empty'
                                               '\nAdd value to Shipment ID via Edit button'))
            for order in sale_order_obj:
                for line in order.order_line[-1]:
                    sale_order_line_obj.write(cr, uid, line.id, {'shipping_line': order.shipping.id}, context=context)
        except IndexError:
            raise osv.except_osv(_('Alert: Empty Order Lines'), _('Sorry! you havent added any product to the Order Lines yet'
                                               '\nAdd product then click on update button'))
        except TypeError:
            raise osv.except_osv(_('Alert: Empty Shipment Id'), _('Sorry! your shipment id field is empty'
                                               '\nAdd value to Shipment ID via Edit button'))
    _columns = {
        'shipping': fields.many2one('sales.ship', 'Shipment ID', required=False, onupdate="cascade", ondelete="cascade")
    }


class shipping_order_line(osv.osv):
    _inherit = 'sale.order.line'
    _columns = {
        'shipping_line': fields.many2one('sales.ship', 'Shipment ID', required=False, onupdate="cascade", ondelete="cascade" )
    }

ship()
inherit_ship_order()
shipping_order_line()
