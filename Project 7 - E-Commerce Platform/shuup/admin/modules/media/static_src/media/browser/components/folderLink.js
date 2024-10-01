   
import m from "mithril";

export default function(ctrl, folder) {
    return m("a", {
        href: "#", onclick: function() {
            ctrl.setFolder(folder.id);
            return false;
        }
    }, folder.name);
}
