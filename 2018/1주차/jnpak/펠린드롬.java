class Æç¸°µå·Ò {
	public static int solution(String s) {
		int answer = 0;
		int max = 0;
		String subs= "";
		
		for (int i = 0; i <= s.length()-1; i++) {
			for (int j = i + 1; j <= s.length(); j++) {

				subs = s.substring(i, j);
				if (new StringBuffer(subs).reverse().toString().equals(subs)) {
					if (max < subs.length()) {
						max = subs.length();
					}
				}
			}
		}
		answer = max;
		return answer;

	}

	public static void main(String args[]) {
		String w = "abcdcaba";

		int b = solution(w);
		System.out.println(b);
	}
}