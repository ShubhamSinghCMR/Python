   
const { getParcelBuildCommand, runBuildCommands } = require("shuup-static-build-tools");

runBuildCommands([
    getParcelBuildCommand({
        cacheDir: "front",
        outputDir: "static/shuup/front/js",
        entryFile: "static_src/js/vendor.js"
    }),
    getParcelBuildCommand({
        cacheDir: "front",
        outputDir: "static/shuup/front/js",
        outputFileName: "scripts",
        entryFile: "static_src/js/index.js"
    }),
    getParcelBuildCommand({
        cacheDir: "front",
        outputDir: "static/shuup/front/css",
        entryFile: "static_src/less/style.css"
    })
]);
