   
import {handleActions} from "redux-actions";
import _ from "lodash";

export default handleActions({
    retrieveCustomerDetails: _.identity,
    receiveCustomerDetails: (state, {payload}) => {
        return _.assign(state, {
            customerInfo: payload.data.customer_info,
            orderSummary: payload.data.order_summary,
            recentOrders: payload.data.recent_orders
        });
    },
    showCustomerModal: ((state, {payload}) => _.assign(state, {showCustomerModal: payload}))
}, {});
