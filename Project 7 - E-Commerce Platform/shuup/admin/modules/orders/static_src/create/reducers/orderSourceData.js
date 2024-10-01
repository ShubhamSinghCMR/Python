   
import {handleActions} from "redux-actions";
import _ from "lodash";

export default handleActions({
    retrieveOrderSourceData: _.identity,
    receiveOrderSourceData: ((state, {payload}) => _.assign(state, {"order": payload.data}))
}, {});
