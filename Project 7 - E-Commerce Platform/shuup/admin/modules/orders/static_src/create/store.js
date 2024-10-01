   
import {compose, createStore, applyMiddleware} from "redux";
import {autoRehydrate} from "redux-persist";
import reducer from "./reducers";

const thunk = function ({ dispatch, getState }) {
    // h/t redux-thunk :)
    return next => action =>
        typeof action === "function" ?
            action(dispatch, getState) :
            next(action);
};

const createLoggedStore = compose(autoRehydrate(), applyMiddleware(thunk))(createStore);
const store = createLoggedStore(reducer);

export default store;
