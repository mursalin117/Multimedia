#include <bits/stdc++.h>
using namespace std;

int main() {
    FILE *f1 = freopen("input.txt", "r", stdin);
    FILE *f2 = freopen("compressed.txt", "w", stdout);

    string str;
    int i, j;
    bool flag = false;

    while (getline(cin, str)) {
        if (flag) {
            cout << endl;
        }
        for (i = 0; i < str.size(); i++) {
            int cnt = 0;
            for (j = i; str[i] == str[j]; j++) {
                cnt++;
            }
            if (cnt > 1) {
                cout << (char)255 << (char)cnt << str[i];  
            }
            else {
                cout << str[i];
            }
            i = j-1;
        }
        flag = true;
    }
    
    fclose(f1);
    fclose(f2);

    return 0;
}