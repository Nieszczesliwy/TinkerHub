

document.addEventListener("DOMContentLoaded", function() {
    content_section = document.getElementById("content");
    url = BASEURL + "/all?page=1";

    fetch(url, {
        method: "GET",
        headers:{
                'Content-Type':'application/json',
        },
    })
    .then(response => {
        return response.json();
    })
    .then(response => {
        articles_page_info = response.data;
        console.log(articles_page_info);
    });

});