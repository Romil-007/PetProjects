//including libraries
#include <iostream>
#include <unistd.h>

//using standard scope for functions
using namespace std;

//entry level function
int main(){

    //initializing some variables
    string c , result;
    //this will help to get a diff random number each time after compiling
    srand((unsigned int) time(NULL));
    int a = rand() % 2;

    //Letting user initiate the coin toss
    cout<<"Do you want to start coin toss(y/n)?";
    cin>>c;
    if(c=="y" || c == "Y"){
    
    sleep(2);

    //using short hand if else
    result = (a==0)? "Heads":"Tails";
    cout<< result;
    }
    

    //essential
    return 0;
}