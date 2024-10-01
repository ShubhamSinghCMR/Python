   
const { getParcelBuildCommand, runBuildCommands } = require("shuup-static-build-tools");

runBuildCommands([
    getParcelBuildCommand({
        cacheDir: "xtheme",
        outputDir: "static/xtheme/",
        entryFile: "static_src/editor/editor.less"
    }),
    getParcelBuildCommand({
        cacheDir: "xtheme",
        outputDir: "static/xtheme/",
        entryFile: "static_src/editor/editor.js"
    }),
    getParcelBuildCommand({
        cacheDir: "xtheme",
        outputDir: "static/xtheme/",
        entryFile: "static_src/editor/vendor.js"
    })
]);
