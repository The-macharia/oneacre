/** @odoo-module **/

import PosComponent from 'point_of_sale.PosComponent';
import ProductScreen from 'point_of_sale.ProductScreen';
import Registries from 'point_of_sale.Registries';
import { useListener } from "@web/core/utils/hooks";

export class OffersButton extends PosComponent {
    setup() {
        super.setup();
        useListener('click', this.onClick);
    }

    async onClick() {
        console.log('this.env.pos', this.env.pos)
        let { confirmed, payload: code } = await this.showPopup('TextInputPopup', {
            title: this.env._t('Enter Code'),
            startingValue: '',
            placeholder: this.env._t('Gift card or Discount code'),
        });
        if (confirmed) {
            code = code.trim();
            if (code !== '') {
                this.env.pos.get_order().activateCode(code);
            }
        }
    }
}

OffersButton.template = 'OffersButton';

ProductScreen.addControlButton({
    component: OffersButton,
    condition: function () {
        return true
        // return this.env.pos.programs.some(p => ['coupons', 'promotion', 'gift_card', 'promo_code', 'next_order_coupons'].includes(p.program_type));
    }
});

Registries.Component.add(OffersButton);
