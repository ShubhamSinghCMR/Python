   
export default function(ctrl, folder) {
    return function clickFolder(event) {
        ctrl.setFolder(folder.id);
        event.preventDefault();
        return false;
    };
}
