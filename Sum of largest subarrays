#include <iostream>
using namespace std;
int maxSub(int n, int a[]){
	int maxSum = 0, Sum = 0, i;
	for (i = 0; i < n; i++){
		Sum += a[i];
		if (Sum>maxSum)
			maxSum = Sum;
		if (Sum < 0)
			Sum = 0;
	}
	return maxSum;
}
int main(){
	int n, Max, i, arr[100];
	cout << "Please enter the length of array:" << endl;
	cin >> n;
	cout << "Please enter the array:" << endl;
	for (i = 0; i < n; i++)
		cin >> arr[i];
	cout << "The sum of largest subarrays is:" << endl << maxSub(n, arr);
	return 1;
}
