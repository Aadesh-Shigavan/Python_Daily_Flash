#include<iostream>

int main() {
	for(int i = 0; i < 4; i++) {
		for(int j = 0; j <= i; j++) {
			std::cout << i + 1 << " ";
		}
		std::cout << std::endl;
	}
	return 0;
}