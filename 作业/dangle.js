var RSAAPP = {};
RSAAPP.NoPadding = "NoPadding";
RSAAPP.PKCS1Padding = "PKCS1Padding";
RSAAPP.RawEncoding = "RawEncoding";
RSAAPP.NumericEncoding = "NumericEncoding"
function charToHex(c)
{
	var ZERO = 48;
	var NINE = ZERO + 9;
	var littleA = 97;
	var littleZ = littleA + 25;
	var bigA = 65;
	var bigZ = 65 + 25;
	var result;

	if (c >= ZERO && c <= NINE) {
		result = c - ZERO;
	} else if (c >= bigA && c <= bigZ) {
		result = 10 + c - bigA;
	} else if (c >= littleA && c <= littleZ) {
		result = 10 + c - littleA;
	} else {
		result = 0;
	}
	return result;
}
function hexToDigit(s)
{
	var result = 0;
	var sl = Math.min(s.length, 4);
	for (var i = 0; i < sl; ++i) {
		result <<= 4;
		result |= charToHex(s.charCodeAt(i))
	}
	return result;
}
function biFromHex(s)
{
	var result = new BigInt();
	var sl = s.length;
	for (var i = sl, j = 0; i > 0; i -= 4, ++j) {
		result.digits[j] = hexToDigit(s.substr(Math.max(i - 4, 0), Math.min(i, 4)));
	}
	return result;
}
function BarrettMu(m)
{
	this.modulus = biCopy(m);
	this.k = biHighIndex(this.modulus) + 1;
	var b2k = new BigInt();
	b2k.digits[2 * this.k] = 1; // b2k = b^(2k)
	this.mu = biDivide(b2k, this.modulus);
	this.bkplus1 = new BigInt();
	this.bkplus1.digits[this.k + 1] = 1; // bkplus1 = b^(k+1)
	this.modulo = BarrettMu_modulo;
	this.multiplyMod = BarrettMu_multiplyMod;
	this.powMod = BarrettMu_powMod;
}
function biHighIndex(x)
{
	var result = x.digits.length - 1;
	while (result > 0 && x.digits[result] == 0) --result;
	return result;
}
function RSAKeyPair(encryptionExponent, decryptionExponent, modulus, keylen)
{

    this.e = biFromHex(encryptionExponent);
    this.d = biFromHex(decryptionExponent);
    this.m = biFromHex(modulus);

    if (typeof (keylen) != 'number') {
        this.chunkSize = 2 * biHighIndex(this.m);
    } else {
        this.chunkSize = keylen / 8;
    }

    this.radix = 16;

    this.barrett = new BarrettMu(this.m);
}


function encryptedString(key, s, pad, encoding)

