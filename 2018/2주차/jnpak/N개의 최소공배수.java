class Solution {
	public int solution(int[] arr) {
		int answer = 0;
		answer=lcm(arr);
		return answer;
	}

	public static int gcd(int p, int q) {
		while (q != 0){
            int t;
            t=p%q;
            p=q;
            q=t;
        }
        return p;
	}

	public static int gcd(int[] array) {
		int result;

		if (array.length <= 1)
			return array[0];

		result = gcd(array[0], array[1]);
		for (int i = 2; i < array.length; ++i)
			result = gcd(result, array[i]);

		return result;
	}

	public static int lcm(int[] array) {
		int gcd = gcd(array);
		int lcm = gcd;
		for (int i = 0; i < array.length; ++i) {
			array[i] /= gcd;
			lcm *= array[i];
		}

		return lcm;
	}
}