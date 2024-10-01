   
import m from "mithril";
import _ from "lodash";
import folderClick from "./folderClick";

export default function(ctrl) {
    const items = [];
    const folderPath = ctrl.currentFolderPath();
    _.each(folderPath, function(folder, index) {
        items.push(
            m("a.breadcrumb-link" + (index === folderPath.length - 1 ? ".current" : ""), {
                href: "#",
                key: folder.id,
                onclick: folderClick(ctrl, folder)
            }, folder.name)
        );
        items.push(m("i.fa.fa-angle-right"));
    });
    items.pop(); // pop last chevron
    items.unshift(m("i.fa.fa-folder-open.folder-icon"));
    return items;
}