{
    var a = new Array();
    // The usual Alice and Bob stuff
    var sl = s.length;
    // Plaintext string length
    var i, j, k;
    // The usual Fortran index stuff
    var padtype;
    // Type of padding to do
    var encodingtype;
    // Type of output encoding
    var rpad;
    // Random pad
    var al;
    // Array length
    var result = "";
    // Cypthertext result
    var block;
    // Big integer block to encrypt
    var crypt;
    // Big integer result
    var text;
    // Text result

    if (typeof (pad) == 'string') {
        if (pad == RSAAPP.NoPadding) {
            padtype = 1;
        } else if (pad == RSAAPP.PKCS1Padding) {
            padtype = 2;
        } else {
            padtype = 0;
        }
    } else {
        padtype = 0;
    }

    if (typeof (encoding) == 'string' && encoding == RSAAPP.RawEncoding) {
        encodingtype = 1;
    } else {
        encodingtype = 0;
    }

    if (padtype == 1) {
        if (sl > key.chunkSize) {
            sl = key.chunkSize;
        }
    } else if (padtype == 2) {
        if (sl > (key.chunkSize - 11)) {
            sl = key.chunkSize - 11;
        }
    }

    i = 0;

    if (padtype == 2) {
        j = sl - 1;
    } else {
        j = key.chunkSize - 1;
    }

    while (i < sl) {
        if (padtype) {
            a[j] = s.charCodeAt(i);
        } else {
            a[i] = s.charCodeAt(i);
        }

        i++;
        j--;
    }

    if (padtype == 1) {
        i = 0;
    }

    j = key.chunkSize - (sl % key.chunkSize);

    while (j > 0) {
        if (padtype == 2) {
            rpad = Math.floor(Math.random() * 256);

            while (!rpad) {
                rpad = Math.floor(Math.random() * 256);
            }

            a[i] = rpad;
        } else {
            a[i] = 0;
        }

        i++;
        j--;
    }

    if (padtype == 2) {
        a[sl] = 0;
        a[key.chunkSize - 2] = 2;
        a[key.chunkSize - 1] = 0;
    }

    al = a.length;

    for (i = 0; i < al; i += key.chunkSize) {

        block = new BigInt();

        j = 0;

        for (k = i; k < (i + key.chunkSize); ++j) {
            block.digits[j] = a[k++];
            block.digits[j] += a[k++] << 8;
        }

        crypt = key.barrett.powMod(block, key.e);
        if (encodingtype == 1) {
            text = biToBytes(crypt);
        } else {
            text = (key.radix == 16) ? biToHex(crypt) : biToString(crypt, key.radix);
        }
        result += text;
    }

    return result;
}

function decryptedString(key, c)

{
    var blocks = c.split(" ");
    // Multiple blocks of cyphertext
    var b;
    // The usual Alice and Bob stuff
    var i, j;
    // The usual Fortran index stuff
    var bi;
    // Cyphertext as a big integer
    var result = "";
    // Plaintext result
    /*
* Carve up the cyphertext into blocks.
*/
    for (i = 0; i < blocks.length; ++i) {
        /*
  * Depending on the radix being used for the key, convert this cyphertext
  * block into a big integer.
  */
        if (key.radix == 16) {
            bi = biFromHex(blocks[i]);
        } else {
            bi = biFromString(blocks[i], key.radix);
        }
        /*
  * Decrypt the cyphertext.
  */
        b = key.barrett.powMod(bi, key.d);
        /*
  * Convert the decrypted big integer back to the plaintext string.  Since
  * we are using big integers, each element thereof represents two bytes of
  * plaintext.
  */
        for (j = 0; j <= biHighIndex(b); ++j) {
            result += String.fromCharCode(b.digits[j] & 255, b.digits[j] >> 8);
        }
    }
    /*
* Remove trailing null, if any.
*/
    if (result.charCodeAt(result.length - 1) == 0) {
        result = result.substring(0, result.length - 1);
    }
    /*
* Return the plaintext.
*/
    return (result);
}

function BigInt(flag)
{
	if (typeof flag == "boolean" && flag == true) {
		this.digits = null;
	}
	else {
		this.digits = ZERO_ARRAY.slice(0);
	}
	this.isNeg = false;
}
function setMaxDigits(value)
{
	maxDigits = value;
	ZERO_ARRAY = new Array(maxDigits);
	for (var iza = 0; iza < ZERO_ARRAY.length; iza++) ZERO_ARRAY[iza] = 0;
	bigZero = new BigInt();
	bigOne = new BigInt();
	bigOne.digits[0] = 1;
}

var rsa = function (arg) {
  setMaxDigits(130);
  var PublicExponent = "10001";
  var modulus = "be44aec4d73408f6b60e6fe9e3dc55d0e1dc53a1e171e071b547e2e8e0b7da01c56e8c9bcf0521568eb111adccef4e40124b76e33e7ad75607c227af8f8e0b759c30ef283be8ab17a84b19a051df5f94c07e6e7be5f77866376322aac944f45f3ab532bb6efc70c1efa524d821d16cafb580c5a901f0defddea3692a4e68e6cd";
  var key = new RSAKeyPair(PublicExponent, "", modulus);
  return encryptedString(key, arg);
}
console.log(rsa('123456'));



