document.getElementById("videoForm").addEventListener("submit", async function(event) {
    event.preventDefault(); // evita o submit padrão

    const url = document.getElementById("videourl").value;
    const encodedUrl = encodeURIComponent(url);

    // redireciona para /find?url=ENCODED_URL
    const result = await fetch('/find?url=' + encodedUrl);

    alert(await result.text());
});