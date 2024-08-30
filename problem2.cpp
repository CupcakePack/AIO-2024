#include <iostream>
#include <vector>
using namespace std;

int main() {
    freopen("bookin.txt", "r", stdin);
    freopen("bookout.txt", "w", stdout);
    int characters;
    cin >> characters;
    vector<char> chars(characters);
    bool questionIsFirst = false;
    for (int i = 0; i < characters; i++) {
        char c;
        cin >> c;
        if (i == 1 and questionIsFirst) {
            chars[0] = c;
        }
        if (c == '?') {
            if (i == 0) {
                questionIsFirst = true;
            }
            else {
                c = chars[i - 1];
            }
        }
        chars[i] = c;
    }
    int cnt = 0;
    for (int i = 1; i < chars.size(); i++) {
        if (chars[i] == chars[i - 1]) {
            cnt++;
        }
    }
    cout << cnt;
}
