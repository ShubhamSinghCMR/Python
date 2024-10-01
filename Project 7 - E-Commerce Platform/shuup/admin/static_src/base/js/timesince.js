   
$(function() {
    "use strict";
    function update() {
        $(".timesince").each(function() {
            const $el = $(this);
            const ts = $el.data("ts");
            if (!ts) {
                return;
            }
            const time = moment(ts);
            if (!time.isValid()) {
                return;
            }
            $el.text(time.fromNow());
        });
    }
    update();
    setInterval(update, 60000);
});
