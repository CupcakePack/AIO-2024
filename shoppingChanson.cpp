#include <iostream>
#include <deque>
using namespace std;
int main() {
    // shopping spree implementation with deque
    freopen("shopin.txt", "r", stdin);
    freopen("shopout.txt", "w", stdout);
    int amount, coupons;
    cin >> amount >> coupons;
    deque<int> items(amount);
    for (int i = 0; i < amount; i++) {
        cin >> items[i];
    }
    int spent = 0;
    for (int i = 0; i < coupons; i++) {
        spent += items[0];
        items.pop_back();
        items.pop_front();
    }
    while (items.size() != 0) {
        spent += items[items.size() - 1];
        items.pop_back();
        items.pop_back();
    }
    cout << spent;

}
