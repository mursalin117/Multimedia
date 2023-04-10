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
            if (str[i+1] == '(') {
                int cnt = 0;
                j = i+2;
                while (str[j] != ')') {
                    cnt = cnt * 10 + str[j] - '0';
                    j++;
                }
                for (int k = 0; k < cnt; k++) {
                    cout << str[i];
                }
            }
            i = j;
        }
        flag = true;
    }
    fclose(f3);
    fclose(f4);

    return 0;
}