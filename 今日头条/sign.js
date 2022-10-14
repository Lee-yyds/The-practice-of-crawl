

function I(e, t) {
    var n, a, r = "".concat('https:', "//").concat('www.toutiao.com');
    (function(e) {
        return !A.some((function(t) {
            return e.indexOf(t) > -1
        }
        ))
    }
    )(e) && (r += "/toutiao");
    var o = {
        url: r + e
    };
    return t.data && (o.body = t.data),
    (null === (n = window.byted_acrawler) || void 0 === n || null === (a = n.sign) || void 0 === a ? void 0 : a.call(n, o)) || ""
}

console.log(I('https://lf3-config.bytetcc.com/obj/tcc-config-web/tcc-v2-data-toutiao.fe.toutiao_web_pc-common',0));