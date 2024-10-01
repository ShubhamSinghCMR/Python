   
$(function () {
    $(".selectpicker").selectpicker();
});

$(document).ready(function () {
    $(".btn-variation").on("click", function (e) {
        e.preventDefault();
        var level = $(this).data("level");
        $(".btn-variation").each(function (i, elem) {
            if ($(elem).data("level") === level) {
                $(elem).removeClass("btn-active");
            }
        });
        $(this).addClass("btn-active");
        var productId = $(this).data("target-product");
        var variationId = $(this).data("product-id");
        var parentProduct = $(this).data("primary-product");
        if ($("#var_" + productId).length) {
            $("#var_" + productId).val(variationId);
        } else {
            $("#product-variations-" + productId).val(variationId);
        }
        var id = (parentProduct) ? parentProduct : productId;
        window.updatePrice(id);
    });
});
