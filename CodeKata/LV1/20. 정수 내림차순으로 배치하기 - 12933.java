/* [연습문제] 정수 내림차순으로 배치하기 */

import java.util.*;

class Solution {
    public long solution(long n) {
        long answer = 0;
        char[] s = Long.toString(n).toCharArray();
        Arrays.sort(s);
        int left = 0, right = s.length - 1;
        while (left < right) {
            char tmp = s[left];
            s[left++] = s[right];
            s[right--] = tmp;
        }
        System.out.println(s);
        for (int i = 0; i < s.length; i++) {
            answer = answer * 10 + (s[i] - '0');
        }
        return answer;
    }
}

//
public class ReverseInt {
    String res = "";
    public int reverseInt(int n){
        res = "";
        Integer.toString(n).chars().sorted().forEach(c -> res = Character.valueOf((char)c) + res);
        return Integer.parseInt(res);
    }
