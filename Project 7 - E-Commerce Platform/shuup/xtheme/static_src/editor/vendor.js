   

//-- jQuery
var jquery = require("jquery");
window.$ = window.jQuery = jquery;
const select2 = require("select2");
select2($);

const _ = require('lodash');
window._ = _;

const Sortable = require('sortablejs');
window.Sortable = Sortable.default || Sortable;

require('bootstrap');
require("summernote/dist/summernote.js");
require("../../../admin/static_src/base/js/browse-widget.js");
