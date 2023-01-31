#include <bits/stdc++.h>
using namespace std;

int main() {
    FILE *f3 = freopen("compressed.txt", "r", stdin);
    FILE *f4 = freopen("decompressed.txt", "w", stdout);

    string str;
    int i, j;
    bool flag = false;

    while (getline(cin, str)) {
        if (flag) {
            cout << endl;
        }

        for (i = 0; i < str.size(); i++) {
            for (j = 0; j < str[i+1]-'0'; j++) {
                cout << str[i];
            }
            i++;
        }
        flag = true;
    }
    fclose(f3);
    fclose(f4);

    return 0;
}