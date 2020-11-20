function addValue() {
    var s = document.getElementById("InputFormula").value;
    s = s.replace("+", "%2B");
    s = s.split('**').join('^');
    s = s.replace("*", " ");
    document.getElementById('wrapper').src = "https://chart.apis.google.com/chart?cht=tx&chl=" + s;
}
