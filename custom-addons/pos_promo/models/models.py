# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductPromotion(models.Model):
    _name = 'product.promotion'
    _description = 'Products Promotions'
    
    name = fields.Char(string='Name', required=True)
    date_start = fields.Date(string='Start Date', required=True)
    date_end = fields.Date(string='End Date', required=True)
    amount = fields.Float(string='Amount', required=True)
    item_ids = fields.One2many('promotion.item', inverse_name='promotion_id', string='Items')
    company_id = fields.Many2one('res.company', string='Company')
    
    
class PromotionItems(models.Model):
    _name = 'promotion.item'
    _description = 'Promotion Items'
    
    product_id = fields.Many2one('product.product', string='Product')
    price_unit = fields.Float(string='Price Unit')
    quantity = fields.Float(string='Quantity')
    promotion_id = fields.Many2one('product.promotion', string='Promotion')
    
    @api.onchange('product_id')
    def _onchange_product_id(self):
        for rec in self:
            rec.price_unit = rec.product_id.list_price
    
    