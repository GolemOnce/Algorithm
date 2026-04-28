package CodeKata.LV3;

/* [2021 카카오 채용연계형 인턴십] 숫자 문자열과 영단어 */

import java.util.*;

// 문자열 일일이 잘라서 비교
class Solution {
    public int solution(String s) {
        StringBuilder sb = new StringBuilder();
        StringBuilder buf = new StringBuilder();
        String[] str_arr = {"zero", "one", "two", "three", "four", 
                            "five", "six", "seven", "eight", "nine"};
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (Character.isDigit(c)) {
                sb.append(c);
            } else {
                buf.append(c);
                int index = Arrays.asList(str_arr).indexOf(buf.toString());
                if (index != -1) {
                    sb.append((char)('0' + index));
                    buf.setLength(0);
                }
            }
        }
        return Integer.parseInt(sb.toString());
    }
}

//replaceAll() 활용
class Solution2 {
    public int solution(String s) {
        String[] strArr = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        for(int i = 0; i < strArr.length; i++) {
            s = s.replaceAll(strArr[i], Integer.toString(i));
        }
        return Integer.parseInt(s);
    }
}