class Solution {
  public int solution(int n) {
      int answer = 0;
      answer= pb(n)%1000000007;
      return answer;
  }
    public static int pb(int a){
        if(a==1) {
          return 1;
      } else if (a==2) {
          return 2;
      } else {
          return pb(a-2)+pb(a-1);
        }
    }
}