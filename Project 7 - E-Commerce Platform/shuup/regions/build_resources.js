   
const { getParcelBuildCommand, runBuildCommands } = require("shuup-static-build-tools");

runBuildCommands([
    getParcelBuildCommand({
        cacheDir: "regions",
        outputFileName: "shuup-regions",
        entryFile: "static_src/index.js"
    })
]);
