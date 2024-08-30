#include <iostream>
#include <vector>
using namespace std;

int main() {
    freopen("backin.txt", "r", stdin);
    freopen("backout.txt", "w", stdout);
    int towns, capacity;
    cin >> towns >> capacity;
    vector<int> distances(towns - 1);
    for (int i = 0; i < towns - 1; i++) {
        cin >> distances[i];
    }
    vector<int> food(towns - 1);
    for (int i = 0; i < towns - 1; i++) {
        cin >> food[i];
    }
    vector<int> bestPriceYet(towns - 1);
    bestPriceYet[0] = food[0];
    for (int i = 1; i < towns - 1; i++) {
        bestPriceYet[i] = min(bestPriceYet[i - 1], food[i]);
    }
    int moneySpent = 0;
    for (int i = 0; i < towns - 1; i++) {
        moneySpent += distances[i] * bestPriceYet[i];
    }
    cout << moneySpent;


}