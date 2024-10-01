   
export default function() {
    const pickMatch = /pick=([^&]+)/.exec(window.location.search);
    return (pickMatch ? pickMatch[1] : null);
}
