var window = global;

function encryptApiKey(){
        API_KEY = "a2c903cc-b31e-4547-9299-b6d07b7631ab"
        var t = API_KEY
          , e = t.split("")
          , r = e.splice(0, 8);
        return e.concat(r).join("")
    }

function encryptTime(t){
        var e = (1 * t + 1111111111111).toString().split("")
          , r = parseInt(10 * Math.random(), 10)
          , n = parseInt(10 * Math.random(), 10)
          , o = parseInt(10 * Math.random(), 10);
        return e.concat([r, n, o]).join("")
    }

function comb(t, e){
        var r = "".concat(t, "|").concat(e);
        return window.btoa(r)
    }

function get_key(){
        var t = (new Date).getTime()
          , e = encryptApiKey();
        return t = encryptTime(t),
        comb(e, t)
    }

console.log(get_key())

