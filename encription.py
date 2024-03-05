import random

###############################NECESSARY_FUNCTION###############################
def P(z):
    #iteration_1
    z[7] = z[3] ^ z[7]
    z[6] = z[2] ^ z[6]
    z[5] = z[1] ^ z[5]
    z[4] = z[0] ^ z[4]
    z[3] = z[4] ^ z[3]
    z[2] = z[5] ^ z[2]
    z[1] = z[7] ^ z[1]
    z[0] = z[6] ^ z[0]
    #iteration_2
    z[7] = z[2] ^ z[7]
    z[6] = z[1] ^ z[6]
    z[5] = z[0] ^ z[5]
    z[4] = z[3] ^ z[4]
    z[3] = z[7] ^ z[3]
    z[2] = z[6] ^ z[2]
    z[1] = z[5] ^ z[1]
    z[0] = z[4] ^ z[0]
    return z

def S(n):
    s_box = [ 0xe1, 0x42, 0x3e, 0x81, 0x4e, 0x17, 0x9e, 0xfd, 0xb4, 0x3f, 0x2c,
              0xda, 0x31, 0x1e, 0xe0, 0x41, 0xcc, 0xf3, 0x82, 0x7d, 0x7c, 0x12,
              0x8e, 0xbb, 0xe4, 0x58, 0x15, 0xd5, 0x6f, 0xe9, 0x4c, 0x4b, 0x35,
              0x7b, 0x5a, 0x9a, 0x90, 0x45, 0xbc, 0xf8, 0x79, 0xd6, 0x1b, 0x88,
              0x02, 0xab, 0xcf, 0x64, 0x09, 0x0c, 0xf0, 0x01, 0xa4, 0xb0, 0xf6,
              0x93, 0x43, 0x63, 0x86, 0xdc, 0x11, 0xa5, 0x83, 0x8b, 0xc9, 0xd0,
              0x19, 0x95, 0x6a, 0xa1, 0x5c, 0x24, 0x6e, 0x50, 0x21, 0x80, 0x2f,
              0xe7, 0x53, 0x0f, 0x91, 0x22, 0x04, 0xed, 0xa6, 0x48, 0x49, 0x67,
              0xec, 0xf7, 0xc0, 0x39, 0xce, 0xf2, 0x2d, 0xbe, 0x5d, 0x1c, 0xe3,
              0x87, 0x07, 0x0d, 0x7a, 0xf4, 0xfb, 0x32, 0xf5, 0x8c, 0xdb, 0x8f,
              0x25, 0x96, 0xa8, 0xea, 0xcd, 0x33, 0x65, 0x54, 0x06, 0x8d, 0x89,
              0x0a, 0x5e, 0xd9, 0x16, 0x0e, 0x71, 0x6c, 0x0b, 0xff, 0x60, 0xd2,
              0x2e, 0xd3, 0xc8, 0x55, 0xc2, 0x23, 0xb7, 0x74, 0xe2, 0x9b, 0xdf,
              0x77, 0x2b, 0xb9, 0x3c, 0x62, 0x13, 0xe5, 0x94, 0x34, 0xb1, 0x27,
              0x84, 0x9f, 0xd7, 0x51, 0x00, 0x61, 0xad, 0x85, 0x73, 0x03, 0x08,
              0x40, 0xef, 0x68, 0xfe, 0x97, 0x1f, 0xde, 0xaf, 0x66, 0xe8, 0xb8,
              0xae, 0xbd, 0xb3, 0xeb, 0xc6, 0x6b, 0x47, 0xa9, 0xd8, 0xa7, 0x72,
              0xee, 0x1d, 0x7e, 0xaa, 0xb6, 0x75, 0xcb, 0xd4, 0x30, 0x69, 0x20,
              0x7f, 0x37, 0x5b, 0x9d, 0x78, 0xa3, 0xf1, 0x76, 0xfa, 0x05, 0x3d,
              0x3a, 0x44, 0x57, 0x3b, 0xca, 0xc7, 0x8a, 0x18, 0x46, 0x9c, 0xbf,
              0xba, 0x38, 0x56, 0x1a, 0x92, 0x4d, 0x26, 0x29, 0xa2, 0x98, 0x10,
              0x99, 0x70, 0xa0, 0xc5, 0x28, 0xc1, 0x6d, 0x14, 0xac, 0xf9, 0x5f,
              0x4f, 0xc4, 0xc3, 0xd1, 0xfc, 0xdd, 0xb2, 0x59, 0xe6, 0xb5, 0x36,
              0x52, 0x4a, 0x2a ]
    return s_box[n]
