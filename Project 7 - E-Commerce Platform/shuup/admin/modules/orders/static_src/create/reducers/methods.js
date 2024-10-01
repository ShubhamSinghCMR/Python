   
import {handleActions} from "redux-actions";
import _ from "lodash";

export default handleActions({
    setShippingMethod: ((state, {payload}) => _.assign(state, {shippingMethod: payload})),
    setShippingMethodChoices: ((state, {payload}) => _.assign(state, {shippingMethodChoices: payload})),
    setPaymentMethod: ((state, {payload}) => _.assign(state, {paymentMethod: payload})),
    setPaymentMethodChoices: ((state, {payload}) => _.assign(state, {paymentMethodChoices: payload}))
}, {
    shippingMethodChoices: [],
    shippingMethod: null,
    paymentMethodChoices: [],
    paymentMethod: null
});
