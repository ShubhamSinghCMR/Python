   
import m from "mithril";
import _ from "lodash";

function getUrl(params) {
    return location.pathname + "?" + m.route.buildQueryString(params);
}

export function get(command, params) {
    const url = getUrl(_.assign({command}, params));
    return m.request({method: "GET", url});
}

export function post(command, data) {
    const url = getUrl({command});
    return m.request({
        method: "POST", url, data,
        config: function (xhr) {
            xhr.setRequestHeader("X-CSRFToken", window.ShuupAdminConfig.csrf);
        }
    });
}
