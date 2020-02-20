import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
	public static int[] solution(int n, long k) {
		int[] answer = new int[n];

		List<Integer> numbers = new ArrayList<>();

		for (int i = 0; i < n; i++) {
			numbers.add(i + 1);
			System.out.println(numbers.get(i));
		}

		long remain;
		int mok;

		ArrayList<Integer> Line = new ArrayList<>();

		while (n > 0) {
			--n;
			remain = k % fac(n);
			mok = (int) (k / fac(n));
			if (remain == 0) {
				Line.add(numbers.get(mok - 1));
				numbers.remove(mok - 1);
				int idx = numbers.size() - 1;
				while (!numbers.isEmpty()) {
					Line.add(numbers.get(idx));
					numbers.remove(idx);
					idx--;

				}
				break;
			}
			Line.add(numbers.get(mok));
			numbers.remove(mok);
			k = remain;

		}

	//	for (int i = numbers.size() - 1; i >= 0; i--) {
	//		Line.add(numbers.get(i));
	//		numbers.remove(i);
	//	}
		for (int i = 0; i < Line.size(); i++) {
			answer[i] = Line.get(i);
		}
		return answer;
	}

	public static long fac(int n) {
		long result = 1;

		for (int i = n; i > 0; i--)
			result *= i;
		return result;
	}

	public static void main(String args[]) {
		Solution sl = new Solution();
		System.out.println(Arrays.toString(sl.solution(4, 13)));
	}
}