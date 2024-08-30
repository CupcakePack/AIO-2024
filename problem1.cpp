#include <iostream>
using namespace std;
int main() {
    freopen("javelin.txt", "r", stdin);
    freopen("javelout.txt", "w", stdout);
    int students;
    cin >> students;
    int leader = 0;
    int cnt = 0;
    for (int i = 0; i < students; i++) {
        int f;
        cin >> f;
        if (f > leader) {
            cnt++;
            leader = f;
        }
    }
    cout << cnt;
    return 0;
}