#include <bits/stdc++.h>
using namespace std;

int main() {
    
    FILE *f1 = freopen("input.txt", "r", stdin);
    FILE *f2 = freopen("rle_compressed.txt", "w", stdout);
    string str;
    int i, j;
    bool flag = false;

    while (getline(cin, str)) {
        if (flag) {
            cout << endl;
        }
        for (i = 0; i < str.size(); i++) {
            int cnt = 0;
            for (j = i; str[j] == str[i]; j++) {
                cnt++;
            }
            
            if (cnt > 1) {
                cout << (char)255 << ' ' << (char)cnt << ' ' << str[i] << ' ';
            } else {
                cout << str[i] << ' ';
            }

            i = j - 1;
        }
        flag = true;
        // cout << (int)str[str.size()] << endl;
    }
    fclose(f1);
    fclose(f2);

    // cout << 123 << endl;

    return 0;
}