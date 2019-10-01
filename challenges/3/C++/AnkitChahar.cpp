#include<bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin>>n;
    if(n < 1)
    {
        cout << "Enter a number greater than 0" << endl;
        return 0;
    }
    vector<int> array;
    array.push_back(0);
    array.push_back(1);
    for(int i = 2; i < n; i++)
    {
        array.push_back(array[i - 1] + array[i - 2]);
    }
    for(int i = 0; i < n; i++)
    {
        cout << array[i] << " ";
    }
    return 0;
}