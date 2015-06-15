var webpack = require('webpack');
var path = require("path");

module.exports = {
  entry: {
    app: [
      './scripts/app.js',
      './scripts/rooms/room.js',
      './scripts/rooms/room_list.js',
    ],
  },
  output: {
    path: path.join(__dirname, 'static'),
    filename: '[name].js',
  },
  resolve: {
    root: [path.join(__dirname, "bower_components")],
    alias: {
      'bootstrap.js': 'bootstrap/dist/js/bootstrap.js',
      'bootstrap.css': 'bootstrap/dist/css/bootstrap.css',
    },
  },
  plugins: [
    new webpack.ResolverPlugin(
      new webpack.ResolverPlugin.DirectoryDescriptionFilePlugin("bower.json", ["main"])
    ),
  ],
  module: {
    loaders: [
      { test: /\.css$/,   loader: "style-loader!css-loader" },
      { test: /\.less$/,  loader: "style-loader!css-loader!less-loader" },
      { test: /\.woff$/,  loader: "file-loader?prefix=font/" },
      { test: /\.woff2$/, loader: "file-loader?prefix=font/" },
      { test: /\.eot$/,   loader: "file-loader?prefix=font/" },
      { test: /\.ttf$/,   loader: "file-loader?prefix=font/" },
      { test: /\.svg$/,   loader: "file-loader?prefix=font/" },
    ],
  },
}