###############################NECESSARY_FUNCTION###############################

#################################GENERATOR_KEYS#################################
def gsd(a,b):
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a

    return (a + b)

def FERMA(K):
    k = 100
    for i in range(k):
        a = random.randint(2, K-1)
        x = pow(a, (K-1), K)
        if gsd(a, K) > 1:
            return False
        if x != 1:
            return False
    return True

def generation_odd_key():
    len_key = 192
    input_key = random.randint(2**(len_key-1), 2**len_key-1)

    while input_key % 2 == 0:
        input_key = random.randint(2**(len_key-1), 2**len_key-1)
    return input_key

def key_calculation():
    key = generation_odd_key()
    while not FERMA(key):
        key = generation_odd_key()
    return key
#################################GENERATOR_KEYS#################################

#################################KEY__EXTENTION#################################
def f(X):
    for i in range(8):
        X[i] = S(X[i])
    X = P(X)
    return X

def splitting_key(K):
    V = 0xAC217638FD08B954
    if (K >> 192) > 0:
        K1 = (K - ((K >> 64) << 64))
        K2 = ((K >> 64) - ((K >> 128) << 64))
        K3 = ((K >> 128) - ((K >> 192) << 64))
        K4 = (K >> 192)
    elif (K >> 128) > 0:
        K1 = (K - ((K >> 64) << 64))
        K2 = ((K >> 64) - ((K >> 128) << 64))
        K3 = ((K >> 128) - ((K >> 192) << 64))

        KP = [(V - ((V >> 8) << 8)), ((V >> 8) - ((V >> 16) << 8)),
              ((V >> 16) - ((V >> 24) << 8)), ((V >> 24) - ((V >> 32) << 8)),
              ((V >> 32) - ((V >> 40) << 8)), ((V >> 40) - ((V >> 48) << 8)),
              ((V >> 48) - ((V >> 56) << 8)), ((V >> 56) - ((V >> 64) << 8))]

        for i in range(8):
            KP[i] = S(S(S(S(KP[i]))))

        K4 = ((KP[7] << 56) + (KP[6] << 48) + (KP[5] << 40) + (KP[4] << 32) +
                (KP[3] << 24) + (KP[2] << 16) + (KP[1] << 8) + KP[0])

    else:
        K1 = (K - ((K >> 64) << 64))
        K2 = ((K >> 64) - ((K >> 128) << 64))

        KP = [(V - ((V >> 8) << 8)), ((V >> 8) - ((V >> 16) << 8)),
              ((V >> 16) - ((V >> 24) << 8)), ((V >> 24) - ((V >> 32) << 8)),
              ((V >> 32) - ((V >> 40) << 8)), ((V >> 40) - ((V >> 48) << 8)),
              ((V >> 48) - ((V >> 56) << 8)), ((V >> 56) - ((V >> 64) << 8))]

        KP3 = [0]*8
        KP4 = [0]*8

        for i in range(8):
            KP3[i] = S(S(S(KP[i])))
            KP4[i] = S(KP3[i])

        K3 = ((KP3[7] << 56) + (KP3[6] << 48) + (KP3[5] << 40) + (KP3[4] << 32) +
                (KP3[3] << 24) + (KP3[2] << 16) + (KP3[1] << 8) + KP3[0])

        K4 = ((KP4[7] << 56) + (KP4[6] << 48) + (KP4[5] << 40) + (KP4[4] << 32) +
                (KP4[3] << 24) + (KP4[2] << 16) + (KP4[1] << 8) + KP4[0])

    return K1, K2, K3, K4

