var webpack = require('webpack');
var path = require("path");

module.exports = {
  entry: './app/main.js',
  output: {
    path: path.join(__dirname, 'static'),
    filename: 'app.js',
  },
  resolve: {
    root: [
      path.join(__dirname, "bower_components"),
      path.join(__dirname, 'app'),
    ],
    alias: {
      'bootstrap.js': 'bootstrap/dist/js/bootstrap.js',
      'bootstrap.css': 'bootstrap/dist/css/bootstrap.css',
      'jquery-cookie': 'jquery-cookie/jquery.cookie.js',
    },
  },
  plugins: [
    new webpack.ResolverPlugin(
      new webpack.ResolverPlugin.DirectoryDescriptionFilePlugin("bower.json", ["main"])
    ),
    new webpack.ProvidePlugin({
      jQuery: "jquery",
      $: "jquery",
    })
  ],
  module: {
    loaders: [
      { test: /\.css$/,   loader: "style-loader!css-loader" },
      { test: /\.less$/,  loader: "style-loader!css-loader!less-loader" },
      { test: /\.vue$/,   loader: "vue-loader" },
      { test: /\.woff$/,  loader: "file-loader?prefix=font/" },
      { test: /\.woff2$/, loader: "file-loader?prefix=font/" },
      { test: /\.eot$/,   loader: "file-loader?prefix=font/" },
      { test: /\.ttf$/,   loader: "file-loader?prefix=font/" },
      { test: /\.svg$/,   loader: "file-loader?prefix=font/" },
    ],
  },
}
