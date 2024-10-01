   
function isTouchDevice() {
  return ("ontouchstart" in window || navigator.maxTouchPoints);
}

$(function() {
    "use strict";
    $("[data-toggle='popover']").each(function(idx, elem) {
        if($(elem).data("trigger") !== "manual") {
            $(elem).popover();
        } else if (!isTouchDevice()) {
            $(elem).on("mouseenter", function() {
                $(elem).popover("show");
            });
            $(elem).on("mouseleave", function() {
                $(elem).popover("hide");
            });
        } else {
            // unbind all hover related from manual popovers on touch device
            $(elem).unbind("hover mouseenter mouseleave");
        }
    });
}());
