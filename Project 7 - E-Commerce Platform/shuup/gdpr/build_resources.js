   
const { getParcelBuildCommand, runBuildCommands } = require("shuup-static-build-tools");

runBuildCommands([
    getParcelBuildCommand({
        cacheDir: "gdpr",
        outputFileName: "shuup-gdpr",
        entryFile: "static_src/index.js"
    })
]);
