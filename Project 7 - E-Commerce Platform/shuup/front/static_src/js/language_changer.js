   
window.changeLanguage = function changeLanguage() {
    const form = document.createElement("form");
    form.method = "POST";
    form.action = "/set-language/";
    const input = document.createElement("input");
    input.type = "hidden";
    input.name = "language";
    input.id = "language-field";
    input.value = $(this).data("value");
    form.appendChild(input);
    document.body.appendChild(form);
    form.submit();
};

$(function() {
    $(".languages li a").click(window.changeLanguage);
});
