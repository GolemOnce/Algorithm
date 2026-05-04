package CodeKata.LV3;

/* [정렬] K번째수 */

import java.util.*;

// stream() + ArrayList
class Solution {
    public int[] solution(int[] array, int[][] commands) {
        List<Integer> answer = new ArrayList<>();
        for (int[] command: commands) {
            answer.add(Arrays.stream(array, command[0]-1, command[1])
                .sorted()
                .toArray()[command[2]-1]);
        }
        return answer.stream().mapToInt(i->i).toArray();
    }
}

// copyOfRange() + 배열 크기 명시
class Solution2 {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        for (int i = 0; i < commands.length; i++) {
            int[] tmp = Arrays.copyOfRange(array, commands[i][0]-1, commands[i][1]);
            Arrays.sort(tmp);
            answer[i] = tmp[commands[i][2]-1];
        }
        return answer;
    }
}