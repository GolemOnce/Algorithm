package CodeKata.LV3;

/* [2021 Dev-Matching: 웹 백엔드 개발자(상반기)] 로또의 최고 순위와 최저 순위 */

class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] rank = {1, 2, 3, 4, 5, 6, 6};
        int v = 0;
        for (int number : lottos) {
            if (number == 0) {
                v++;
            } else {
                for (int j = 0; j < win_nums.length; j++) {
                    if (number == win_nums[j]) {
                        win_nums[j] = 0;
                        break;    
                    }
                }
            }
        }
        int remain = 0;
        for (int cnt: win_nums) {
            if (cnt != 0) remain++;
        }
        return new int[]{rank[remain - v], rank[remain]};
    }
}