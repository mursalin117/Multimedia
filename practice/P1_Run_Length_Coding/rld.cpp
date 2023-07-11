#include <bits/stdc++.h>
using namespace std;

int main() {
    FILE *f1 = freopen("compressed.txt", "r", stdin);
    FILE *f2 = freopen("decompressed.txt", "w", stdout);

    string str;
    int i, j;
    bool flag = false;

    while(getline(cin, str)) {
        if (flag) {
            cout << endl;
        }

        for (i = 0; i < str.size(); i++) {
            if (str[i] == (char)255) {
                for (j = 0; j < (int)str[i+1]; j++) {
                    cout << str[i+2];
                }
                i += 2;
            }
            else {
                cout << str[i];
            }
        }
        flag = true;
    }

    fclose(f1);
    fclose(f2);

    return 0;
}