
class Solution
{
    public static int solution(String s)
    {
        int answer = 0;
        int a=0;
        
        if(new StringBuffer(s).reverse().toString().equals(s)) {
        	a=s.length();
        } else return answer;


        answer = a/2;
        return answer;
    }
    
    public static void main(String args[]) {
    	String w = "abccba";
    	
    	int b = solution(w);
    	System.out.println(b);
    }
}