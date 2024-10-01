   
import {handleActions} from "redux-actions";
import _ from "lodash";

export default handleActions({
    setComment: ((state, {payload}) => _.trim(payload || ""))
}, null);
