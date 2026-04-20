package CodeKata.LV2;

/* [월간 코드 챌린지 시즌1] 내적 */

import java.util.stream.IntStream;

class Solution {
    public int solution(int[] a, int[] b) {
        int answer = 0;
        for (int i = 0; i < a.length; i++) {
            answer += a[i] * b[i];
        }
        return answer;
    }
}

// IntStream() 활용
class Solution2 {
    public int solution(int[] a, int[] b) {
        return IntStream.range(0, a.length).map(index -> a[index] * b[index]).sum();    }
}

