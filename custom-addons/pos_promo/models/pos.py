from odoo import models, fields


class PosSession(models.Model):
    _inherit = 'pos.session'

    def _pos_ui_models_to_load(self):
        result = super()._pos_ui_models_to_load()
        result += ['product.promotion', 'promotion.item']
        return result

    def _loader_params_product_promotion(self):
        today = fields.Date.today()
        return {
            'search_params': {
                'domain': [('date_start', '<=', today), ('date_end', '>=', today)],
                'fields': ['name', 'date_start', 'date_end', 'amount', 'date_to'],
            },
        }

    def _loader_params_promotion_item(self):
        return {
            'search_params': {
                'domain': [],
                'fields': ['product_id', 'price_unit', 'quantity'],
            },
        }
        
    def _get_pos_ui_product_promotion(self, params):
        return self.env['product.promotion'].search_read(**params['search_params'])

    def _get_pos_ui_promotion_item(self, params):
        return self.env['promotion.item'].search_read(**params['search_params'])
    