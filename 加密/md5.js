// 引用 crypto-js 加密模块
var CryptoJS = require('crypto-js')

function MD5Test() {
    var text = "I love python!"
    return CryptoJS.MD5(text)
}

console.log(MD5Test().toString())  // 21169ee3acd4a24e1fcb4322cfd9a2b8

console.log('e10adc3949ba59abbe56e057f20f883e'.length);