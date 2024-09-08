#役満貫の判定、符の計算、基本点の計算、支払いの計算の順で計算する予定

#基本点を計算する関数。飜は場ゾロを含めない

def B_Point(hu, han):

    MAXIMAM = 2000;

    base = hu * 2 ** (han + 2);

    if base > MAXIMAM:

        base = 2000;

    return base;


if __name__ == "__main__":

    MIN = 20;

    MAX = 2000;

    #子の出上がりの点数表を書かせる（ピンヅモ、チートイは考慮しない）

    i = MIN // 10;

    while True:

        i = i + 1;

        print(i * 10, "符", end="");

        j = 0;

        while True:

            j = j + 1;

            base = B_Point(i * 10, j);

            if base < MAX:

                points = base * 4;

                print(",", points if points % 100 == 0 else points // 100 * 100 + 100, end="");

            else:

                print("\n");

                break

        #１７０符が最高符（連風牌雀頭、幺九牌暗カン２面子、暗順子２面子、で愚形待ちして出和了りした場合が１６４符）

        if i >= 17:

            break

