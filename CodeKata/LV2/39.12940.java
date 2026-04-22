package CodeKata.LV2;

/* [연습문제] 최대공약수와 최소공배수 */

class Solution {
    public int[] solution(int n, int m) {
        int[] answer = {1, 1};
        for (int i = Math.min(n, m); i > 1 ; i--) {
            if ((n % i == 0) && (m % i == 0)) {
                answer[0] = i;
                break;
            }
        }
        int first = Math.max(n, m);
        long cur = (long)first;
        while (!((cur % n == 0) && (cur % m == 0))) {
            cur += (long)first;
        }
        answer[1] = (int)cur;
        return answer;
    }
}

// 유클리드 호제법
class Solution2 {
      public int[] gcdlcm(int a, int b) {
        int[] answer = new int[2];

          answer[0] = gcd(a,b);
        answer[1] = (a*b)/answer[0];
        return answer;
    }

   public static int gcd(int p, int q)
   {
    if (q == 0) return p;
    return gcd(q, p%q);
   }
}