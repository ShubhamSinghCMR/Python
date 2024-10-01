   
import menuItem from "./menuItem";
import * as fileActions from "../actions/fileActions";

export default function(controller, file) {
    return function() {
        return [
            menuItem(gettext("Rename file"), () => {
                fileActions.promptRenameFile(controller, file);
            }, {disabled: controller.isFileMenuDisabled("rename-file", file)}),
            menuItem(gettext("Delete file"), () => {
                fileActions.promptDeleteFile(controller, file);
            }, {disabled: controller.isFileMenuDisabled("delete-file", file)})
        ];
    };
}
