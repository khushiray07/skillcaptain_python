const HtmlWebpackPlugin = require('html-webpack-plugin');

const path =require('path');
module.exports={
    entry :"./app/index.js",
    module :{
        rules :[{
            test :/\.svg$/,
            loader:"svg-inline-loader",
        },
          {
        test: /\.css$/i,
        use: ["style-loader", "css-loader"],
      },
      {
        test:/\.(js)$/,
        use:"babel-loader",
      },
        
    ]
    },
    output :{
        path :path.resolve(__dirname,"dist"),
        filename : "bundle.js"
    },
      plugins: [new HtmlWebpackPlugin({
    template: './app/index.html' 
  }),],
mode: process.env.NODE_ENV === "production" ? "production" : "development",

    devServer: {
  static: {
    directory: path.resolve(__dirname, 'dist'),
  },
  port: 8080,
  open: true,
  hot: true,
},
};