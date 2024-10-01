   
const { getParcelBuildCommand, runBuildCommands } = require("shuup-static-build-tools");

runBuildCommands([
    getParcelBuildCommand({
        cacheDir: "notify",
        outputDir: "static/notify/admin/",
        outputFileName: "script-editor",
        entryFile: "static_src/index.js"
    })
]);
