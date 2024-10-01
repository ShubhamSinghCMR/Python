   
import {combineReducers} from "redux";
import lines from "./lines";
import productData from "./productData";
import shop from "./shop";
import customer from "./customer";
import customerData from "./customerData";
import customerDetails from "./customerDetails";
import methods from "./methods";
import order from "./order";
import comment from "./comment";
import quickAdd from "./quickAdd";

const childReducer = combineReducers({
    lines,
    productData,
    shop,
    customer,
    customerData,
    customerDetails,
    methods,
    order,
    comment,
    quickAdd
});

export default function(state, action) {
    if(action.type === "_replaceState") { // For debugging purposes.
        return action.payload;
    }
    state = childReducer(state, action);
    return state;
}
