/* The problem is equivalent to counting how many factors of 5 appear in n! */

class Solution {
public:
    int trailingZeroes(int n) {
        int answer = 0;
        int ex = 1;
        while (pow(5,ex) <= n){
            answer += n/pow(5,ex);
            ex++;
        }
        return answer;
    }
};
