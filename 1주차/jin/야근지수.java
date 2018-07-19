class Solution {
	public static long solution(int n, int[] works) {
		long answer = 0;

		if (works.length == 0) { // 배열길이 0인경우 0 리턴
			return answer;
		} else {
			for (int j = 1; j <= n; j++) { // 남은시간 n 만큼 for문 실행
				int m = 0; // m은 배열 인덱스 번호
				int max = works[0];
				for (int i = 0; i < works.length; i++) {

					if (works[i] > max) { // 배열의 최대값위치를 m에 저장
						max = works[i]; 
						m = i;
					}
				}
				works[m] = works[m] - 1; //최대값 1만큼 감소시킴
			}
		}
		for (int k = 0; k < works.length; k++) {
            if(works[k]>=0){
			long w = works[k] * works[k]; // w 배열원소 제곱
			answer = answer + w; // 제곱한 값 모두 더함
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
