import gplay from "google-play-scraper";

gplay.app({appId: 'com.facebook.katana'})
    .then(console.log, console.log);