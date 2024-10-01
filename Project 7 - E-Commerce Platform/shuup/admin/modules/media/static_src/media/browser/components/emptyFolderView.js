   
import m from "mithril";
import responsiveUploadHint from "./responsiveUploadHint";
import { uploadIndicator } from "./images";

export default function(ctrl, folder) {  // eslint-disable-line no-unused-vars
    return m("div.empty-folder", [
        m("div.empty-image",
            m("img", {src: uploadIndicator})
        ),
        m("div.empty-text", responsiveUploadHint)
    ]);
}
