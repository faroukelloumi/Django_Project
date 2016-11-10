// Exécute un appel AJAX GET
// Prend en paramètres l'URL cible et la fonction callback appelée en cas de succès
function ajaxGet(url, func) {
    var req = new XMLHttpRequest();
    req.open("GET", url);
    req.addEventListener("load", function () {
        if (req.status >= 200 && req.status < 400) {
            // Appelle la fonction callback en lui passant la réponse de la requête
            func(req.responseText);
        } else {
            console.error(req.status + " " + req.statusText + " " + url);
        }
    });
    req.addEventListener("error", function () {
        console.error("Erreur réseau avec l'URL " + url);
    });
    req.send(null);
}

var articlesElt = document.getElementById("article");
ajaxGet("https://oc-jswebsrv.herokuapp.com/api/articles", function (reponse) {
    // Transforme la réponse en un tableau d'articles
    var articles = JSON.parse(reponse);
    console.log(articles);
    articles.forEach(function (article) {
        // Ajout du titre et du contenu de chaque article
        var rowElt = document.createElement("tr");
        var titreElt = document.createElement("td");
        titreElt.textContent = article.titre;
        var autElt = document.createElement("td");
        autElt.textContent = article.auteur;
        var catElt = document.createElement("td");
        catElt.textContent = article.categorie;
        var dateElt = document.createElement("td");
        dateElt.textContent = article.date;
        rowElt.appendChild(titreElt);
        rowElt.appendChild(autElt);
        rowElt.appendChild(catElt);
        rowElt.appendChild(dateElt);
        articlesElt.appendChild(rowElt);
    });
});