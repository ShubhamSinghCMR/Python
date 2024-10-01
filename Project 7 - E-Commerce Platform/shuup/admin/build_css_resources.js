   
const { getParcelBuildCommand, runBuildCommands } = require("shuup-static-build-tools");

const srcFiles = [
  { entry: "static_src/base/scss/style.scss", name: "base"},
  { entry: "static_src/dashboard/scss/dashboard.scss"},
  { entry: "static_src/wizard/scss/wizard.scss"},
  { entry: "modules/media/static_src/media/browser/media-browser.scss"},
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

