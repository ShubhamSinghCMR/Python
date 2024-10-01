   
function isNumeric(n) {
  return !isNaN(parseFloat(n)) && isFinite(n);
}

function ensureNumericValue(value, defaultValue = 0, asInteger = false) {
    if (!isNumeric(value)) {
        return defaultValue || 0;
    }
    if (Number.isInteger(value) || asInteger) {
        return parseInt(value, 10);
    }
    return parseFloat(value);
}

export default ensureNumericValue;
