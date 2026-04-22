package CodeKata.LV2;

/* [연습문제] 직사각형 별찍기 */

import java.util.*;

class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        sc.close();
        StringBuilder sb = new StringBuilder();
        for (int j = 0; j < a; j++) {
            sb.append('*');
        }            
        for (int i = 0; i < b; i++) {
            System.out.println(sb.toString());
        }
    }
}