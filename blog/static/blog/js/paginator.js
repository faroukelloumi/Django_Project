var n_pages = {{ page_obj.paginator.num_pages }}
for (i = 1; i < n_pages ; i++) {
    var linkElt = document.createElement("li");
var pageElt = document.createElement("a");
pageElt.href = "/blog/list_article?page={{ page_obj.page }};
pageElt.textContent = 1;
linkElt.textContent = pageElt;
document.querySelector(".pagination").appendChild(linkElt);
}

{% if page_obj.has_previous %}
                    <li><a href="/blog/list_article?page={{ page_obj.previous_page_number }}">previous</a></li>
                {% endif %}
                <li class="active">
                    Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}.
                </li>
                {% if page_obj.has_next %}
                <li>   <a href="/blog/list_article?page={{ page_obj.next_page_number }}">next</a></li>
                {% endif %}