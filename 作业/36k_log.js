

function lz() {
        var r = n(17)
      , o = n(4)
      , i = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCeiLxP4ZavN8qhI+x+whAiFpGWpY9y1AHSQC86qEMBVnmqC8vdZAfxxuQWeQaeMWG07lXhXegTjZ5wn9pHnjg15wbjRGSTfwuZxSFW6sS3GYlrg40ckqAagzIjkE+5OLPsdjVYQyhLfKxj/79oOfjl/lV3rQnk/SSczHW0PEyUbQIDAQAB"

    var e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "";
    if (!Object(o.isNodeEnv)()) {
        var t = n(755)
          , r = new t.JSEncrypt;
        r.setPublicKey(i);
        var a = r.encrypt(e);
        return a
}
}

console.log(lz(123456))