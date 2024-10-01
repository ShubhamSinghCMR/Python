   
import {handleActions} from "redux-actions";
import _ from "lodash";

export default handleActions({
    retrieveProductData: _.identity,  // Could've just omitted this, but Explicit Is Better, etc.
    receiveProductData: ((state, {payload}) => _.assign(state, {[payload.id]: payload.data}))
}, {});
