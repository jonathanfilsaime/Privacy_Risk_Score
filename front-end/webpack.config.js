/*
    ./webpack.config.js
*/
const path = require('path');
const webpack = require('webpack');

module.exports = {
  entry: './src/index.js',
  output: {
    path: path.resolve('dist'),
    filename: 'bundle.js',
    publicPath: '/'
  },
  module: {
    loaders: [
      { test: /\.js$/, loader: 'babel-loader', exclude: /node_modules/ },
      { test: /\.css$/, loader: 'style-loader'},
      { test: /\.css$/, loader: 'css-loader' },
      { test: /\.(png|jpg|gif)$/, loader: 'url-loader'}
    ]
  },
  devServer: {
    historyApiFallback: true,
  },
  devtool: '#eval-source-map'
}
