package CodeKata.LV3;

/* [연습문제] 푸드 파이트 대회 */

class Solution {
    public String solution(int[] food) {
        StringBuilder half = new StringBuilder();
        for (int i = 1; i < food.length; i++) {
            int ad = food[i] / 2;
            for (int j = 0; j < ad; j++) {
                half.append(i);
            }
        }
        return half.toString() + '0' + half.reverse().toString();
    }
}