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
  },
  module: {
    loaders: [
      { test: /\.css$/,  loader: "style-loader!css-loader" },
      { test: /\.less$/,  loader: "style-loader!css-loader!less-loader" },
    ],
  },
  plugins: [
    new webpack.ResolverPlugin(
      new webpack.ResolverPlugin.DirectoryDescriptionFilePlugin("bower.json", ["main"])
    ),
  ],
}
