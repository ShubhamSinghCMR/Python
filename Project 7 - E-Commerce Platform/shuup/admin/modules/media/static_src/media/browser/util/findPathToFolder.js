   
/* eslint-disable no-shadow,eqeqeq */
import _ from "lodash";

export default function(rootFolder, folderId) {
    var pathToFolder = null;

    function walk(folder, folderPath) {
        if (folder.id == folderId) {
            pathToFolder = folderPath.concat([folder]);
            return;
        }
        folderPath = [].concat(folderPath).concat([folder]);
        _.each(folder.children, function(folder) {
            if (!pathToFolder) {
                walk(folder, folderPath);
            }
        });
    }

    walk(rootFolder, []);
    return pathToFolder || [];
}