def G(K_i):
    U0 = 0xDCAF5678923568BADCFDFAA654963AF6

    k = [0]*8

    k[0] = K_i - ((K_i >> 8) << 8)
    k[1] = (K_i >> 8) - ((K_i >> 16) << 8)
    k[2] = (K_i >> 16) - ((K_i >> 24) << 8)
    k[3] = (K_i >> 24) - ((K_i >> 32) << 8)
    k[4] = (K_i >> 32) - ((K_i >> 40) << 8)
    k[5] = (K_i >> 40) - ((K_i >> 48) << 8)
    k[6] = (K_i >> 48) - ((K_i >> 56) << 8)
    k[7] = (K_i >> 56)

    k = f(k)

    kk = ((k[7] << 56) + (k[6] << 48) + (k[5] << 40) + (k[4] << 32) +
          (k[3] << 24) + (k[2] << 16) + (k[1] << 8) + (k[0]))

    kkk = [0]*4

    for i in range(4):
        U1 = [ (U0 >> 120),
               ((U0 >> 112) - ((U0 >> 120) << 8)),
               ((U0 >> 104) - ((U0 >> 112) << 8)),
               ((U0 >> 96) - ((U0 >> 104) << 8)),
               ((U0 >> 88) - ((U0 >> 96) << 8)),
               ((U0 >> 80) - ((U0 >> 88) << 8)),
               ((U0 >> 72) - ((U0 >> 80) << 8)),
               ((U0 >> 64) - ((U0 >> 72) << 8))]

        U2 = [ ((U0 >> 56) - ((U0 >> 64) << 8)),
               ((U0 >> 48) - ((U0 >> 56) << 8)),
               ((U0 >> 40) - ((U0 >> 48) << 8)),
               ((U0 >> 32) - ((U0 >> 40) << 8)),
               ((U0 >> 24) - ((U0 >> 32) << 8)),
               ((U0 >> 16) - ((U0 >> 24) << 8)),
               ((U0 >> 8) - ((U0 >> 16) << 8)),
               (U0 - ((U0 >> 8) << 8))]

        U1 = f(U1)
        U2 = f(U2)

        U0 = ((U1[0] << 120) + (U1[1] << 112) + (U1[2] << 104) + (U1[3] << 96) +
              (U1[4] << 88) + (U1[5] << 80) + (U1[6] << 72) + (U1[7] << 64) +
              (U2[0] << 56) + (U2[1] << 48) + (U2[2] << 40) + (U2[3] << 32) +
              (U2[4] << 24) + (U2[5] << 16) + (U2[6] << 8) + (U2[7]))
        kkk[i] = kk ^ U0
        U0 = kkk[i]

    return kkk
#################################KEY__EXTENTION#################################


###################################ENCRYPTION###################################
def FIX_BIT(number, bits):
    return format(number & (2**bits) - 1, "0{}b".format(bits))

def BP_P(X):
    XX = [0]*16

    for i in range(16):
        XX[i] = (X >> (8 * i)) - ((X >> (8 * (i + 1))) << 8)

    X = ((XX[15] << 120) + (XX[10] << 112) + (XX[5] << 104) + (XX[0] << 96) +
        (XX[11] << 88) + (XX[6] << 80) + (XX[1] << 72) + (XX[12] << 64) +
        (XX[7] << 56) + (XX[2] << 48) + (XX[13] << 40) + (XX[8] << 32) +
        (XX[3] << 24) + (XX[14] << 16) + (XX[9] << 8) + (XX[4]))
    return X

def BP_M(X):
    XX = [0]*16

    for i in range(16):
        XX[i] = (X >> (8 * i)) - ((X >> (8 * (i + 1))) << 8)

    X = ((XX[15] << 120) + (XX[2] << 112) + (XX[5] << 104) + (XX[8] << 96) +
        (XX[11] << 88) + (XX[14] << 80) + (XX[1] << 72) + (XX[4] << 64) +
        (XX[7] << 56) + (XX[10] << 48) + (XX[13] << 40) + (XX[0] << 32) +
        (XX[3] << 24) + (XX[6] << 16) + (XX[9] << 8) + (XX[12]))
    return X

def IT(X, K13, K14):
    XX = X ^ K13

    XXX = [(XX - ((XX >> 32) << 32)),
           ((XX >> 32) - ((XX >> 64) << 32)),
           ((XX >> 64) - ((XX >> 96) << 32)),
           (XX >> 96)]

    KK14 = [(K14 - ((K14 >> 32) << 32)),
           ((K14 >> 32) - ((K14 >> 64) << 32)),
           ((K14 >> 64) - ((K14 >> 96) << 32)),
           (K14 >> 96)]

    for i in range(4):
        if (XXX[i] + (KK14[i])) > (2**32):
            XXX[i] = (XXX[i] + (KK14[i])) - (2**32)
        else:
            XXX[i] = (XXX[i] + (KK14[i]))

    X = (XXX[3] << 96) + (XXX[2] << 64) + (XXX[1] << 32) + (XXX[0])

    X = BP_P(X)

    return X

