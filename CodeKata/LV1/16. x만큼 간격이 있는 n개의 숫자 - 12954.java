/* [연습문제] x만큼 간격이 있는 n개의 숫자 */

// 동적 배열
import java.util.List;
import java.util.ArrayList;
class Solution {
    public long[] solution(int x, int n) {
        List<Long> answer = new ArrayList<>();
        for (int i = 1; i < n + 1; i++) {
            answer.add((long)i * x);
        }
        return answer.stream().mapToLong(i -> i).toArray();
    }
}

class Solution {
    public long[] solution(int x, int n) {
        long[] answer = new long[n];
        for (int i = 0; i < n; i++) {
            answer[i] = (long)x * (i + 1);
        }
        return answer;
    }
}