   
const { getParcelBuildCommand, runBuildCommands } = require("shuup-static-build-tools");

runBuildCommands([
    getParcelBuildCommand({
        cacheDir: "classic_gray",
        outputDir: "static/shuup/classic_gray/pink",
        entryFile: "static_src/pink/style.css"
    }),
    getParcelBuildCommand({
        cacheDir: "classic_gray",
        outputDir: "static/shuup/classic_gray/blue",
        entryFile: "static_src/blue/style.css"
    })
]);
