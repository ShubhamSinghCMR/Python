   
const { getParcelBuildCommand, runBuildCommands } = require("shuup-static-build-tools");

runBuildCommands([
    getParcelBuildCommand({
        cacheDir: "xtheme",
        outputDir: "static/xtheme/",
        entryFile: "static_src/injection/editor-injection.js"
    })
]);
