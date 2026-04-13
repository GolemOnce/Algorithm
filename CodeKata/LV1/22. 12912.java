/* [연습문제] 두 정수 사이의 합 */

// 등차수열 합. 타입 변환 순서 신경 쓰기 (int * int * double != int * double * int)
class Solution {
    public long solution(int a, int b) {
        return (long)((a + b) / 2.0 * (Math.abs(a - b) + 1));
    }
}