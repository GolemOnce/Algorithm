/* [연습문제] 핸드폰 번호 가리기 */

import java.util.*;

// StringBuilder
class Solution {
    public String solution(String phone_number) {
        int l = phone_number.length();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < l - 4; i++) {
            sb.append('*');
        }
        sb.append(phone_number.substring(l - 4, l));
        return sb.toString();
    }
}

// String > char[] > String
class Solution {
  public String solution(String phone_number) {
     char[] ch = phone_number.toCharArray();
     for(int i = 0; i < ch.length - 4; i ++){
         ch[i] = '*';
     }
     return String.valueOf(ch);
  }
}