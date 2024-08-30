#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main() {
    freopen("backin.txt", "r", stdin);
    freopen("backout.txt", "w", stdout);
    int towns, capacity;
    cin >> towns >> capacity;
    vector<int> food(towns - 1);
    vector<int> distances(towns - 1);
    int needToBuy = 0;
    int moneySpent = 0;
    for (int i = 0; i < towns - 1; i++) {
        cin >> distances[i];
        needToBuy += distances[i];
    }
    for (int i = 0; i < towns - 1; i++) {
        cin >> food[i];
    }
    int itemsInBag = 0;
    for (int i = 0; i < towns - 1; i++) {
        if (i != 0) {
            itemsInBag -= distances[i - 1];
        }
        int space = capacity - itemsInBag;
        int buying = min(space, needToBuy);
        moneySpent += buying * food[i];
        itemsInBag += buying;
        needToBuy -= buying;
    }
    cout << moneySpent;

}