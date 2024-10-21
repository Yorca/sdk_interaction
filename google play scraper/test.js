import gplay from "google-play-scraper";

gplay.app({appId: 'com.nianticlabs.pokemongo'})
    .then(console.log, console.log);