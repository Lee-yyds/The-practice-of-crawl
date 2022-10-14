var CryptoJS = require('crypto-js')
var csrfToken = "s7NTaEldZH56S6zMKAmjxRmmeCWKdayac12bRwnh";

function aes(val) {
    var k = CryptoJS.enc.Utf8.parse('1234567890abcDEF');
    var iv = CryptoJS.enc.Utf8.parse('1234567890abcDEF');
    enc = CryptoJS.AES.encrypt(val, k, {iv: iv, mode:CryptoJS.mode.CBC, padding: CryptoJS.pad.ZeroPadding}).toString();
    return enc;
}


console.log(aes('123456'));


