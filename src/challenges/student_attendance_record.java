class Solution {
    public boolean checkRecord(String s) {
        int aCount = 0;
        int lCount = 0;
        for(int i=0; i<s.length();i++){
            if(s.charAt(i) == 'A'){
                aCount += 1;
                lCount = 0;
                if(aCount == 2){
                    return false;
                }
            }else if(s.charAt(i) == 'L'){
                lCount += 1;
                System.out.println(lCount);
                if(lCount == 3){
                    return false;
                }
            }else{
                lCount = 0;
            }
        }
        return true;
    }
}