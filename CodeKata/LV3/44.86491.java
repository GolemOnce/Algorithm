package CodeKata.LV3;

/* [완전탐색] 최소직사각형 */

class Solution {
    public int solution(int[][] sizes) {
        int taller = 0;
        int shorter = 0;
        for (int[] wallet: sizes) {
            taller = Math.max(Math.max(wallet[0], wallet[1]), taller);
            shorter = Math.max(Math.min(wallet[0], wallet[1]), shorter);
        }
        return taller * shorter;
    }
}