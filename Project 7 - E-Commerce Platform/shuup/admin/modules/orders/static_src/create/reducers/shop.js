   
import { handleActions } from "redux-actions";

export default handleActions({
    setShopChoices: ((state, { payload }) => Object.assign({}, state, { choices: payload })),
    setCountries: ((state, { payload }) => Object.assign({}, state, { countries: payload })),
    setShop: ((state, { payload }) => Object.assign({}, state, { selected: payload }))
}, {
    choices: [],
    countries: [],
    selected: null
});
