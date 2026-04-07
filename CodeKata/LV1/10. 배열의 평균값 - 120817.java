/* [코딩테스트 입문] 배열의 평균값 */

import java.util.Arrays;

class Solution {
    public double solution(int[] numbers) {
        double answer = 0;
        for (int i = 0; i < numbers.length; i++)
            answer += numbers[i];
        return answer/numbers.length;
    }
}


// Arrays.stream() 활용
class Solution2 {
    public double solution(int[] numbers) {
        return Arrays.stream(numbers).average().orElse(0);
    }
}