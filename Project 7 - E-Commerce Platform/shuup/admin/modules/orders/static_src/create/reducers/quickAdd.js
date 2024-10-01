   
import {handleActions} from "redux-actions";
import _ from "lodash";

export default handleActions({
    setAutoAdd: ((state, {payload}) => _.assign(state, {autoAdd: payload})),
    setQuickAddProduct: ((state, {payload}) => _.assign(state, {product: payload})),
    clearQuickAddProduct: ((state) => _.assign(state, {product: {id: "", text: ""}})),
    setFocusOnQuickAdd: ((state, {payload}) => _.assign(state, {focus: payload}))
}, {
    autoAdd: false,
    focus: false,
    product: {
        id: "",
        text: ""
    }
});
