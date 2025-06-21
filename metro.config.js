const { getDefaultConfig } = require('@expo/metro-config');
const path = require('path');

const projectRoot = path.resolve(__dirname, 'apps/mobile');
const config = getDefaultConfig(projectRoot);

config.watchFolders = [
  path.resolve(__dirname, 'node_modules'),
  projectRoot,
];

config.projectRoot = projectRoot;

module.exports = config;

