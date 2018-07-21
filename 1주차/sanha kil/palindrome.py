# 가장 긴 팔린드롬 알고리즘 구현
# 팔린드롬 : 앞뒤를 뒤집어도 똑같은 문자열
# 입력 문자열 s의 팔린드롬을 성립하는 가장 긴 부분문자열의 길이를 출력하도록 코딩

def palindrome(s):
    sentence = []
    for i in range(0, len(s)):                                  # len(s) : 입력값 s의 길이를 출력하는 내장 객체
        for j in range(1, len(s)+1):
            if s[i:j] and str(s[i:j]) == str(s[i:j])[::-1]:     # [::-1]을 이용하여 문자열을 뒤집을 수 있음
                sentence.append(len(s[i:j]))                    # append(a) : 리스트의 마지막에 데이터를 추가
            if s[j:i] and str(s[j:i]) == str(s[j:i])[::-1]:
                sentence.append(len(s[j:i]))
    return max(sentence)                                        # max(s) : 반복가능한 자료형을 받아 그 중 최대값을 리턴해 줌
 
if __name__ == "__main__":
    a = input("문자열을 입력하세요 : ")
    print(palindrome(a))