#include<iostream>
using namespace std;


void countFrequency(int arr[], int size){
    int count = 1, countedList[] = {};

    for(int i = 0; i < size; i++){
        count = 1;
        for(int j = i + 1; j < size; j++){
            if(arr[i] == arr[j]){
                count ++;
            }
        }
        cout << arr[i] << count <<endl;
    }
}


int main(){
    int arr[] =  {1, 1, 2, 4, 6, 7, 7, 7};
    int size = sizeof(arr)/sizeof(int);
    countFrequency(arr, size);
    return 0;
}