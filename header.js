document.addEventListener("DOMContentLoaded", function() {
    const isSubdir = window.location.pathname.includes('/events/');
    const isHome = !isSubdir && (
        window.location.pathname.endsWith('index.html') || 
        window.location.pathname.endsWith('/') || 
        window.location.pathname.split('/').pop() === ''
    );

    const logoUrl = isHome ? '#top' : (isSubdir ? '../index.html#top' : 'index.html#top');
    const newsUrl = isHome ? '#news' : (isSubdir ? '../index.html#news' : 'index.html#news');
    const karteUrl = isHome ? 'karte.html' : (isSubdir ? '../karte.html' : 'karte.html');
    const landwirteUrl = isHome ? '#landwirte' : (isSubdir ? '../index.html#landwirte' : 'index.html#landwirte');
    const anwohnerUrl = isHome ? '#anwohner' : (isSubdir ? '../index.html#anwohner' : 'index.html#anwohner');
    const passantenUrl = isHome ? '#passanten' : (isSubdir ? '../index.html#passanten' : 'index.html#passanten');
    const supportUrl = isHome ? '#support' : (isSubdir ? '../index.html#support' : 'index.html#support');

    const headerHTML = `
        <nav>
            <div class="logo"><a href="${logoUrl}">Landunter am Hammer&nbsp;Bach</a></div>
            <ul>
                <li><a href="${newsUrl}">News</a></li>
                <li><a href="${karteUrl}">Karte</a></li>
                <li><a href="${landwirteUrl}">Landwirte</a></li>
                <li><a href="${anwohnerUrl}">Anwohner</a></li>
                <li><a href="${passantenUrl}">Passanten</a></li>
                <li><a href="${supportUrl}" style="white-space: nowrap;">Termine&nbsp;&amp;&nbsp;Newsletter</a></li>
            </ul>
        </nav>
    `;

    const headerElement = document.querySelector('header');
    if (headerElement) {
        headerElement.innerHTML = headerHTML;
    }
});
