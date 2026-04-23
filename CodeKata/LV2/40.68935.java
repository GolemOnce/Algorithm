package CodeKata.LV2;

/* [월간 코드 챌린지 시즌1] 3진법 뒤집기 */

class Solution {
    public int solution(int n) {
        int answer = 0;
        StringBuilder sb = new StringBuilder();
        while(n >= 1) {
            sb.append(n % 3);
            n /= 3;
        }
        //return Integer.parseInt(sb.toString(), 3);
        for (int i = sb.length() - 1; i > -1; i--) {
            answer += (int)Math.pow(3, sb.length() - 1 - i) * (sb.charAt(i) - '0');
        }
        return answer;
    }
}