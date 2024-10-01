   
import {handleActions} from "redux-actions";
import _ from "lodash";

export default handleActions({
    retrieveCustomerData: _.identity,
    receiveCustomerData: ((state, {payload}) => _.assign(state, {[payload.id]: payload.data}))
}, {});
