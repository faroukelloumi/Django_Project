var url = window.location.search;
var n = url.substring(url.lastIndexOf("=")+1);
console.log(n_pages, url, n);
if (n > 1) {
    linkElt = document.createElement("li");
    pageElt = document.createElement("a");
    pageElt.href = "/blog/list_article?page=" + 1;
    pageElt.textContent = "<<";
    linkElt.appendChild(pageElt);
    document.querySelector(".pagination").appendChild(linkElt);
    n--;
    var linkElt = document.createElement("li");
    var pageElt = document.createElement("a");
    pageElt.href = "/blog/list_article?page=" + n;
    n++;
    pageElt.textContent = "<";
    linkElt.appendChild(pageElt);
    document.querySelector(".pagination").appendChild(linkElt);
 }
for (i = 1; i <= n_pages ; i++) {
    var linkElt = document.createElement("li");
    var pageElt = document.createElement("a");
    pageElt.href = "/blog/list_article?page=" + i;
    pageElt.textContent = i;
    if (i == n) {
        linkElt.classList.add("active");
    };
    linkElt.appendChild(pageElt);
    document.querySelector(".pagination").appendChild(linkElt);
}
if (n < n_pages) {
    n++;
    linkElt = document.createElement("li");
    pageElt = document.createElement("a");
    pageElt.href = "/blog/list_article?page=" + n;
    pageElt.textContent = ">";
    linkElt.appendChild(pageElt);
    document.querySelector(".pagination").appendChild(linkElt);
    var linkElt = document.createElement("li");
    var pageElt = document.createElement("a");
    pageElt.href = "/blog/list_article?page=" + n_pages;
    pageElt.textContent = ">>";
    linkElt.appendChild(pageElt);
    document.querySelector(".pagination").appendChild(linkElt);
}
