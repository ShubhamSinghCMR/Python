   

var inputChangeTimeout;
function activateColorPicker(el) {
    $(el).colorpicker({
        format: "hex",
        horizontal: true,
        autoInputFallback: false,
    }).unbind("keyup").on("keyup", function(event) {
        window.clearTimeout(inputChangeTimeout);
        inputChangeTimeout = window.setTimeout(function () {
            $(event.target).trigger("change");
        }, 1000);
    });
}
window.activateColorPicker = activateColorPicker;

$(function() {
    $(".hex-color-picker").each((index, el) => {
        activateColorPicker(el);
    });
});
