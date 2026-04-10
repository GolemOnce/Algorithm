/* [연습문제] 정수 제곱근 판별 */

class Solution {
    public long solution(long n) {
        long sqrt = (long)Math.sqrt(n);
        if (sqrt * sqrt == n) return (sqrt + 1) * (sqrt + 1);
        else return -1;
    }
}