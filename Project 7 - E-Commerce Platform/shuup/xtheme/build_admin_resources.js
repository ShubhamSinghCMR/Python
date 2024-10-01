   
const { getParcelBuildCommand, runBuildCommands } = require("shuup-static-build-tools");

runBuildCommands([
    getParcelBuildCommand({
        cacheDir: "xtheme",
        outputDir: "static/xtheme/admin/",
        entryFile: "static_src/admin/xtheme_admin.less"
    }),
    getParcelBuildCommand({
        cacheDir: "xtheme",
        outputDir: "static/xtheme/admin",
        entryFile: "static_src/admin/script.js"
    }),
    getParcelBuildCommand({
        cacheDir: "xtheme",
        outputDir: "static/xtheme/admin/",
        entryFile: "static_src/admin/snippet.js"
    }),
]);
