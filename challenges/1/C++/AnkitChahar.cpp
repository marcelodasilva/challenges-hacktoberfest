#include<bits/stdc++.h>

using namespace std;

int main()
{
    vector<int> inputArray;
    for(int i = 0; i < 5; i++)
    {
        inputArray.push_back(rand() % 9000 + 1);
    }
    for(int i = 0; i < inputArray.size(); i++)
    {
        cout << inputArray[i] << " ";
    }
    int sum = 0;
    for(int i = 0; i < inputArray.size(); i++)
    {
        sum += inputArray[i];
    }
    cout << endl << "Sum is " << sum << endl;
    return 0;
}