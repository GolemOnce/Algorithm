/* [연습문제] 제일 작은 수 제거하기 */

// stream()을 쓸거면 그냥 싹 쓰던지... for문을 쓸거면 for문만 쓰던지...
import java.util.*;

class Solution {
    public int[] solution(int[] arr) {
        List<Integer> answer = new ArrayList<>();
        if (arr.length == 1) {
            answer.add(-1);
        } else {
            int min = arr[0];
            for (int i: arr) {
                if (i < min) min = i;
            }
            for (int i = 0; i < arr.length; i++) {
                if (arr[i] != min) answer.add(arr[i]);
            }
        }
        return answer.stream().mapToInt(i->i).toArray();
    }
}

// getAsInt(), filter()
class Solution {
  public int[] solution(int[] arr) {
      if (arr.length <= 1) return new int[]{ -1 };
      int min = Arrays.stream(arr).min().getAsInt();
      return Arrays.stream(arr).filter(i -> i != min).toArray();
  }
}