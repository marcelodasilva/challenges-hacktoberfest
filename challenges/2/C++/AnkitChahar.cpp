#include<bits/stdc++.h>

using namespace std;

int main()
{
    vector<int> inputArray(5);
    for(int i = 0; i < 5; i++)
    {
        cin >> inputArray[i];
    }
    int sum = 0;
    for(int i = 0; i < 5; i++)
    {
        sum += inputArray[i];
    }
    cout << "Average is " << sum/5 << endl;
    return 0;
}