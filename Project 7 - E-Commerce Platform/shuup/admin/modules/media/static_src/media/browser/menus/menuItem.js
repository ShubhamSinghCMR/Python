   
import _ from "lodash";
import m from "mithril";
import * as menuManager from "../util/menuManager";

export default function item(label, action, attrs = {}) {
    const tagBits = ["li"];
    if (attrs.disabled) {
        action = _.noop;
        tagBits.push("disabled");
        return;
    }
    return m(tagBits.join("."), m("a.dropdown-item", {
        href: "#", onclick: (event) => {
            event.preventDefault();
            action();
            menuManager.close();
        }
    }, label));
}
