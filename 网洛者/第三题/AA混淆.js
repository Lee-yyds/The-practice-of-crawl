var window = {
    document: {location:{'href':'http://spider.wangluozhe.com/challenge/3'}}
}
var CryptoJS = require('crypto-js')
function anonymous() {
    try {
        (function() {
            'use strict';
            var tmp = "";
            Object.defineProperty(window, 'sign', {
                set: function(val) {
                    tmp = val;
                    return val;
                },
                get: function() {
                    return tmp;
                }
            });
        }
        )();
    } catch (e) {
        return 0;
    }
    delete window;
    delete window.sign;
    function encryptByDES(message, key) {
        var keyHex = CryptoJS.enc.Utf8.parse(key);
        var encrypted = CryptoJS.DES.encrypt(message, keyHex, {
            mode: CryptoJS.mode.ECB,
            padding: CryptoJS.pad.Pkcs7
        });
        return encrypted.ciphertext.toString();
    }
    try {
        var message = window.document.location.href;
        var tmp = window.DeviceMotionEvent;
        message = message + '|' + Date.parse(new Date()).toString();
        var key = Date.parse(new Date()).toString();
        return  encryptByDES(message, key);
    } catch (e) {
        var message = '1234567890abcdefghijklmnopqrstuvwxyz';
        var key = Date.parse(new Date()).toString() + '123';
        return encryptByDES(message, key);
    }
}


