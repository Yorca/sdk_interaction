import gplay from "google-play-scraper";
import fs from "fs"
import Parser from "json2csv"

const csvFilePath = 'app_metadata_topfree-100.csv';
if (!fs.existsSync(csvFilePath)) {
    fs.writeFileSync(csvFilePath, 'appId,title,type\n');
    //fs.writeFileSync(csvFilePath, 'appId,type,title,installs,minInstalls,maxInstalls,androidVersion,androidMaxVersion,developerEmail,privacyPolicy,available,genreId,categories,contentRating,adSupported,updated,url\n');
}

async function downloadAppData() {
    const promises = [];

    Object.keys(gplay.category).forEach(categoryKey => {
        const categoryValue = gplay.category[categoryKey];
        // if (categoryValue.startsWith("GAME_")) {
        //     return;
        // }
        // if (["FINANCE", "WEATHER", "PARENTING", "PHOTOGRAPHY", "GAME", "BOOKS_AND_REFERENCE", "HEALTH_AND_FITNESS"].includes(categoryValue)) {
        //     return;
        // }
        console.log(`Category Key: ${categoryKey}, Category Value: ${categoryValue}`);

        const promise = gplay.list({
            category: categoryValue,
            collection: gplay.collection.TOP_FREE,
            num: 100,
            lang: "en",
            fullDetail: false
        }).then(result => {
            result.forEach(app => {
                const {appId, title}  = app
                //const {appId, title, installs, minInstalls, maxInstalls, androidVersion, androidMaxVersion, developerEmail, privacyPolicy, available, genreId, categories, contentRating, adSupported, updated, url}  = app
                //const csvRow = `"${appId}","${categoryValue}","${title}","${installs}","${minInstalls}","${maxInstalls}","${androidVersion}","${androidMaxVersion}","${developerEmail}","${privacyPolicy}","${available}","${genreId}","${categories}","${contentRating}","${adSupported}","${updated}","${url}"\n"`;
                const csvRow = `"${appId}","${title}","${categoryValue}"\n"`;
                fs.appendFileSync(csvFilePath, csvRow);
            });
            console.log(`Apps in category ${categoryValue}:`, result);
        }).catch(console.error);

        promises.push(promise);
    });
    await Promise.all(promises);
}


downloadAppData().catch(console.error);
