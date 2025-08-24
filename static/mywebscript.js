let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value;
    let encodedText = encodeURIComponent(textToAnalyze);

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            if (this.status == 200) {
                document.getElementById("system_response").innerHTML = xhttp.responseText;
            } else {
                document.getElementById("system_response").innerHTML = "<p><b>Error: " + this.status + "</b></p>";
            }
        }
    };
    xhttp.open("GET", "emotionDetector?textToAnalyze=" + encodedText, true);
    xhttp.send();
}