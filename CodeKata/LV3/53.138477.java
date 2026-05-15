package CodeKata.LV3;

/* [연습문제] 명예의 전당 (1) */

import java.util.*;

class Solution {
    public int[] solution(int k, int[] score) {
        int[] answer = new int[score.length];
        List<Integer> board = new ArrayList<>();
        for (int i = 0; i < score.length; i++) {
            if (board.size() < k) {
                board.add(score[i]);
            } else {
                if (score[i] > board.get(0)) {
                    board.set(0, score[i]);
                }
            }
        Collections.sort(board);
        answer[i] = board.get(0);
        }
        return answer;
    }
}