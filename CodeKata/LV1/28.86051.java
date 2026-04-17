/* [월간 코드 챌린지 시즌3] 없는 숫자 더하기 */

import java.util.*;

// Stream()
class Solution {
    public int solution(int[] numbers) {
        return 45 - Arrays.stream(numbers).sum();
    }
}

// 정석 for each문
class Solution {
    public int solution(int[] numbers) {
        int sum = 45;
        for (int i : numbers) {
            sum -= i;
        }
        return sum;
    }
}