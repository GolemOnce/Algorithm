package CodeKata.LV3;

/* [연습문제] 카드뭉치 */

class Solution {
    public String solution(String[] cards1, String[] cards2, String[] goal) {
        int idx1 = 0;
        int idx2 = 0;
        
        for (String s: goal) {
            if (cards1[idx1].equals(s)) {
                idx1 += 1;
            } else if (cards2[idx2].equals(s)) {
                idx2 += 1;
            } else {
                return "No";
            }
            if (idx1 == cards1.length) idx1 -= 1;
            if (idx2 == cards2.length) idx2 -= 1;
        }
        return "Yes";
    }
}