#include <bits/stdc++.h>
using namespace std;

int main() {
    FILE *f3 = freopen("rle_compressed.txt", "r", stdin);
    FILE *f4 = freopen("decompressed.txt", "w", stdout);

    string str;
    int i, j;
    bool flag = false;

    while (getline(cin, str)) {
        if (flag) {
            cout << endl;
        }

        for (i = 0; i < str.size(); i++) {
            if (str[i] == (char)255) {
                for (int j = 0; j < (int)str[i+2]; j++) {
                    cout << str[i+4];
                }
                i += 4;
            }
            else if (str[i] == ' ' && str[i+1] == ' ') { // for single space in input
                cout << str[i];
                i++;
            }
            else if (str[i] == ' ') {
                continue;
            }
            else {
                cout << str[i];
            }
        }
        flag = true;
    }
    fclose(f3);
    fclose(f4);

    return 0;
}
