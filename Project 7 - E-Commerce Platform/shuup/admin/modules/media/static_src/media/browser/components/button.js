   
import m from "mithril";
import _ from "lodash";

export default function(prop, value, label, title) {
    const active = (prop() == value);  // eslint-disable-line eqeqeq
    return m("button.btn.btn-default" + (active ? ".active" : ""), {
        type: "button",
        onclick: _.bind(prop, null, value),
        title: title
    }, label);
}
