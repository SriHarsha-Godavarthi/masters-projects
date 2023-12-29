const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
module.exports = {
mode: 'development',
entry: './src/index.js',
devtool: 'inline-source-map',
output: {
path: path.join(__dirname, '../../../dist'),
filename: 'bundle.js'
},
devtool: 'inline-source-map',
devServer: {
static: '../../../dist',
},
module: {
rules: [
{
test: /\.jsx?$/,
exclude: /node_modules/,
loader: 'babel-loader'
},
{
    test: /\.css$/i,
    exclude: /node_modules/,
    use: ["style-loader", "css-loader"],
  },{
    test: /\.(png|jpe?g|gif)$/i,
    use: [
      {
        loader: 'url-loader',
      },
    ],
  },
]
},
resolve: {
extensions: ['.jsx', '.ts', '.js','.css'],
},
plugins:[
new HtmlWebpackPlugin({
template: './public/index.html'
})
]
}