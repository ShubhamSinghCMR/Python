   
/* eslint-disable no-unused-vars */

import './dashboard-charts.js';

const Masonry = require('masonry-layout');
window.Masonry = Masonry;

$(function() {
    "use strict";
    if (window.DashboardCharts) {
        window.DashboardCharts.init();
    }

    const target = document.getElementById("dashboard-wrapper");
    if (target && window.Masonry) {
        const msnry = new window.Masonry(target, {
            itemSelector: ".block",
            columnWidth: ".block",
            percentPosition: true
        });

        document.getElementById("menu-button").addEventListener("click", () => {
            setTimeout(() => {msnry.layout()}, 500)
        });
    }

    $(document).on("click", "button.dismiss-button", function() {
        const $button = $(this);
        const url = $button.data("dismissUrl");
        if (!url) {
            return;
        }
        $.ajax({
            type: "POST",
            url: url,
            dataType: "json",
            success: function(data) {
                if (data.ok) {
                    const dismissTarget = $button.data("dismissTarget");
                    if (dismissTarget) {
                        $(dismissTarget).remove();
                    }
                }
                if (data.error && window.Messages) {
                    window.Messages.enqueue({text: data.error});
                }
            }
        });
    });
});
