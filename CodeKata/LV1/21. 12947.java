/* [연습문제] 하샤드 수 */

// 성능은 이거지만
class Solution {
    public boolean solution(int x) {
        int cur = x;
        int harshad = 0;
        while(cur >= 1) {
            harshad += cur % 10;
            cur /= 10;
        }
        return x % harshad == 0;
    }
}

// Stream방식도 알아두기
class Solution {
    public boolean solution(int x) {
        int harshad = String.valueOf(x).chars().map(c -> c - '0').sum();
        return x % harshad == 0;
    }
}