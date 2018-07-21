class Solution {
	public static long solution(int n, int[] works) {
		long answer = 0;

		if (works.length == 0) {
			return answer;
		} else {
			for (int j = 1; j <= n; j++) {
				int m = 0;
				int max = works[0];
				for (int i = 0; i < works.length; i++) {

					if (works[i] > max) {
						max = works[i];
						m = i;
					}
				}
				works[m] = works[m] - 1;
			}
		}
		for (int k = 0; k < works.length; k++) {
            if(works[k]>=0){
			long w = works[k] * works[k];
			answer = answer + w;
            }
		}

		return answer;
	}
	public static void main(String args[]) {
		int[] w1 = {4,3,3};
		int[] w2 = {2,1,2};
		int[] w3 = {1,1};

		System.out.println(solution(4,w1));
		System.out.println(solution(1,w2));
		System.out.println(solution(3,w3));

	}
}
