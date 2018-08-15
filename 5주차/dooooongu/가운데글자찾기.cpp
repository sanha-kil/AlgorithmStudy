//프로그래머스 level1 가운데 글자 찾기
#include <string>
#include <vector>

using namespace std;

string solution(string s) {
    int a=s.size()-1;
     string answer = "";
    if (a%2 ==0 ){
        answer = s[a/2];
    }
    else {
        
        answer = s.substr(a/2,2);
            
    }

   
    return answer;
}