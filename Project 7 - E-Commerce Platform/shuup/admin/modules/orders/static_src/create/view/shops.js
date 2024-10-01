   
import { setShop, updateLines } from "../actions";
import { selectBox } from "./utils";

export function shopSelectView(store) {
    const { shop } = store.getState();
    return m("div.form-group", [
        m("label.control-label", gettext("Shop")),
        selectBox(shop.selected.id, function () {
            const newShop = _.find(shop.choices, { "id": parseInt(this.value) });
            store.dispatch(setShop(newShop));
            store.dispatch(updateLines());
        }, shop.choices)
    ]);
}