def FT(X, K15, K16):

    X = BP_M(X)

    XX = [(X - ((X >> 32) << 32)),
           ((X >> 32) - ((X >> 64) << 32)),
           ((X >> 64) - ((X >> 96) << 32)),
           (X >> 96)]

    KK15 = [(K15 - ((K15 >> 32) << 32)),
           ((K15 >> 32) - ((K15 >> 64) << 32)),
           ((K15 >> 64) - ((K15 >> 96) << 32)),
           (K15 >> 96)]

    for i in range(4):
        XX[i] = (XX[i] - (KK15[i]))
        if XX[i] < 0:
            XX[i] = XX[i] + 2**32

    X = (XX[3] << 96) + (XX[2] << 64) + (XX[1] << 32) + (XX[0])

    X = X ^ K16
    return X

def BRL(X_64):
    X_8 = (X_64 >> 56)
    X_64 = ((X_64 - ((X_64 >> 56) << 56)) << 8) + X_8
    return X_64

def F(X_R, K):
    k_R = [(K - ((K >> 8) << 8)),
           ((K >> 8) - ((K >> 16) << 8)),
           ((K >> 16) - ((K >> 24) << 8)),
           ((K >> 24) - ((K >> 32) << 8)),
           ((K >> 32) - ((K >> 40) << 8)),
           ((K >> 40) - ((K >> 48) << 8)),
           ((K >> 48) - ((K >> 56) << 8)),
           ((K >> 56) - ((K >> 64) << 8))]

    k_L = [((K >> 64) - ((K >> 72) << 8)),
           ((K >> 72) - ((K >> 80) << 8)),
           ((K >> 80) - ((K >> 88) << 8)),
           ((K >> 88) - ((K >> 96) << 8)),
           ((K >> 96) - ((K >> 104) << 8)),
           ((K >> 104) - ((K >> 112) << 8)),
           ((K >> 112) - ((K >> 120) << 8)),
           (K >> 120)]

    X_RR = [(X_R - ((X_R >> 8) << 8)),
           ((X_R >> 8) - ((X_R >> 16) << 8)),
           ((X_R >> 16) - ((X_R >> 24) << 8)),
           ((X_R >> 24) - ((X_R >> 32) << 8)),
           ((X_R >> 32) - ((X_R >> 40) << 8)),
           ((X_R >> 40) - ((X_R >> 48) << 8)),
           ((X_R >> 48) - ((X_R >> 56) << 8)),
           (X_R >> 56)]
    for i in range(8):
        X_RR[i] = X_RR[i] ^ k_L[i]
        X_RR[i] = S(X_RR[i])
    X_RR = P(X_RR)
    for i in range(8):
        X_RR[i] = X_RR[i] ^ k_R[i]
        X_RR[i] = S(X_RR[i])
        X_R = ((X_RR[7] << 56) + (X_RR[6] << 48) +
               (X_RR[5] << 40) + (X_RR[4] << 32) +
               (X_RR[3] << 24) + (X_RR[2] << 16) +
               (X_RR[1] << 8) + (X_RR[0]))
    X_R = BRL(X_R)
    return X_R

def ENCODE(X, K):

    K1, K2, K3, K4 = splitting_key(K)
    k = G(K1) + G(K2) + G(K3) + G(K4)

    X = IT(X, k[12], k[13])

    X_R = X - ((X >> 64) << 64)
    X_L = X >> 64
    X_S = 0

    for i in range(12):
        X_S = X_L ^ F(X_R, k[i])
        X_L = X_R
        X_R = X_S

    X = (X_L << 64) + (X_R)

    X = FT(X, k[14], k[15])
    print("ENCODE: ", X)
    return X
###################################ENCRYPTION###################################

#####################################PROGRAM####################################
input_file = open("input_file.txt", encoding = 'latin-1')
output_file = open("encoded_file.txt", "w", encoding = 'latin-1')
keys = open("keys.txt", "w")

code = 0
i = 0

while True:
    char = input_file.read(1)
    if not char:
        break
    code = (code << 8) + ord(char)
    i += 1
    if i == 16:
        i = 0
        K = key_calculation()
        output_file.write(FIX_BIT(ENCODE(code, K), 128))
        code = 0
        keys.write(str(K))
        keys.write('\n')

if code != 0:
    K = key_calculation()
    code = code << ((16 - i) * 8)
    output_file.write(FIX_BIT(ENCODE(code, K), 128))
    keys.write(str(K))

input_file.close()
output_file.close()
keys.close()
#####################################PROGRAM####################################