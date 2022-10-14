function M() {
    var n = c[33]
      , t = parseInt(a[103], e[44])
      , o = a[104]
      , i = r[80];
    S = new rt([i, i, i, i, n, n, n, o, t, t, t, t, t, t, t, i, t, n]),
    S[f] = ot.serverTimeNow(),
    L(),
    S[k] = zn,
    S[O] = Kn,
    S[T] = e[22],
    S[d] = ot.strhash(navigator.userAgent),
    S[b] = ut.getBrowserFeature(),
    S[p] = ut.getPlatform(),
    S[g] = ut.getBrowserIndex(),
    S[m] = ut.getPluginNum()
}
function N() {
    S[T]++,
    S[f] = ot.serverTimeNow(),
    S[l] = ot.timeNow(),
    S[k] = zn,
    S[I] = it.getMouseMove(),
    S[_] = it.getMouseClick(),
    S[y] = it.getMouseWhell(),
    S[E] = it.getKeyDown(),
    S[A] = it.getClickPos().x,
    S[C] = it.getClickPos().y;
    var n = S.toBuffer();
    return et.encode(n)
}

function x() {
    var t = N();
     return t
}

console.log(N());