   
const { getParcelBuildCommand, runBuildCommands } = require("shuup-static-build-tools");

const srcFiles = [
  { entry: "static_src/base/js/base.js"},
  { entry: "static_src/picotable/picotable.js"},
  { entry: "static_src/vendor/vendor.js"}
];

runBuildCommands(
  srcFiles.map(file => {
    return getParcelBuildCommand({
      cacheDir: "admin",
      entryFile: file.entry,
      outputFileName: (file.name !== 'undefined') ? file.name : null,
      outputDir: (file.entry.includes('.js')) ? "static/shuup_admin/js" : "static/shuup_admin/css"
    })
  })
);

