package CodeKata.LV3;

/* [월간 코드 챌린지 시즌1] 두 개 뽑아서 더하기 */

import java.util.*;

// ArrayList -> O(n^3)
class Solution {
    public int[] solution(int[] numbers) {
        List<Integer> answer = new ArrayList<>();
        for (int i = 0; i < numbers.length - 1; i++) {
            for (int j = i + 1; j < numbers.length; j++) {
                int tmp = numbers[i] + numbers[j];
                if (!answer.contains(tmp)) answer.add(tmp); 
            }
        }
        return answer.stream().mapToInt(i -> i).sorted().toArray();
    }
}

// HashSet -> O(n^2)
class Solution2 {
     public int[] solution(int[] numbers) {
        Set<Integer> set = new HashSet<>();
        for(int i=0; i < numbers.length - 1; i++) {
            for(int j = i + 1; j< numbers.length; j++) {
                set.add(numbers[i] + numbers[j]);
            }
        }
        return set.stream().sorted().mapToInt(Integer::intValue).toArray();
    }
}